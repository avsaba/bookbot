def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    print(num_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    return text


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counter = {}
    for char in text:
        char = char.lower()
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    return counter


main()
