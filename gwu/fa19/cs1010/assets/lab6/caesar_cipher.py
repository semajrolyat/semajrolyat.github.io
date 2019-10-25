# Sample of casear cipher, changing the letters of a string to the next letter
# Date: Sep. 30th, 2019; Author: https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python

def casear(a, key):

    str = ""
    if key > 26:
        key %= 26
    for i in range(0, len(a)):
        if a[i].isalpha():
            b = ord(a[i])
            b += key
            print(a[i])
            print(b)
            if b == 91:
                str += chr(65)
            elif b > 122:
                c = b - 122
                str += chr(96 + c)
            else:
                str += chr(b)
        else:
            str += a[i]
    print(str)


a = 'A SAMPLE TEXT Z'
# Change key as you wish
key = 1
casear(a, key)
print()
