# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)

import random
import time


def find_max_in_subarray(arr):
    k = random.randint(1, len(arr))
    arr = [int(arr[i]) for i, _ in enumerate(arr)]

    result = [] * (len(arr)-k)
    for i in range(0, len(arr)-k+1):
        result.append(max(arr[i:i+k]))

    return k, result


if __name__ == '__main__':
    given_array = input("input array: ")

    if "," in given_array:
        given_array = given_array.split(",")
    else:
        given_array = given_array.split(" ")

    start = time.time()
    k, output_list = find_max_in_subarray(given_array)
    end = time.time()

    print("given_array: ", given_array)
    print("k: ", k)
    print("result: ", output_list)
    print("time elapsed: ", end-start)
