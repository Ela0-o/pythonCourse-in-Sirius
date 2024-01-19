from matplotlib import pyplot as plt
from LorenzPack.Simulator import Simulator
import numpy as np


def plot_points(arr):

    xL = []
    yL = []
    zL = []

    for i in arr:
        xL.append(i.tolist()[0])
        yL.append(i.tolist()[1])
        zL.append(i.tolist()[2])

    fig = plt.figure()
    fig3d = fig.add_subplot(projection='3d')

    fig3d.plot(xL, yL, zL, '.b')
    fig3d.set_xlabel("X")
    fig3d.set_ylabel("Y")
    fig3d.set_zlabel("Z")

    # plt.savefig('Lorenz Attractor (points)')
    plt.show()


def plot_line(arr):
    fig = plt.figure()
    fig3d = fig.add_subplot(projection='3d')

    xL = []
    yL = []
    zL = []

    for i in arr:
        xL.append(i.tolist()[0])
        yL.append(i.tolist()[1])
        zL.append(i.tolist()[2])

    fig3d.plot(xL, yL, zL, 'b', lw=0.5)
    fig3d.set_xlabel("X")
    fig3d.set_ylabel("Y")
    fig3d.set_zlabel("Z")
    fig3d.set_title("Lorenz Attractor")

    # plt.savefig('Lorenz Attractor (line)')
    plt.show()

def three_projection(arr):
    xL = []
    yL = []
    zL = []

    for i in arr:
        xL.append(i.tolist()[0])
        yL.append(i.tolist()[1])
        zL.append(i.tolist()[2])

    plt.plot(xL, yL, label='y(x)')
    plt.plot(yL, zL, label='z(y)')
    plt.plot(zL, xL, label='x(z)')

    plt.legend()

    plt.savefig('Lorenz Attractor (3 проекции)')

    plt.show()

if __name__ == '__main__':
    step = 0.05
    interval = [0, 1000]
    parameters = [6, 30, 10/3]
    init_conditions = [0, 1, 1]
    noise = np.random.standard_normal(3)

    sim = Simulator(step, interval, parameters, init_conditions,noise)
    arr = sim.run()
    print(arr)
    plot_points(arr)
    plot_line(arr)
    three_projection(arr)