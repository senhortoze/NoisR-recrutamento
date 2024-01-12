from random import random
import matplotlib.pyplot as plt


def random_walk(num_steps, prob_right, num_particles):

    particle_paths = []

    for i in range(0,num_particles):
        particle_path = [0]
        for x in range(0,num_steps):
            if random() <= prob_right:
                particle_path.append(particle_path[x]+1)
            else:
                particle_path.append(particle_path[x]-1)
        particle_paths.append(particle_path)

    create_plot(num_steps,particle_paths)

    return particle_paths

def create_plot(num_steps, particle_paths):
    time = [x for x in range(len(particle_paths[0]))]

    #Build the plot with all the particles
    for particle_path in particle_paths:
        plt.plot(particle_path, time)

    plt.title("Random Walk -N particles")
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.show()

num_steps = 100 # Number of steps
prob_right = 0.5 # Probability of moving to the right
num_particles = 10 # Number of particles

random_walk(num_steps,prob_right,num_particles)
