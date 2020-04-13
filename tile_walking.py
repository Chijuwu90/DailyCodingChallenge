import numpy as np

matrix = np.array([[1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 1, 0, 1],
                   [0, 1, 1, 1, 1, 0, 1],
                   [0, 1, 0, 0, 0, 0, 1],
                   [0, 1, 1, 1, 1, 0, 1],
                   [0, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1]])


matrix_size = matrix.shape
n_loop = matrix_size[0]*matrix_size[1]

directions = {"r": [0, 1], "l": [0, -1], "u": [-1, 0], "d": [1, 0]}
counter_directions = {"r": "l", "l": "r", "u": "d", "d": "u"}


def check_start_end_valid(start, end):
    if matrix[start[0]][start[1]] == 0:
        raise ValueError('Start cannot be a Wall node')
    elif matrix[end[0]][end[1]] == 0:
        raise ValueError('End cannot be a Wall node')
    elif start == end:
        raise ValueError('End cannot be Start')
    else:
        if start > end:
            buffer = end
            end = start
            start = buffer
        return start, end


def bound_check(path):
    boundary_check = {}
    for direction in path:
        if len(direction) == 1:
            boundary_check[direction] = any((n < 0) | (n > matrix_size[0]-1) for n in path[direction][0])
        elif len(direction):
            boundary_check[direction] = any((n < 0) | (n > matrix_size[0]-1) for n in path[direction][-1])

    keep_direction = [k for k in boundary_check.keys() if not boundary_check[k]]
    path = {i: path[i] for i in keep_direction}
    return path


def path_valid_check(path):
    for key in list(path.keys()):
        route = path[key]
        if len(route) == 1:
            val = matrix[route[0][0]][route[0][1]]
            if val == 0:
                del path[key]
        else:
            for r in route:
                val = matrix[r[0]][r[1]]
                if val == 0:
                    del path[key]
    return path


def end_check(path, end):
    if_end_path = {key: path[key] for key in path.keys() if path[key][-1] == end}
    path_val, path_cor = get_matrix_val(if_end_path)
    final_path = get_valid_path(path_val)

    if len(final_path) > 0:
        return True, if_end_path
    else:
        return False, path


def get_matrix_val(path):
    path_val = {}
    path_cor = {}
    for key in path.keys():
        route = path[key]
        vals = [''] * len(route)
        for i, r in enumerate(route):
            vals[i] = matrix[r[0]][r[1]]
        path_val[key] = vals
        path_cor[key] = route
    return path_val, path_cor


def get_valid_path(path_val):
    final_path = path_val
    for key in list(final_path.keys()):
        if 0 in final_path[key]:
            del final_path[key]
        else:
            pass
    return final_path


def run(start, end):

    start, end = check_start_end_valid(start, end)

    path = {}
    for loop in range(int(n_loop/2)):

        existing_path = path.keys()
        if len(existing_path) == 0:

            # first step
            path = {k: [[sum(x) for x in zip(start, directions[k])]] for k in directions}
            path = bound_check(path)

        else:
            for key in list(path.keys()):
                try:
                    for direction in directions.keys():
                        if key[-1] == direction:
                            path = {key+k: [[sum(x) for x in zip(path[key][0], directions[k])]]
                                    for k in directions if counter_directions[k] != key[-1]} if len(key) == 1 \
                                else \
                                {**path, **{key + k: path[key] + [[sum(x) for x in zip(path[key][-1], directions[k])]]
                                            for k in directions if counter_directions[k] != key[-1]}}

                            del path[key]
                            path = bound_check(path)
                            path = path_valid_check(path)
                except:
                    pass

        if_end, path = end_check(path, end)
        if if_end:
            path_val, path_cor = get_matrix_val(path)
            final_path = get_valid_path(path_val)
            if len(final_path) > 0:
                return loop, final_path, path_cor
            else:
                pass
        else:
            pass
    return 0, None, None


if __name__ == '__main__':
    print("Given Matrix: \n", matrix)
    print("\n")

    start_at = input("start at (insert coordinate, e.g, 0,0): ")
    end_at = input("end at (insert coordinate, e.g, 1,1): ")
    start_at = [int(x) for x in start_at.split(",")]
    end_at = [int(x) for x in end_at.split(",")]
    n, final_path, path_cor = run(start_at, end_at)

    if final_path is None:
        print("No possible route found.")
    else:
        print("Shortest path length: ", n + 1)
        print("Possible routes: ", list(final_path.keys()), list(path_cor.values())[0])
