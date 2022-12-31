import sys
import os
from os import path
from tabulate import tabulate
import csv

menu1 = []


def main():
    error_check()
    menu(sys.argv[1])
    print(tabulate(menu1, headers="keys", tablefmt="grid"))


def error_check():
    if len(sys.argv) < 2:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    elif path.exists(sys.argv[1]) == False:
        sys.exit("file does not exist")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("not a csv file")
    else:
        return sys.argv[1]


def menu(file):
    with open(file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu1.append(row)


if __name__ == "__main__":
    main()
