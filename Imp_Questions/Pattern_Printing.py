'''

This function prints the following pattern:

*
**
***
****

'''

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

'''

This function prints the following pattern:

****
***
**
*

'''

n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


'''

This function prints the following pattern:

   *
  **
 ***
**** 

'''

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

'''

This function prints the following pattern:

****
 ***
  **
   *

'''

n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


'''

This function prints the following pattern:

      *
     ***
    *****

'''

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

