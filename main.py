print("--- Begin report of books/Frankenstein.txt ---\n")

def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def word_count(r): 
    r = file_contents.split(' ')
    num_words = len(r)
    print(f"There are {num_words} words in this document\n\n")
    return num_words

def char_count(r):
    chars = file_contents.lower()
    char_count = {}
    for i in chars:
        if i.isalpha():
            if i not in char_count:
                char_count[i] = 1
            else:
                char_count[i] += 1   
    return char_count

def sort_on(dict):
    return dict["amount"]

def print_sorted_character_count(r):
    list_of_characters = []
    for character, amount in r.items():
        new_dict = {"character": character, "amount": amount}
        list_of_characters.append(new_dict)
    list_of_characters.sort(reverse = True, key=sort_on)
    for item in list_of_characters:
        print(f"The letter {item['character']} appears {item['amount']} times.")

file_contents = main()
word_count(file_contents)
characters = char_count(file_contents)
print_sorted_character_count(characters)


"""---Solution:---

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

"""