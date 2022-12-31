import validators


def main():
    print(validator(input("What's your email adress? ")))


def validator(s):
    if state := validators.email(s):
        return "valid"
    else:
        return "invalid"


if __name__ == "__main__":
    main()
