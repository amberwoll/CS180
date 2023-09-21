import json
import string
import argparse
import os

def main(inputString):
    words = inputString.split()

    quantities = {}

    for word in words:
        word = word.strip(string.punctuation).lower()
        if word in quantities:
            quantities[word] += 1
        else:
            quantities[word] = 1

    with open("word-counts.json", "w") as json_file:
        json.dump(quantities, json_file)

    return "word-counts.json"

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)