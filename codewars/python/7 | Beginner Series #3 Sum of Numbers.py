#Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
def get_sum(a,b):
    if b > a:
        counter = b
        nc = a
    else:
        counter = a
        nc = b
    total = counter
    while counter != nc:
        counter -= 1
        total += counter
    return total
