import sys
import argparse
import textwrap

from pathlib import Path


def main(input_filename: str, output_filename: str, format: str, characters_per_line: int) -> None:
    try:
        with open(input_filename, encoding="utf-8") as f:
            text = f.read()

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)
    except OSError as e:
        print(f"OSError: {e}")
        sys.exit(1)

    # print warning if characters per line is too high, which could risk in missing words
    if characters_per_line >= 21:
        print("Warning: Setting '--charactersperline // -c' too high could result in missing words in books!")

    # split lines every x character 
    lines = textwrap.wrap(text, characters_per_line)
    book_pages: list[str] = []
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

    normalized_format: str = format.lower()
    # create output
    with open(output_filename, "w", encoding="utf-8") as book_text:
        output: list[str] = []
        output.append("Made with Text2McBook by Neocky | https://github.com/Neocky/Text2McBook/\n\n")
        output.append(f"Format: {normalized_format}\n")
        output.append(f"Characters per line: {characters_per_line}\n\n")
        match normalized_format:
            # could add more formats here
            # Denizen | https://denizenscript.com/ | scripting plugin for minecraft servers
            case "denizen":
                output.append("\n")
                for page in book_pages:
                    # replace new line character with <n> which stands for a new line in a book script container in denizen
                    # already indent line with 4 spaces to work easily with text property of book container: https://meta.denizenscript.com/Docs/Search/book#book%20script%20containers
                    formatted_page = page.replace("<LINEBREAK>", "<n>")
                    output.append(f"    - {formatted_page}\n")

            # Default minecraft book format with give command
            case _:
                # add give command for the book
                # book pages could have less than 14 lines, because we just use a space " " instead of an actual line break symbol here
                mc_give_command_all_pages = str(book_pages).replace("<LINEBREAK>", " ")
                mc_give_command: str = (
                    f"/give @p writable_book[minecraft:writable_book_content={{pages:{mc_give_command_all_pages}}}] 1"
                )
                output.append(f"Give command:\n{mc_give_command}\n\n")

                # output book in a copy friendly format
                for i, page in enumerate(book_pages, start=1):
                    # replace new line placeholder with actual new line and output to file
                    formatted_page: str = page.replace("<LINEBREAK>", "\n")
                    output.append(f"\n### Page: {i} ###\n{formatted_page}\n")

        book_text.write("".join(output))

    # check if book could be unsupported
    if len(book_pages) > 100:
        print(f"Warning: Book has more than 100 pages ({len(book_pages)})! Using the GUI, a player can write a single book up to 100[Java Edition only] or 50[Bedrock Edition only] pages long!")

    print(f"Text2McBook convertion of '{input_filename}' with format '{normalized_format}' completed!\nOutputfile: {output_filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Arguments for Text2McBook",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("file", nargs="?", type=str,
                        help="Filename of textfile which should be converted to minecraft book format",
                        default=str(Path(__file__).parent / "text.txt"))
    parser.add_argument("outputfile", nargs="?", type=str,
                        help="Filename of output textfile ",
                        default=str(Path(__file__).parent / "booktext.txt"))
    parser.add_argument("-f", "--format", nargs="?", type=str,
                        help="Book format [default, denizen]",
                        default="default")
    parser.add_argument("-c", "--characterlimit", nargs="?", type=int,
                        help="Characters per book line",
                        default=19)
    args = parser.parse_args()

    main(input_filename=args.file, output_filename=args.outputfile, format=args.format, characters_per_line=args.characterlimit)
