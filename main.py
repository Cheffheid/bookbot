
def main():
    book_text = open_book('./books/frankenstein.txt')
    word_count = count_words(book_text)
    character_counts = count_characters(book_text)
    character_list = convert_to_alphabet_list(character_counts)
    character_list.sort(reverse=True,key=sort_by_count_callback)

    print_report('./books/franktenstein.txt', word_count, character_list )

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

def convert_to_alphabet_list(dict):
    characters = []

    for c in dict:

        if c.isalpha():
            characters.append({
                'name': c,
                'count': dict[c]
            })

    return characters

def sort_by_count_callback(dict):
    return dict['count']

def print_report(path, word_count, character_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")

    for character in character_list:
        print(f"The {character['name']} character was found {character['count']} times.")

    print('--- End report ---')

main()
