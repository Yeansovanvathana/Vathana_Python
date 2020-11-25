def dict_count(word_list):
    word_dict = {}
    for words in word_list:
        word_dict[str(words)] = word_list.count(words)
    return word_dict
print(dict_count("vathana"))