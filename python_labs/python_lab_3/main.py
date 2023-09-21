import argparse
import numpy
import os
import math

def main(number: int) -> int:
    total = 0
    init_num = 1
    for i in range(number):
        if int((str(init_num**3))[0]) % 2 == 0:
            total += init_num**3
        init_num += 1
    print(total)
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)
