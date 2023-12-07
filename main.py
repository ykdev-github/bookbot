def main():
    book_path = "books/frankenstein.txt"
    file_contents = open_file(book_path)

    count = count_word(file_contents)
    letters = count_letters(file_contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    sorted_list = []
    for k,v in letters.items():
        sorted_list.append({"char": k, "num": v})
    sorted_list.sort(reverse=True, key=sort_on)

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]


def count_word(content):
    words = content.split()
    return len(words)

def count_letters(content):
    dict = {}
    for i in range(0, len(content)):
        if content[i].lower() in dict:
            dict[content[i].lower()] += 1
        else:
            dict[content[i].lower()] = 1
    return dict

def open_file(path):
    with open("./books/frankenstein.txt") as f:
        return f.read()
        

main()