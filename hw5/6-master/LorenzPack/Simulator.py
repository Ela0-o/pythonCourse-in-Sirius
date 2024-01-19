import numpy as np
from scipy.integrate import odeint
from LorenzPack.Attractor import Lorenz



class Simulator(Lorenz):
    def __init__(self, step, interval, parameters, init_conditions, noise):
        super().__init__(step, interval, parameters, init_conditions, noise)

    def run(self):

        t0, t1 = self.interval
        t = np.linspace(t0, t1, int((t1 - t0) / self.step))
        xyz_val = odeint(self.call, self.init_conditions, t)

        return xyz_val