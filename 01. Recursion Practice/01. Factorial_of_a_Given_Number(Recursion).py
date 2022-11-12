
# Finding the factorial of a number using recursion
def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

num = int(input("Enter a number to find the factorial : "))
fact1 = fact(num)
print(fact1)