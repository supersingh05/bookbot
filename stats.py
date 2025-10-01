
def count_words(book_string):
    word_list = book_string.split()
    return len(word_list)


def character_count(book_string):
    words = {}
    for c in book_string:
        if c.isalpha():
            add_to_map(words, c.lower())
        elif c.isdigit() or not c.isspace():
            add_to_map(words, c)
    return words


def add_to_map(words, c):
    if c in words:
        words[c] += 1
    else:
        words[c] = 1


def sort_on(items):
    return items["num"]


def sorted_word_count(words):
    wc = []
    for key, value in words.items():
        j = {"char": key, "num": value}
        wc.append(j)
    wc.sort(reverse=True, key=sort_on)
    return wc
