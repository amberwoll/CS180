import argparse

def main(inputString):
    # Write the code to reverse the string here
    new_string = ''
    number_of_characters = len(inputString)
    for a in range(number_of_characters):
        new_string += inputString[-1]
        inputString = inputString[:-1]

    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    
    print(new_string)

if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser("String Reverser")
    argumentParser.add_argument("--string", type=str, help="Input a string to reverse")
    parsed = argumentParser.parse_args()
    main(parsed.string)