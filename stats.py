def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    result = {}
    for char in text:
        lowered_char = char.lower()
        if not lowered_char in result:
            result[lowered_char] = 1
        else:
            result[lowered_char] += 1
        
    return result

def get_sorted_chars(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append(
            {
                "char": key,
                "num": char_dict[key]
            }
        )
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list