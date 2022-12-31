import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "([1-9]|1[0-2])(?::([0-5][0-9]))? ([AP]M)"
    if times := re.search(r"^" + regex + " to " + regex + "$", s):
        t = times.groups()
        return f"{convert_time(t[:3])} to {convert_time(t[3:])}"
    raise ValueError


def convert_time(time):
    if time[2] == "PM":
        if time[0] == "12":
            hours = "12"
        else:
            hours = str(int(time[0]) + 12).zfill(2)
    if time[2] == "AM":
        if time[0] == "12":
            hours = "00"
        else:
            hours = time[0].zfill(2)
    if time[1] == None:
        minutes = "00"
    else:
        minutes = time[1].zfill(2)
    return hours + ":" + minutes


if __name__ == "__main__":
    main()
