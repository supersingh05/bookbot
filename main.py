from stats import count_words, character_count, sorted_word_count
import sys


def get_book_text(file_path):
    print(f"Analyzing book found at {file_path}")
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    contents = get_book_text(sys.argv[1])
    wc = character_count(contents)
    count_list = sorted_word_count(wc)
    print(f"Found {count_words(contents)} total words")
    print("--------- Character Count -------")
    for c in count_list:
        if c["char"].isalpha():
            k = c["char"]
            v = c["num"]
            print(f"{k}: {v}")
    print("============= END ===============")


main()
