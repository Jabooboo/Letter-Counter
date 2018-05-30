name = 'bryan'
alphabet = {'a' : 1,
            'b' : 2,
            'c' : 3,
            'd' : 4,
            'e' : 5,
            'f' : 6,
            'g' : 7,
            'h' : 8,
            'i' : 9,
            'j' : 10,
            'k' : 11,
            'l' : 12,
            'm' : 13,
            'n' : 14,
            'o' : 15,
            'p' : 16,
            'q' : 17,
            'r' : 18,
            's' : 19,
            't' : 20,
            'u' : 21,
            'v' : 22,
            'w' : 23,
            'x' : 24,
            'y' : 25,
            'z' : 26,}
name_split = list(name)
print(name_split)
name_length = (len(name_split))
print(name_length, "\n")

for i in range(name_length):
    result = alphabet[name_split[i]]
    print(result)

'''Now I have no clue how to add the results of the loop into one whole number on one line.
from
2
18
25
1
14

to

60
'''