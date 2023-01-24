import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as amt


class OneDimensionalFluctuation:
    def __init__(self,
                 *args,
                 length=1,
                 wave_velocity=1,
                 number_split=75,
                 end_time=2.495,
                 phi=lambda x: 0,
                 varphi=lambda x: 0,
                 callbacks=None,
                 left_boundary_situation=1,
                 right_boundary_situation=1,
                 ):
        self.wave_velocity = wave_velocity

        # init basic variables
        self.x_min, self.x_max, self.number_dx = 0, length, number_split  # Discretization of x
        self.t_min, self.t_max, self.number_dt = 0, end_time, int(number_split * end_time)  # Discretization of y

        self.x_ticks = np.linspace(self.x_min, self.x_max, self.number_dx)
        self.t_ticks = np.linspace(self.t_min, self.t_max, self.number_dt)

        self.dx = (self.x_max - self.x_min) / (self.number_dx - 1)
        self.dt = (self.t_max - self.t_min) / (self.number_dt - 1)

        self._time_step = 1

        # init functions
        self.phi = phi
        self.varphi = varphi
        self.callbacks = callbacks
        self.left_boundary_situation = left_boundary_situation
        self.right_boundary_situation = right_boundary_situation

        # the fluctuation
        self.u = np.zeros((self.number_dx, self.number_dt))

        # init u(x, 0)
        for i, x in enumerate(self.x_ticks):
            self.u[i][0] = phi(x)

    def _apply_boundary_situation(self):
        # left
        if self.left_boundary_situation == 1:
            self.u[0][self._time_step] = 0
        elif self.left_boundary_situation == 2:
            self.u[0][self._time_step] = self.u[1][self._time_step]
        else:
            raise ValueError("No such left boundary situation {}".format(self.left_boundary_situation))

        # right
        if self.right_boundary_situation == 1:
            self.u[-1][self._time_step] = 0
        elif self.right_boundary_situation == 2:
            self.u[-1][self._time_step] = self.u[-2][self._time_step]
        else:
            raise ValueError("No such right boundary situation {}".format(self.right_boundary_situation))

    def _next_step(self):
        if self.t_ticks[self._time_step] < self.t_max:
            # calculate each position's next value
            u_t = self.u[:, self._time_step]
            end = len(u_t) - 1
            ddu = list(u_t[0: end - 1] - 2 * u_t[1: end] + u_t[2: end + 1])
            ddu = np.array([0] + ddu + [0])
            self.u[:, self._time_step + 1] = (self.wave_velocity * self.dt / self.dx) ** 2 * ddu + 2 * self.u[:, self._time_step] - self.u[:, self._time_step - 1]

            # apply the boundary situation
            self._time_step += 1
            self._apply_boundary_situation()

            return self._time_step - 1
        else:
            # the iter is over
            return -1

    def run(self):
        while self._time_step < self.number_dt:
            if self.callbacks is not None:
                self.callbacks(self.t_ticks[self._time_step], self.dx, self.u[:, self._time_step])
            result = self._next_step()
            if result == -1:
                break

    def draw(self):
        # get the max u value
        u_max = np.max(self.u)
        for i in range(self.number_dt):
            plt.clf()
            plt.plot(self.x_ticks, self.u[:, i])
            plt.axis((self.x_min - self.x_max / 10, self.x_max + self.x_max / 10, -1.2 * u_max, 1.2 * u_max))
            plt.xlabel("Distance (x), t = {:.2f}(s)".format(self.t_ticks[i]))
            plt.ylabel("u")
            plt.pause(self.dt / 2)
        plt.show()

    def get_animation(self, name, fps=10, interval=None):
        if interval is None:
            interval = self.number_dt / (self.t_max + 1)

        fig, ax = plt.subplots()
        line, = ax.plot(self.x_ticks, self.u[:, 0])
        ax.set_xlim(self.x_min - self.x_max / 10, self.x_max + self.x_max / 10)
        ax.set_ylim(-1.1 * np.max(self.u), 1.1 * np.max(self.u))

        def update(num):
            line.set_ydata(self.u[:, num])
            ax.set_xlabel("t={:.2f}(s)".format(self.t_ticks[num]))

            return line,

        ani = amt.FuncAnimation(fig, update, frames=self.number_dt, interval=interval)
        ani.save('{}.gif'.format(name), fps=fps)
        plt.show()

        return ani

# if __name__ == '__main__':
#     u = OneDimensionalFluctuation(
#         length=1,
#         wave_velocity=1,
#         number_split=100,
#         end_time=2,
#         phi=lambda x: np.sin(3 * np.pi * x),
#         left_boundary_situation=1,
#         right_boundary_situation=1
#     )
#     u.run()
#     u.draw()
#     # u.get_animation("test")


def add_right_power(current_time, dx, ut):
    if current_time < 2:
        ut[-1] = ut[-2] + 10 * dx * np.sin(4 * np.pi * current_time)


if __name__ == '__main__':
    u = OneDimensionalFluctuation(
        callbacks=add_right_power,
        end_time=np.pi
    )
    u.run()
    u.draw()
    # u.get_animation("right_power", fps=20, interval=70)
