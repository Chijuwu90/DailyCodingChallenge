# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.
#


closing_bracket_list = {")": "(",
                        "]": "[",
                        "}": "{"}


def string_composition_check(input_string):
    for letter in input_string:
        if (letter not in closing_bracket_list.keys()) & (letter not in closing_bracket_list.values()):
            raise KeyError("Unknown symbol in the list")


def if_string_valid(input_string):
    input_string = list(input_string)
    string_composition_check(input_string)

    for n in range(int(len(input_string)/2)):
        for ind, letter in enumerate(input_string):
            if letter in closing_bracket_list.keys():
                if input_string[ind-1] == closing_bracket_list[letter]:
                    input_string.pop(ind)
                    input_string.pop(ind-1)

    if len(input_string) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    input_string = "({[]}(){}"

    if if_string_valid(input_string):
        print("Valid")
    else:
        print("Not Valid")