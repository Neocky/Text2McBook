import sys
import argparse
import textwrap


def main(input_filename, output_filename, format, characters_per_line) -> None:
    try:
        with open(input_filename, encoding="utf-8") as f:
            text = f.read()

    except FileNotFoundError as exception:
        print(f"Error: {type(exception).__name__}")
        print(f"Error message: {exception}")
        sys.exit()

    # print warning if characters per line is too high, which could risk in missing words
    if characters_per_line >= 21:
        print("Warning: Setting '--charactersperline // -c' too high could result in missing words in books!")

    # split lines every x character 
    lines = textwrap.wrap(text, characters_per_line)
    book_pages = []
    current_book_page = ""

    for line in range(len(lines)):
        # every page consists of 14 lines
        line_count = line % 14
        if line_count == 0 and current_book_page:
            book_pages.append(current_book_page)
            current_book_page = ""
        # create placeholder for linebreaks which gets later replaced
        current_book_page += lines[line] + "<LINEBREAK>"
    # print last book page
    if current_book_page:
         book_pages.append(current_book_page)

    # create output
    with open(output_filename, "w", encoding="utf-8") as book_text:
        book_text.write("Made with Text2McBook by Neocky | https://github.com/Neocky/Text2McBook/\n\n")
        book_text.write(f"Format: {str(format).lower()}\n")
        book_text.write(f"Characters per line: {characters_per_line}\n\n")
        match str(format).lower():
            # could add more formats here
            # Denizen | https://denizenscript.com/ | scripting plugin for minecraft servers
            case "denizen":
                book_text.write("\n")
                for current_book_page in book_pages:
                    # replace new line character with <n> which stands for a new line in a book script container in denizen
                    # already indent line with 4 spaces to work easily with text property of book container: https://meta.denizenscript.com/Docs/Search/book#book%20script%20containers
                    current_book_page = current_book_page.replace("<LINEBREAK>", "<n>")
                    book_text.write(f"    - {current_book_page}\n")

            # Default minecraft book format with give command
            case _:
                # add give command for the book
                # book pages could have less than 14 lines, because we just use a space " " instead of an actual line break symbol here
                mc_give_command_all_pages = str(book_pages).replace("<LINEBREAK>", " ")
                mc_give_command = f"/give @p writable_book{{pages:{mc_give_command_all_pages}}} 1"
                book_text.write(f"Give command:\n{mc_give_command}\n\n")

                # output book in a copy friendly format
                for i, current_book_page in enumerate(book_pages, start=1):
                    # replace new line placeholder with actual new line and output to file
                    current_book_page = current_book_page.replace("<LINEBREAK>", "\n")
                    book_text.write(f"\n ### Page: {i} ###\n")
                    book_text.write(f"{current_book_page}\n")

    # check if book could be unsupported
    if len(book_pages) > 100:
        print(f"Warning: Book has more than 100 pages ({len(book_pages)})! Using the GUI, a player can write a single book up to 100‌[Java Edition only] or 50‌[Bedrock Edition only] pages long!")

    print(f"Text2McBook convertion of '{input_filename}' with format '{str(format).lower()}' completed! Outputfile: {output_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments for Text2McBook",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file", nargs="?", help="Filename of textfile which should be converted to minecraft book format", default="text.txt")
    parser.add_argument("outputfile", nargs="?", help="Filename of output textfile ", default="booktext.txt")
    parser.add_argument("-f", "--format", nargs="?", help="Book format [default, denizen]", default="default")
    parser.add_argument("-c", "--characterlimit", nargs="?", type=int, help="Characters per book line", default=19)
    args = parser.parse_args()

    main(input_filename=args.file, output_filename=args.outputfile, format=args.format, characters_per_line=args.characterlimit)
