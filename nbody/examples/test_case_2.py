import numpy as np
from nbody.dem import (interparticle_force, body_force, soil_step)
from pysph.base.utils import get_particle_array
from pysph.tools.geometry import get_2d_tank
import matplotlib.pyplot as plt


class BouncingBalls():
    def initialize(self):
        pass

    def create_particles(self):
        spc = 0.3
        x = np.array([0, 0])
        y = np.array([0, 0.2])
        soil = get_particle_array(x=x, y=y, m=1, fx=0, fy=0, rad=spc / 2)

        x, y = get_2d_tank(spc, [0.45, -0.3], 2, 2, 2)
        wall = get_particle_array(x=x, y=y, m=1, rad=spc / 2)

        return [soil, wall]

    def run(self):
        self.initialize()

        [soil, wall] = self.create_particles()
        kn = 1e3
        # before computing the force it should be zero
        np.testing.assert_almost_equal(soil.fx, np.array([0., 0.]))
        np.testing.assert_almost_equal(soil.fy, np.array([0., 0.]))
        interparticle_force(soil.x, soil.y, soil.fx, soil.fy, soil.rad,
                            soil.x, soil.y, soil.rad, kn)
        assert(soil.fx[0] == -soil.fx[1])
        assert(soil.fy[0] == -soil.fy[1])
        assert(soil.fx[0] == 0)
        assert(soil.fx[1] == 0)

        assert(soil.fy[0] < 0)
        assert(soil.fy[1] > 0)


if __name__ == '__main__':
    a = BouncingBalls()
    a.run()
