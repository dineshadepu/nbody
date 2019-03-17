import numpy as np
from nbody.dem import (interparticle_force, body_force, soil_step)
from pysph.base.utils import get_particle_array
from pysph.tools.geometry import get_2d_tank
import matplotlib.pyplot as plt


class BouncingBalls():
    def initialize(self):
        pass

    def create_particles(self):
        spc = 0.1
        x, y = np.mgrid[0:1:spc, 0:1:spc]
        soil = get_particle_array(x=x, y=y, m=1, fx=0, fy=0, rad=spc / 2)

        x, y = get_2d_tank(spc, [0.45, -0.3], 2, 2, 2)
        wall = get_particle_array(x=x, y=y, m=1, rad=spc / 2)
        # import matplotlib.pyplot as plt
        # plt.scatter(tank.x, tank.y)
        # plt.scatter(soil.x, soil.y)
        # plt.show()

        return [soil, wall]

    def run(self):
        self.initialize()
        tf = 0.3
        t = 0
        dt = 1e-3

        [soil, tank] = self.create_particles()
        kn = 1e3

        while t < tf:
            body_force(soil)
            interparticle_force(soil.x, soil.y, soil.fx, soil.fy, soil.rad,
                                tank.x, tank.y, tank.rad, kn)
            interparticle_force(soil.x, soil.y, soil.fx, soil.fy, soil.rad,
                                soil.x, soil.y, soil.rad, kn)
            soil_step(soil, dt)
            t = t + dt
            print(t)
        plt.scatter(tank.x, tank.y)
        plt.scatter(soil.x, soil.y)
        plt.show()


if __name__ == '__main__':
    a = BouncingBalls()
    a.run()
