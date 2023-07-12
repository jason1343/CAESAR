d = int(input("알파벳을 옮길 거리 -> "))
sen = input('복호화 시킬 문장 -> ')



plainList =[]
encryptedList = []
finalList = []

##PlainText Generator##
for p in range(1,27):
    pla = chr(p + 96)
    plainList.append(pla)

##암호화##
for i in range(1,27):
    if ((i + 96) + d) > 122:
        cae = (((i + 96) + d) - 122) + 96
        cae = chr(cae)
        encryptedList.append(cae)

        continue

    cae = chr((i + 96) + d)
    encryptedList.append(cae)

sen = list(sen)

for s in sen:
    if s == " ":
        finalList.append(s)
        continue
    elif s in "?!.,/:;\'\"@#$%^&*()_-+=~<>":
        finalList.append(s)
        continue

    finalList.append(plainList[(encryptedList.index(s))])

finalList = "".join(finalList)
print(finalList)
    
