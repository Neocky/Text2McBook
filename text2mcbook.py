import textwrap

template = "{Count:1,id:\"minecraft:writable_book\",tag:{pages:TEMPLATE_LIST}}"


def main():
    try:
        with open("text.txt", encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        with open("text.txt", "w", encoding='utf-8') as f:
            print("Error: File 'text.txt' wasn't found. Creating a new one...")

    lines = textwrap.wrap(text, 19)

    pages = []
    page = ""
    for line in range(len(lines)):
        lines_count = line % 14
        if lines_count == 0 and page:
            pages.append(page)
            page = ""
        page += lines[line] + " "
    if page:  # Чтобы последнюю страницу тоже вписало.
        pages.append(page)

    with open("book_text.txt", "w", encoding="utf-8") as write_to_book:
        write_to_book.write(template.replace("TEMPLATE_LIST", str(pages)))


if __name__ == "__main__":
    main()
