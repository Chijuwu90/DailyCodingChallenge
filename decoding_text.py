# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

import numpy as np
import time


def create_number_list():
    num = np.arange(1, 27)
    num = [str(i) for i in num]
    return num


def create_letter_list():
    letter_list = []
    alpha = 'a'
    for i in range(0, 26):
        letter_list.append(alpha)
        alpha = chr(ord(alpha) + 1)
    return letter_list


def splitter(input_encode):
    for i in range(1, len(input_encode)):
        start = input_encode[0:i]
        end = input_encode[i:]
        yield start, end
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result


def find_valid_list(num, combinations):
    valid_list = []
    for com in combinations:
        if len((set(num) | set(com)) - set(num)) == 0:
            valid_list.append(com)
    return valid_list


def mapping_to_letter(valid_list, letter_list):
    valid_letter_list = []
    for valid in valid_list:
        letters = [letter_list[int(i)-1] for i in valid]
        valid_letter_list.append(letters)
    return valid_letter_list


if __name__ == "__main__":
    input_test = input("enter number: ")
    start = time.time()

    number_list = create_number_list()
    letter_list = create_letter_list()
    combinations = list(splitter(input_test))
    valid_number_list = find_valid_list(number_list, combinations)
    valid_letter_list = mapping_to_letter(valid_number_list, letter_list)
    end = time.time()

    if len(valid_letter_list) != 0:
        print("possible combinations: ", valid_number_list)
        print("possible letters     :", valid_letter_list)
        print("total number of possibilities: ", len(valid_letter_list))
        print("Time taken: ", end-start)
    else:
        print("Entered number is not valid.")

