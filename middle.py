num = int(input("Enter a number: "))
t = num
print("the number is:", t)
numlen = 0
while t > 0:
    numlen += 1
    t = int(t / 10)
    print(t)
if numlen >= 4:
    print("you can continue")
else:
    print("it is not 4 digit number or it is a more digit number")

if num >= 4:
    numlen = int(numlen/2)
    print("the length of the number is:", numlen)
    chk = 0
    while num > 0:
        rem = num % 10
        if chk == numlen:
            print("the remainder is:", rem)
            midOne = rem
        elif chk == numlen - 1:
            print("the midTwo is:", rem)
            midTwo = rem

        num = int(num / 10)
        chk += 1
    print("chk is:", chk)
    print("the middle two digits are:", midOne, midTwo)

    product = midOne * midTwo
    print("the product of the middle two digits is:", product)

