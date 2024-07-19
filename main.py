def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    print_report(book_path, num_words, num_chars)


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


def sort_chars(chars):
    result = []
    for char in chars:
        if char.isalpha():
            result.append({"char": char, "num": chars[char]})
    result.sort(reverse=True, key=lambda x: x["num"])
    return result


def print_report(path, num_words, num_chars):
    chars = sort_chars(num_chars)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} found in the document")
    print()
    for char in chars:
        print(f"The '{char['char']} character was found {char['num']} times")
    print("--- End report ---")


main()
