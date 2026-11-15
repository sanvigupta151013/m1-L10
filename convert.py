n = int(input("Enter a decimal number: "))
binary = ""
print("Decimal number is:", n)
print("Decimal number is:", n)
while n > 0:
    binary = str(n % 2) + binary
    n = n // 2
print("the binary representation is:", binary)

