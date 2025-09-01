# X      Y | OUT
#----------------
# 0      0 | 0
# 0      1 | 1
# 1      0 | 1
# 1      1 | 0

def decrypt():
    cipher = input("Enter HEX cipher text: ")
    key = input("Enter key: ")
    plain = ""

    for i in range(0, len(cipher), 2):
        byte = cipher[i:i+2]
        key_decrypt = key[(i//2) % len(key)] # Repeat key if shorter than cipher text
        plain += chr(int(byte, 16) ^ ord(key_decrypt)) # Convert hex to int, XOR and convert to char
    print(plain)


decrypt()
