import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import Body


def draw(bodies):
    # Create figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw bodies
    for body in bodies:
        x, y, z = body.position
        ax.scatter(x, y, z)

    # Show the figure
    plt.show()


if __name__ == '__main__':
    # Simulation parameters
    t_max = 60
    dt = 0.1

    # Body parameters
    num_bodies = 30
    mass = 100*np.random.rand(num_bodies) + 10
    position = 5*np.random.rand(3, num_bodies)
    velocity = np.zeros((3, num_bodies))
    acceleration = np.zeros((3, num_bodies))

    # Create and initialize bodies
    body = []
    for i in range(num_bodies):
        body.append(Body.MobileBody(mass[i], position[:, i], velocity[:, i], acceleration[:, i]))

    # Perform simulation
    t = 0
    while t < t_max:
        # Draw current state
        draw(body)

        for i in range(num_bodies):
            # Calculate interactions with other bodies
            for j in range(num_bodies):
                if i != j:
                    force = body[i].interact(body[j])
                    body[i].add_force(force)
            # Update body position and velocity
            body[i].velocity += body[i].acceleration * dt * dt
            body[i].position += body[i].velocity * dt
        # Update time
        t += dt
