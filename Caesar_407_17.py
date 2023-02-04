def caesar(plaintext,a,b):
    Txt = ""
    pos = -1
    for i in plaintext:
        pos += 1
        val = 0 
        if i.isalpha():
            if i.isupper():
                if pos%2 == 0:
                    val = ord(i)+a
                else:
                    val = ord(i)+b
                if val > 90:
                    val -= 26
            if i.islower():
                if pos%2 == 0:
                    val = ord(i)+a
                else:
                    val = ord(i)+b
                if val > 122:
                    val -= 26
        Txt += chr(val)
    return Txt

print(caesar("BCDE",-1,-1))
            
            
