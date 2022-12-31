def main():
    expresion = input("Expression: ")
    calculator(expresion)


def calculator(expresion):
    expresion = expresion.strip()
    x, y, z = expresion.split()
    x = int(x)
    z = int(z)
    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/":
        print(float(x / z))


main()
