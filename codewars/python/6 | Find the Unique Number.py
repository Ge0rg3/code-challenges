#There is an array with some numbers. All numbers are equal except for one. Try to find it!
#findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
#It’s guaranteed that array contains more than 3 numbers.
def find_uniq(arr):
    arr.sort()
    return arr[0] if arr.count(arr[0]) == 1 else arr[-1]
    
