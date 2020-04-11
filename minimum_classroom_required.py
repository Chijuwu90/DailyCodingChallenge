# This problem was asked by Snapchat.
#
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

import numpy as np


def transform_time_to_set(given_list):
    sets = []
    for i, class_time in enumerate(given_list):
        time_period_set = np.arange(class_time[0], class_time[1]+1)
        sets.append(time_period_set)
    return sets


def run(given_list):
    max_minute = max(max(given_list))
    number_room_required_per_min = np.zeros([max_minute+1, 1])
    time_sets = transform_time_to_set(given_list)

    for time_set in time_sets:
        for i in time_set:
            number_room_required_per_min[i] = number_room_required_per_min[i] + 1

    return int(max(number_room_required_per_min)[0])


if __name__ == '__main__':
    given_class_time = [(30, 75), (0, 50), (60, 150), (100, 150)]
    class_number = run(given_class_time)
    print("classroom number required: ", class_number)
