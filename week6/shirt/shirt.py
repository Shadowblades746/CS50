import sys
import os
from os import path
from PIL import Image, ImageOps


def main():
    error_check()
    image_manipulation(sys.argv[1], sys.argv[2])


def error_check():
    if len(sys.argv) < 3:
        sys.exit("too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("too many command-line arguments")
    elif path.exists(sys.argv[1]) == False:
        sys.exit("file does not exist")
    elif len(sys.argv) == 3:
        file_1, ext_1 = os.path.splitext(sys.argv[1])
        file_2, ext_2 = os.path.splitext(sys.argv[2])
        if (
            not sys.argv[1].endswith(".jpg")
            or sys.argv[1].endswith(".jpeg")
            or sys.argv[1].endswith(".png")
        ):
            sys.exit("not an image file")
        elif ext_1 != ext_2:
            sys.exit("input and output have different extentions")
        else:
            return sys.argv[1] and sys.argv[2]


def image_manipulation(file1, file2):
    pic = Image.open(file1)
    shirt = Image.open("shirt.png")
    cropped_pic = ImageOps.fit(
        pic,
        shirt.size,
        method=Image.Resampling.BICUBIC,
        bleed=0.0,
        centering=(0.5, 0.5),
    )
    cropped_pic.paste(shirt, shirt)
    cropped_pic.save(file2)


if __name__ == "__main__":
    main()
