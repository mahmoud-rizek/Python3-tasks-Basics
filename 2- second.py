sentance = input("Enter the sentance: ")

def count_words(sentance):
    result = len(sentance.split(" ") )

    return result

print(count_words(sentance))

