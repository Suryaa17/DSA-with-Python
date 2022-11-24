# Problem statement

""""
Check Number in Array
Send Feedback
Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.
Input Format :
Line 1 : An Integer N i.e. size of array
Line 2 : N integers which are elements of the array, separated by spaces
Line 3 : Integer x
Output Format :
'true' or 'false'
Constraints :
1 <= N <= 10^3
Sample Input 1 :
3
9 8 10
8
Sample Output 1 :
true
Sample Input 2 :
3
9 8 10
2
Sample Output 2 :
false

"""
#######  NOT RECURSIVE METHOD  #############

list1 = []
n = int(input("Enter the number of elements in the list : "))
for i in range(1,n+1):
    values = int(input("Enter the values : "))
    list1.append(values)
print("The list is : ",list1)
given_number = int(input("Enter the number you want to check it is available or not : "))
flag = False
for i in range(n):
    if list1[i] == given_number:
        flag = True
if flag:
    print(True)
else:
    print(False)