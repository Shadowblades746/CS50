def main():
    greet = input("Greeting: ")
    greeting(greet)


def greeting(greet):
    greet = greet.strip()
    greet = greet.lower()
    if greet[0:5] == "hello":
        print("$0")
    elif greet[0] == "h":
        print("$20")
    else:
        print("$100")


main()