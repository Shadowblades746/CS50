def main():
    variable = input("camelCase: ")
    case_converter(variable)


def case_converter(variable):
    for c in variable:
        if c.islower():
            print(c, end="")
        else:
            print("_" + c.lower(), end="")
    print("")


if __name__ == "__main__":
    main()


