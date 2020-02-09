def count_th(word):

    if word.find('th') == -1 or len(word) == 0:
        return 0
    else:
       occurrence = word.find('th')
       new_word = word[occurrence + 2:]
       return 1 + count_th(new_word)     
