# Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
import numpy as np


def cal_multiplication(input_list: list):
    length = len(input_list)
    output_list = np.zeros(shape=length)

    for i in range(length):
        temp_list = [input_list[j] for j, x in enumerate(input_list) if j != i]
        output_list[i] = np.prod(temp_list)
    return output_list


if __name__ == '__main__':
    given_list = [1, 2, 3, 4, 5]
    output = cal_multiplication(given_list)
    print(output)
