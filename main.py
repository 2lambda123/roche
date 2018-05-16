import numpy as np
import Body


def update():
    pass


if __name__ == '__main__':
    # Simulation parameters
    t_max = 60
    dt = 0.1

    # Body parameters
    num_bodies = 5
    mass = 10*np.random.rand(num_bodies)
    position = 5*np.random.rand(3, num_bodies)
    velocity = 5*np.random.rand(3, num_bodies)
    acceleration = 5*np.random.rand(3, num_bodies)

    # Create and initialize bodies
    body = []
    for i in range(num_bodies):
        body.append(Body.MobileBody(mass[i], position[:, i], velocity[:, i], acceleration[:, i]))

    # Perform simulation
    t = 0
    while t < t_max:
        # Draw current state
        # TODO: Draw current state

        for i in range(num_bodies):
            # Calculate interactions with other bodies
            for j in range(num_bodies):
                if i != j:
                    force = body[i].interact(body[j])
                    body[i].add_force(force)
            # Move body
            body[i].position += velocity * dt + acceleration * dt * dt
        # Update time
        t += dt
