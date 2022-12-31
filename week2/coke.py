def main():
    price = 50
    while price != 0:
        coin = int(input("insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            price -= coin
            if price > 0:
                print("amount due:", price)
            else:
                print("change owed:", -price)
                break
        else:
            print("amount due:", price)
            continue


if __name__ == "__main__":
    main()
