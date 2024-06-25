
def main():
    book_text = open_book('./books/frankenstein.txt')
    word_count = count_words(book_text)

    print(book_text)
    print(word_count)

def open_book(path):
    with open(path) as book:
        return book.read()

def count_words(text):
    words = text.split()
    return len(words)

main()
