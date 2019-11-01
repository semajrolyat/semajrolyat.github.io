'''
Simple caesar cipher
'''
def caesar(text, key):
    msg = ""
    text = text.upper()
    sign = 1
    if key < 0:
        sign = -1
        key *= sign;
    if key > 26:
        key %= 26
        
    for i in range(0, len(text)):
        if text[i].isalpha():
            x = ord(text[i]) - ord("A")
            x = (x + sign * key) % 26
            msg += chr(x + ord("A"))
        else:
            msg += text[i]
    return msg


plaintxt = 'A SAMPLE TEXT Z'
# Change key as you wish
key = 10
ciphertxt = caesar(plaintxt, key)
key *= -1
msg = caesar(ciphertxt, key)

print(plaintxt)
print(ciphertxt)
print(msg)
