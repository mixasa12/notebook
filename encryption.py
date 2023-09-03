def cipher(s,PK):
    ss = ""    
    for i in range(len(s)):
        char = s[i]
        byte = ord(char)
        byte = byte ^ PK
        char2 = chr(byte)
        ss += char2
    return ss
