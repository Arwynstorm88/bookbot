from stats import get_num_words
#from stats import get_num_char
from stats import generate_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    total_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print (f"Found {total_words} total words")
    print("--------- Character Count -------")
    generate_report(text)

main()