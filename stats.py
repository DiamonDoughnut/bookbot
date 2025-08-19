def get_num_words (str):
    return len(str.split())

def get_num_chars (str):
    char_dict = {}
    for char in str:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1 
    return char_dict     

def sort_on (items):
    return items["count"]

def num_chars_report (chars):
    char_list = []
    for char in chars:
        if char.isalpha():
            char_list.append({"char": char, "count": chars[char]})
    char_list.sort(reverse=True, key=sort_on) 
    return char_list         