import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
        return (
            int(matches.group(1)) in range(0, 256)
            and int(matches.group(2)) in range(0, 256)
            and int(matches.group(3)) in range(0, 256)
            and int(matches.group(4)) in range(0, 256)
        )
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
