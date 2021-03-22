import sys
import textwrap

try:
    f = open("text.txt", "r")
except FileNotFoundError:
    print("Error: File 'text.txt' wasn't found. Make sure it is in the same directory as this script and run again.")
    input("Press any key + Enter to end program...")
    sys.exit()

text = f.read()
lines = textwrap.wrap(text, 19)
i = 0
fi = open("booktext.txt", "w")
fi.write("Made with Text2McBook  | By Neocky | https://github.com/Neocky/Text2McBook/")

for line in range(len(lines)):
    summ = line % 14
    if summ == 0:
        i += 1
        fi.write("\n")
        fi.write(f" ### Page: {i} ###\n")
    fi.write(lines[line] + "\n")
