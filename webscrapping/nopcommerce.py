#reverce a string
s="hello"
print(s[::-1])

#remove duplicates from list
nk=[1,2,3,4,4,5,5,2,3,1]
mnk=list(set(nk))
print(mnk)

#check string is a palindrome
s="madam"
palindrome=s==s[::-1]
print(palindrome)

#max number in a list
list=[1,3,25,75,2]
print(max(list))

#Count the Occurrences of Each Element in a List
lst=[1,1,2,3,4,5,2,4,5,3,3,3,5,1,]
count={i:lst.count(i) for i in set(lst)}
print(count)

#merge two list and remove duplicates
list1=[1,2,3,4,56,7]
list2=[1,2,3,4]
merged_list=(set(list1+list2))
print(merged_list)

#factorial of a number
n=5
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)

#check prime number
n=7
if n>1:
    for i in range(2, int(n/2) + 1):
        if (n% i)==0:
            print(f"{n}is not a prime")
            break
    else:
            print(f"{n}is prime")
else:
        print(f"{n}is not a prime num")
#fibonacci series
n = 10
fib_sequence = [0, 1]
for i in range(2, n):
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
print(fib_sequence)


#armstrong number
num = 153
power = len(str(num))
sum_digits = sum(int(digit) ** power for digit in str(num))
is_armstrong = num == sum_digits
print(is_armstrong)

#sum of digits
num = 1234
digit_sum = sum(int(digit) for digit in str(num))
print(digit_sum)

#swap two numbers
a = 5
b = 10
# Swapping the values
a, b = b, a
# Print the swapped values
print("a =", a)
print("b =", b)

#matrix multiplication

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
# Initialize the result matrix with zeros
result = [
    [0, 0],
    [0, 0]
]
# Perform matrix multiplication
for i in range(len(A)):  # Iterate over rows of A
    for j in range(len(B[0])):  # Iterate over columns of B
        for k in range(len(B)):  # Iterate over rows of B
            result[i][j] += A[i][k] * B[k][j]

# Print the resulting matrix
for row in result:
    print(row)










