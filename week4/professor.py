import random


def main():
    score = 0
    error = 0

    levelchoice = get_level()
    for i in range(10):
        x = generate_integer(int(levelchoice))
        y = generate_integer(int(levelchoice))
        answer = x + y
        guess = int(input(f"{x} + {y} = "))
        if guess == answer:
            score += 1
        while guess != answer:
            print("EEE")
            error += 1
            if error == 3:
                print(f"Answer: {answer}")
                error = 0
                break
            guess = int(input(f"{x} + {y} = "))
            if guess == answer:
                score += 1
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Select Level: "))
            if level not in range(1, 4):
                raise ValueError
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
