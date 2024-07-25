def single_root_words(root_word, *other_words):
    new_list = [i for i in other_words if root_word.lower() in i.lower() or i.lower() in root_word.lower()]
    return new_list

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
