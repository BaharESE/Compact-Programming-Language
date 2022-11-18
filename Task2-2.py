
def sort_list(tuples):

    for i in range(number):
        for j in range(number-i-1):
            if tuples[j][-1] > tuples[j+1][-1]:
                temp = tuples[j]
                tuples[j] = tuples[j+1]
                tuples[j+1] = temp

    return tuples

list = []
number = int(input("How many tuples are in your list?"))

for i in range(number):
    a = input("Enter a Tuple")
    list.append(a)

print(list)
print("Sorted by last digit:", sort_list(list))