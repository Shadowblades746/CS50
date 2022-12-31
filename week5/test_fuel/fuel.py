import math


def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))



def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        if numerator > denominator:
            while True:
                fraction = input("Fraction: ")
                numerator, denominator = fraction.split("/")
                if numerator < denominator:
                    break
        percentage = math.ceil(int(numerator) / int(denominator) * 100)
        return percentage
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    percentage = f"{percentage}%"
    return percentage



if __name__ == "__main__":
    main()
