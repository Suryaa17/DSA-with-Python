
# Sum of N natural numbers using recursion
def sum1(n):
    if n == 0:
        return 0

    return n+sum1(n-1)

num = int(input("Enter a number : "))
sum_of_numbers = sum1(num)
print(sum_of_numbers)