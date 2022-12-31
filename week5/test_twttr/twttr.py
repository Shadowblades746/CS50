def main():
    word = input("input: ")
    shorten(word)


def shorten(word):
    vowels = "aeiou"
    for char in vowels:
        word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()