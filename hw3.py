import numpy as np
import sys


def read_arr(path):
    W = np.zeros((100, 100), dtype=int)
    with open(path, 'r') as f:
        for line in f:
            x, y, w = line.split(' ')
            x = int(x)
            y = int(y)
            w = int(w)
            W[x, y] += w
    return W


def in_round(W, x0, y0, R):
    w_sum = 0
    for x in range(int(x0-R), int(x0+R)+1):
        for y in range(int(y0-R), int(y0+R)+1):
    # for x in range(100):
    #     for y in range(100):
            if (x - x0) ** 2 + (y - y0) ** 2 <= R ** 2 and x >= 0 and y >= 0 and x <= 99 and y <= 99:
                w_sum += W[x, y]
    return w_sum

def max_w(W, R):
    w_max = 0
    x_max = 0
    y_max = 0
    for x0 in range(400):
        for y0 in range(400):
            w_i = in_round(W, x0/4, y0/4, R)
    # for x0 in range(100):
    #     for y0 in range(100):
    #         w_i = in_round(W, x0, y0, R)
            if w_i >= w_max:
                w_max = w_i
                x_max = x0/4
                y_max = y0/4
    return x_max, y_max, w_max


if __name__ == '__main__':
    path = sys.argv[1]
    R = int(sys.argv[2])
    WWW = read_arr(path)
    xMax, yMax, wMax = max_w(WWW, R)
    print(f'{xMax} {yMax} {wMax}')


