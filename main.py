from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters
from stats import sort_on
import sys

def main():
    if len(sys.argv) > 1:
        try:
            book_path = sys.argv[1]  
            text = get_book_text(book_path)
            words = get_num_words(text)
            words = [word.lower() for word in words]
            characters = get_num_characters(words)
            sorted = sort_on(characters)
            print(
                "============ BOOKBOT ============"
                "\nAnalyzing book found at books/frankenstein.txt..."
                "\n----------- Word Count ----------"
                f"\nFound {len(words)} total words"
                "\n--------- Character Count -------" \
                )
            for key in sorted:
                if key.isalpha() == True:
                    value = sorted[key]
                    print(f"{key}: {value}")
            print(
                "============= END ==============="
            )
        except Exception as e:
            print("Error path/ book not found")
            sys.exit(1)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
