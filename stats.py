def get_num_words(text):
    words = text.split()
    wordcount = len(words)
    return wordcount
def get_num_char(text):
    num_char = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            num_char[char] = num_char.get(char, 0) + 1
    return num_char
def sort_on(char_dict):
    return char_dict["num"]
def generate_report(text):
    char_counts = get_num_char(text)
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(f"{item['char']}: {item['num']}")