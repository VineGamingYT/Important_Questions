def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit) ** power for digit in num_str)

n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
