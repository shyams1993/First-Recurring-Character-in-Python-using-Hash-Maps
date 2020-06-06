arr = [2,1,9,3,3,4,5,6]
def firstOccurrence(arr):
    d = {}
    for x in arr:
        if x in d:
            return x
            break
        d[x] = x
print(firstOccurrence(arr))