
def main():
    book_text = open_book('./books/frankenstein.txt')
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)

    print(book_text)
    print(word_count)
    print(character_counts)

def open_book(path):
    with open(path) as book:
        return book.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowercase_text = text.lower()
    character_counts = {}

    for c in lowercase_text:
        character_counts[c] = character_counts.setdefault(c, 0) + 1

    return character_counts

main()
