sentance = input("Enter the sentance: ")
def count_words(sentance):
    words_list =sentance.split(" ")    
    result = len(dict.fromkeys(words_list))

    return result


print(count_words(sentance))

