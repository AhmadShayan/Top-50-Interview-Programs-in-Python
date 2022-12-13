def sub(l1, l2):
    for i in l2:
        if i in l1:
            l1.remove(i)
    return l1


def giveRepeatedNumbers():
    l1 = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
    print(l1)
    l2 = set(list(l1))
    return sub(l1, l2)

print (giveRepeatedNumbers())
