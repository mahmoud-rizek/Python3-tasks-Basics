while True:
    sentance = input("Enter the sentance: ")

    def count_words(sentance):
        result = len(set(sentance.split(" ")))
        return result

    print(count_words(sentance))

    choice = input("let's count anthor sentance, type any key to countinue or type 'x' to exit ")
    if choice == 'x':
        break