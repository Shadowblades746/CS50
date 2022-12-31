def main():
    percentage = converter()
    print(percentage)


def converter():
    while True:
        try:
            fraction = input("Fraction: ")
            numerator, denominator = fraction.split("/")
            if int(numerator) > int(denominator):
                while True:
                    fraction = input("Fraction: ")
                    numerator, denominator = fraction.split("/")
                    if numerator < denominator:
                        break
            percentage = round((int(numerator)) / round(int(denominator)) * 100)
            if percentage >= 99:
                return "F"
            elif percentage <= 1:
                return "E"
            percentage = str(int(percentage)) + "%"
            return percentage
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
