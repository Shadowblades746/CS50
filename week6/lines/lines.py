import sys
import os
from os import path


def main():
    error_check()
    print(line_counter(sys.argv[1]))


def error_check():
    if len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    elif path.exists(sys.argv[1]) == False:
        sys.exit("file does not exist")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("not a python file")
    else:
        return sys.argv[1]


def line_counter(file):
    with open(file) as file:
        lines = file.read().splitlines()
        line_count = len(lines)
        invalid_lines = 0
        for line in lines:
            linestripped = line.rstrip().strip().split("\n")
            for line in linestripped:
                if len(line) < 1 or line.startswith("#"):
                    invalid_lines += 1
        return line_count - invalid_lines


if __name__ == "__main__":
    main()
