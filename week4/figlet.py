import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) < 1 or len(sys.argv) > 3 or sys.argv[1] != "-f":
    sys.exit("invalid use")

if len(sys.argv) < 2:
    text = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(text))
elif len(sys.argv) >= 2 and sys.argv[1] == "-f":
    text = input("input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
