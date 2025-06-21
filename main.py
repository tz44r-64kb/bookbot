import sys
from stats import get_word_count, get_char_dict, get_sorted_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_contents = get_book_text(path)
    word_count = get_word_count(book_contents)
    char_dict = get_char_dict(book_contents)
    sorted_chars = get_sorted_chars(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()