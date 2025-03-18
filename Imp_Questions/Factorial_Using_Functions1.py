#Using While loop without using recursion

n = int(input("Enter the parameter: "))

def fact(a):
    f = 1
    i = 1
    while i <= a:
        f = f * i
        i += 1
    return f

res = fact(n)
print("Factorial of",n,"is",res)