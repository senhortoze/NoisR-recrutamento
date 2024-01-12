import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def simulate_colision(left, right, velocity_left, velocity_right, mass_left, mass_right, num_frames, box_size):
    ball1_x = [left]
    ball2_x = [right]

    for i in range(0,num_frames):
        if (left + velocity_left + 0.1) >= (right + velocity_right - 0.1):
            velocity_left, velocity_right = (2*mass_right*velocity_right + velocity_left*(mass_left-mass_right))/(mass_left + mass_right), velocity_left + ((2*mass_right*velocity_right + velocity_left*(mass_left-mass_right))/(mass_left + mass_right)) - velocity_right
        else:
            if (left + velocity_left - 0.1) <= 0:
                velocity_left = -velocity_left

            if (right + velocity_right + 0.1) >= box_size:
                velocity_right = -velocity_right

        left += velocity_left
        right += velocity_right

        ball1_x.append(left)
        ball2_x.append(right)

    create_animation(ball1_x, ball2_x, box_size)

def create_animation(positions1, positions2, box_size) :
    num_frames = len(positions1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, box_size)
    ax.set_ylim(-0.1, 0.1)

    ball1,= ax.plot(positions1[0], 0, 'bo', markersize=10)
    ball2,= ax.plot(positions2[0], 0, 'ro', markersize = 10)

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2

    ani = FuncAnimation (fig, update, frames=num_frames, blit=True )
    plt.show()

    plt.close(fig)

#Valores iniciais da posições/velocidades
pos1 = 1
pos2 = 4
velocity1 = 0.1
velocity2 = -0.1

mass1 = 1
mass2 = 2
num_frames = 500
box_size = 5

#Define a bola da esquerda e a bola da direita
if pos1 == pos2:
    print('As bolas não podem transgredir as Leis da Física')
    exit()
elif pos1 < pos2:
    left = pos1
    velocity_left = velocity1
    mass_left = mass1

    right = pos2
    velocity_right = velocity2
    mass_right = mass2
else:
    left = pos2
    velocity_left = velocity2
    mass_left = mass2

    right = pos1
    velocity_right = velocity1
    mass_right = mass1



simulate_colision(left, right, velocity_left, velocity_right, mass_left, mass_right, num_frames, box_size)