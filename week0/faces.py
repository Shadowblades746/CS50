def main():
    print(convert(input("enter a string: ")))


def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str


main()