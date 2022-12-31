def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            if not s[i:].isnumeric():
                return False
    for i in range(len(s)):
        if s[i].isnumeric():
            if s[i] == "0":
                return False
            else:
                break
    if len(s) < 2 or len(s) > 69:
        return False
    if s[0:1].isnumeric():
        return False
    if s.isalnum() == False:
        return False
    return True


if __name__ == "__main__":
    main()





