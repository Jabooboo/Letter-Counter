result = 0
for c in input('Enter Phrase\n').upper():
    if c.isalpha():
        result = result + ord(c) - 64
print(result)