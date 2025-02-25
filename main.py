def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
def num_words(texts):
    words = texts.split()
    wordcount = len(words)
    return wordcount
def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    total_words = num_words(text)
    print (f"{total_words} words found in the document")
    #print(text)



main()