from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_num_words(text)
    words = [word.lower() for word in words]
    characters = get_num_characters(words)
    print(f"{len(words)} words found in the document")
    print(characters)

main()
