def reverse_number(n):
    return int(str(n)[::-1])

n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))
