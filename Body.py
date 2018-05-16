import numpy as np

class Body:
    def __init__(self, mass, position):
        self.position = position
        self.mass = mass


class MobileBody(Body):
    def __init__(self, mass, position, velocity, acceleration):
        super().__init__(mass, position)
        self.velocity = velocity
        self.acceleration = acceleration

    def add_force(self, force):
        self.acceleration += force/self.mass

    def interact(self, other_body):
        grav_constant = 6.67408e-11
        distance = np.sqrt(abs(self.position**2 - other_body.position**2))
        direction = (self.position - other_body.position) / distance
        force = (grav_constant * self.mass * other_body.mass) / distance**2 * direction
        return force


class FixedBody(Body):
    def __init__(self, mass, position):
        super().__init__(mass, position)
