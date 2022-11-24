# Setting Recursion limit in python using sys library

from sys import setrecursionlimit 
setrecursionlimit(10000)

def fact(n):
    if n == 1:
        return 1
    smalloutput = fact(n-1)
    output = n*smalloutput
    return output

n = int(input("Enter a number to find factorial : "))
print(fact(n))