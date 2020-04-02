import numpy as np
import random
import time
import matplotlib.pyplot as plt


def min_positive_val(input_arr):
    input_arr.sort()

    positive_array = [i for i in input_arr if i > 0]
    for ind, val in enumerate(positive_array):
        if ind+1 < val:
            return ind+1
        else:
            return max(positive_array)+1


if __name__ == '__main__':
    N = [1, 10, 100, 1000, 10000, 100000, 1000000]
    timer = np.zeros(shape=len(N))

    for t, length in enumerate(N):
        random_array = [random.randint(-1000, 1000) for i in range(length)]

        start = time.time()
        val = min_positive_val(random_array)
        print(val)
        end = time.time()
        timer[t] = end - start

    plt.plot(N, timer, '.')
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
