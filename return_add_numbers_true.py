# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import random
from itertools import combinations


def determine(number_list: list, target_number: int):
    comb = list(combinations(number_list, 2))
    added = [sum(list(i)) for i in comb]
    if target_number in added:
        return True
    else:
        return False


if __name__ == '__main__':
    length = 5
    number_list = [random.randint(0, 10) for i in range(length)]
    target_number = random.randint(0, max(number_list))

    ans = determine(number_list, target_number)
    print("Given List: ", number_list)
    print("Given Target: ", target_number)
    print("If add up: ", ans)
