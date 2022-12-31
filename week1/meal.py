def main():
    time = input("what time is it? ")
    new_time = convert(time)
    if 8 >= new_time >= 7:
        print("breakfast time")
    elif 13 >= new_time >= 12:
        print("lunch time")
    elif 19 >= new_time >= 18:
        print("dinner time")
    else:
        print()


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    new_time = hours + minutes
    return new_time


if __name__ == "__main__":
    main()