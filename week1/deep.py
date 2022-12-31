answer = input(
    "what is the answer to the great question of life, the universe and everything? "
)
answer = answer.lower()
answer = answer.strip()
match answer:
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("no")