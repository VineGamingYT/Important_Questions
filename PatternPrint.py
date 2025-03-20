#Outer loop --> Rows
#Inner Loop --> Column

"""
* * * *
* * * *
* * * *
* * * *
"""

n = int(input("Enter no.: "))

for i in range(n):
    for j in range(n):
        print("*", end = " ")
    print()

"""
*
* *
* * *
* * * *
"""

n = int(input("Enter no: "))

for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()

"""
* * * *
* * *
* *
*
"""

n = int(input("Enter no.: "))

for i in range(n):
    for j in range(n-i):
        print("*", end = ' ')
    print()

"""
      *
    * *
  * * *
* * * *
"""

n = int(input("Enter no.: "))

for i in range(n):
    for j in range(n-1-i):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end = " ")
    print()


"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

n = int(input("Enter max. no. stars in the middle: "))

for i in range(n):
    for j in range(i+1):
        print("*", end = " ")
    print()

for i in range(n-1):
    for j in range(n-1-i):
        print("*", end = " ")
    print()


"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

n = int(input("Enter no.: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end = " ")
    print()

"""
A 
A B 
A B C 
A B C D 
"""

n = int(input("Enter no.: "))

for i in range(n):
    char = 65
    for j in range(i+1):
        print(chr(char), end = " ")
        char += 1
    print()

"""
A 
B C 
D E F 
G H I J 
K L M N O 
"""

n = int(input("Enter no.: "))

char = 65
for i in range(n):
    for j in range(i+1):
        print(chr(char), end = " ")
        char += 1
    print()


"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""

n = int(input("Enter no.: "))

num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end = ' ')
        num += 1
    print()

"""
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
"""

n = int(input("Enter no.: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end = " ")
    for j in range((2*i)+1):
        print("*", end = " ")
    print()

"""
        A 
      A B C 
    A B C D E 
  A B C D E F G 
A B C D E F G H I
"""

n = int(input("Enter no.: "))

for i in range(n):
    char = 65
    for j in range(n-i-1):
        print(" ", end = " ")
    for j in range((2*i)+1):
        print(chr(char), end = " ")
        char += 1
    print()