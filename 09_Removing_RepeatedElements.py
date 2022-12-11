# remove repeated elements from a l1
def elementl1():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l1)
    print("Removing repeated elements from the l1")
    l1 = set(l1)
    print(l1)
    
elementl1()