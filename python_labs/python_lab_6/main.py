import argparse

def main(number):
    string_num = str(number)
    if string_num[0] != string_num[-1]:
        print("False")
        return 0
    elif len(string_num) == (0 or 1):
        print("True")
        return 0
    new_num = int(string_num[1:-1])
    return main(new_num)

if __name__ == "__main__":
    arg = argparse.ArgumentParser("Pallindrome Checker")
    arg.add_argument("--x", type=int, help="Input a number to determine if it's a pallindrome")
    parsed = arg.parse_args()
    main(parsed.x)