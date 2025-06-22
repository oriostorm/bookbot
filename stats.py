def get_book_text(text_filepath):
    with open(text_filepath) as f:
    # do something with f (the file) here
        file_contents = f.read()
        return file_contents
    
def word_counter(text):
    list_of_words = text.split()
    return len(list_of_words)

def character_counter(text):
    lowercase_text = text.lower()
    character_list = list(lowercase_text)

    char_counter_dict = {}

    for char in character_list:
        if char in char_counter_dict:
                char_counter_dict[char] += 1
        else:
             char_counter_dict[char] = 1

    return char_counter_dict


def sort_on(items):
    return items["num"]

def sort_list_of_chars (dict):
     char_list = []
     #print(dict)
     #char_list = [{"char": ch, "num": count} for ch, count in dict.items()]
     for ch, count in dict.items():
          if ch.isalpha():
            char_list.append({"char": ch, "num": count})
     char_list.sort(reverse=True, key=sort_on)
     return char_list

def print_pretty_book_stats(file_to_analyze):
    book_text = get_book_text(file_to_analyze)
    num_words = word_counter(book_text)

    character_dict = character_counter(book_text)

    sorted_list_of_chars = sort_list_of_chars(character_dict)

    print("=======BOOKBOT=======")
    print(f"Analyzing book found at {file_to_analyze}...")
    print("------ WORD COUNT ------")
    print(f"Found {num_words} total words")

    print("------- CHARACTER COUNT------")

    for char_stat in sorted_list_of_chars:
        char = char_stat["char"]
        count = char_stat["num"]
        print(f"{char}: {count}")

