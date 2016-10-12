
listA = [67, 45, 2, 13, 1, 998]
listB = [89, 23, 33, 45, 10, 12, 45, 45, 45]

def bubbleSort(list):
    n = len(list)
    for x in range(n-1, 0, -1):
        for i in range(x):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
 
bubbleSort(listA)
print(listA)
bubbleSort(listB)
print(listB)




'''I tried assigning variables to list[i] and list[i+1] to shorten code
and make it esier to read, but it doesn't work and I can't figure out why.
Can you tell me?

def bubbleSort(list):
    n = len(list)
    for x in range(n-1, 0, -1):
        for i in range(x):
            a = list[i]
            b = list[i+1]
            if a > b:
                a, b = b, a


'''
