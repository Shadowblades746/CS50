import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ").title()
        names.append(name)
        output = p.join(names)
    except EOFError:
        print("Adieu, adieu, to", output)
        break
