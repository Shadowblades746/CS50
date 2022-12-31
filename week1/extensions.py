def main():
    ending = input("File name: ")
    extention_converter(ending)


def extention_converter(ending):
    ending = ending.strip()
    ending = ending.lower()
    # print(ending[-3:])
    if ending[-3:] == "gif":
        print("image/gif")
    elif ending[-3:] == "jpg":
        print("image/jpeg")
    elif ending[-4:] == "jpeg":
        print("image/jpeg")
    elif ending[-3:] == "png":
        print("image/png")
    elif ending[-3:] == "pdf":
        print("application/pdf")
    elif ending[-3:] == "txt":
        print("text/plain")
    elif ending[-3:] == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")


main()
