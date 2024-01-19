class Lorenz:
    def __init__(self, step, interval:list, parameters:list, init_conditions:list, noise: list):
        self.step = step
        self.interval = interval
        self.parameters = parameters
        self.init_conditions = init_conditions
        self.noise = noise

    def call(self, state, t):
        x, y, z = state
        sigX, sigY, sigZ = self.noise
        sigma, r, b = self.parameters

        dx = sigma * (y - x) + sigX
        dy = x * (r - z) - y + sigY
        dz = x * y - b * z + sigZ

        df = [dx, dy, dz]

        return df