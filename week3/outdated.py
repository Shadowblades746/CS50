months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


def date_input():
    date = input("Date: ")
    date = date.strip()
    try:
        month, day, year = date.split("/")
        month = month.zfill(2)
        day = day.zfill(2)
        if int(month) in range(1, 12) and int(day) in range(1, 31):
            print(f"{year}-{month}-{day}")
        else:
            date_input()
    except ValueError:
        try:
            month_day, year = date.split(",")
            month, day = month_day.split(" ")
            day = day.zfill(2)
            year = str(year)
            year = year.strip()
            month = month.title()
            month = months[month]
            if int(month) in range(1, 12) and int(day) in range(1, 31):
                print(f"{year}-{month}-{day}")
            else:
                date_input()
        except ValueError:
            date_input()
        except KeyError:
            date_input()


def main():
    date_input()


if __name__ == "__main__":
    main()
