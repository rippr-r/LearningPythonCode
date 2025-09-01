# X      Y | OUT
#----------------
# 0      0 | 0
# 0      1 | 1
# 1      0 | 1
# 1      1 | 0

def encrypt():
    plain = input("Enter plain text: ").lower()
    key = input("Enter key: ")
    cipher = ""

    for i in range(len(plain)):
        key_encrypt = key[i % len(key)] # Repeat key if shorter than plain text]
        cipher += hex(ord(plain[i]) ^ ord(key_encrypt))[2:] # XOR and convert to hex
    print(cipher)

encrypt()
