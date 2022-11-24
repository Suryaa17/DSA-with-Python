
# Problem Statement 

"""
Sum Of Array
Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Output Format :
Sum
Constraints :
1 <= N <= 10^3
Sample Input 1 :
3
9 8 9
Sample Output 1 :
26
Sample Input 2 :
3
4 2 1
Sample Output 2 :
7    
"""

# Solution

a = []
length_array = int(input("Enter the number of elements to be in the array : "))
for i in range(length_array):
    abc = int(input("Enter the number : "))
    a.append(abc)
print("The array is : ",a)
size = len(a)

def Sum_Array(a,size):
    if size == 0:
        return 0
    sum_of_array = a[size-1] + Sum_Array(a,size-1)
    return sum_of_array

print(Sum_Array(a,size))


