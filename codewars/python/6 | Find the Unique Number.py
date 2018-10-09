#There is an array with some numbers. All numbers are equal except for one. Try to find it!
#findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
#It’s guaranteed that array contains more than 3 numbers.
def find_uniq(arr):
    first = [];second = []
    for i in arr:
        if i == arr[0]: first.append(i)
        else: second.append(i)
    if len(first) > len(second): return second[0]
    else: return first[0]
