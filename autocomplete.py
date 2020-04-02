# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

import pandas as pd

word_database = ["dog", "deer", "deal", "apple", "apes", "banana", "bases", "beep"]


def create_database_df(word_database):
    df = pd.DataFrame(word_database, columns=["word"])
    return df


def create_key_df(input_string):
    string_length = len(input_string)
    df = create_database_df(word_database)
    df["keys"] = df["word"].apply(lambda x: x[0:string_length])
    result_word = filter_key(input_string, df)
    return result_word.tolist()


def filter_key(input_string, df):
    df = df[df["keys"] == input_string]
    return df["word"]


if __name__ == "__main__":
    input_string = input("input prefix: ")
    result = create_key_df(input_string)
    if len(result) == 0:
        print("No similar word found.")
    else:
        print("Similar words are: ", result)


