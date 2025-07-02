import random as rand


listtoSort = []

for i in range (50):
    listtoSort.append(rand.randint(0, 100))

print (f"Original: {listtoSort}")
running = True
largestNumber = listtoSort[0]
smallestNumber = listtoSort[0]

while running :
    sorted = True
    for i in range(len(listtoSort)-1):

        if (listtoSort[i] > listtoSort[i+1] ):
            listtoSort[i+1], listtoSort[i] = listtoSort[i], listtoSort[i+1]
            # print(f"swapping! {listtoSort}")
        if (listtoSort[i+1] > largestNumber):
            largestNumber = listtoSort[i+1]
        if (listtoSort[i] < smallestNumber ):
            smallestNumber = listtoSort[i]

    for i in range(len(listtoSort) - 1):
        if (listtoSort[i+1] < listtoSort[i] and sorted):
            sorted = False



    if (listtoSort[0] == smallestNumber and listtoSort[-1] == largestNumber and sorted):
        running = False

print (listtoSort)