import sys
from stats import get_num_words
from stats import generate_report

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    
    text = get_book_text(sys.argv[1])
    total_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print (f"Found {total_words} total words")
    print("--------- Character Count -------")
    generate_report(text)

main()