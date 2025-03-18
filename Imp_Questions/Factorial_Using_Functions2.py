#Using for loop without using recursion

n = int(input("Enter the parameter: "))

def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f * i
    return f

res = fact(n)
print("Factorial of",n,"is",res)