def main():
    word = input("Input: ")
    vowels = "aeiouAEIOU"
    for char in vowels:
        word = word.replace(char, "")
    print(word)


if __name__ == "__main__":
    main()
