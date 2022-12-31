import sys
import requests
import json


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        count = sys.argv[1]
    bitcoin_price(count)


def bitcoin_price(count):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    output = response.json()
    rate_float = output["bpi"]["USD"]["rate_float"]
    print(f"${rate_float * float(count):,.4f}")


if __name__ == "__main__":
    main()

