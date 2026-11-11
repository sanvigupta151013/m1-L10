string = input("enter a word here: ")
char = input("enter a character here: ")

i = 0
count = 0

while i<len(string):
    if string[i] == char:
        count += 1

    i += 1

print("the number of character this word has:",count)
