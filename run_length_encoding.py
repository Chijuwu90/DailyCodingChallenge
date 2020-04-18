# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".


def run_length(input_string):
    diff_ind = []
    diff_letter = []

    starting = input_string[0]
    for i in range(1, len(input_string)):
        if input_string[i] != input_string[i-1]:
            diff_ind.append(i)
            diff_letter.append(input_string[i])

    diff = [diff_ind[0]] + [diff_ind[i] - diff_ind[i-1] for i in range(1, len(diff_ind))]
    diff.append(len(input_string)-diff_ind[-1])

    letters = [starting] + diff_letter

    output = ""
    for x, y in zip(diff, letters):
        output = output + str(x) + y

    return output


if __name__ == '__main__':
    input_string = "ABBBCDDCDAAC"
    output = run_length(input_string)
    print(output)
