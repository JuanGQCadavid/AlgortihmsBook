
def insertion(arrayList):
    for j in range(1, len(arrayList)):
        key = arrayList[j]
        i = j-1

        while (i >= 0 and key < arrayList[i]):
            arrayList[i + 1] = arrayList[i]
            i = i - 1

        arrayList[i + 1] = key

    return arrayList

print insertion([5,2,4,6,1,3])



