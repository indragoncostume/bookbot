def get_book_text(book):
    with open(book) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return words

def get_num_characters(words):
    characters = {}
    letters = []
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter not in characters:
                characters[letter] = 0
            characters[letter] += 1
    return characters

def sort_on(characters):
    sortedbykey = {k: v for k, v in sorted(characters.items(), key= lambda v: v[1], reverse=True)}
    return sortedbykey
