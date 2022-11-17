
def count_word(sentence):

    sentence = sentence.lower()
    sentence = sentence.replace(' ', ',')
    sentence = sentence.replace('.', ',')
    print(sentence)
    sentence = sentence.split(',')

    print(sentence)

    num = dict()

    for word in sentence:
        if word in num:
            num[word] = num[word] + 1
        else:
            num[word] = 1

    return print(num)

count_word(str(input("Enter a Sentence")))


