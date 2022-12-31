import sys
import csv
import os
from os import path

clean_list = []


def main():
    error_check()
    cleanup(sys.argv[1])
    cleaned_list(sys.argv[2])


def error_check():
    if len(sys.argv) < 3:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("too many command-line arguments")
    elif path.exists(sys.argv[1]) == False:
        sys.exit("file does not exist")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("not a csv file")
    else:
        return sys.argv[1]


def cleanup(file):
    with open(file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            clean_list.append(
                {"first": first.lstrip(), "last": last, "house": row["house"]}
            )


def cleaned_list(file):
    with open(file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(clean_list)


if __name__ == "__main__":
    main()
