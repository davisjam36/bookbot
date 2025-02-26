#count number of words
def get_num_words(text):
    words = text.split()
    return len(words)

#count characters
def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#report function
def sort_on(d):
    return d["num"]

def char_dict_to_sorted_list(num_char_dict):
    sorted_list = []
    for ch in num_char_dict:
        sorted_list.append({"char": ch, "num": num_char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list