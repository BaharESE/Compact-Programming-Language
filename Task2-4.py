
def convert(str):

    lists = map(list,str)
    return list(lists)

strings = ["Hello", "How", "Are", "You"]
print(strings)

print(convert(strings))