c = int(input("알파벳을 옮길 횟수 -> "))
sen = input('암호화 시킬 문장 -> ')



plainList =[]
encryptedList = []
finalList = []

##PlainText Generator##
for p in range(1,27):
    pla = chr(p + 96)
    plainList.append(pla)

##암호화##
for n in range(1,27):
    if ((n + 96) + c) > 122:
        cae = (((n + 96) + c) - 122) + 96
        cae = chr(cae)
        encryptedList.append(cae)

        continue

    cae = chr((n + 96) + c)
    encryptedList.append(cae)

sen = list(sen)

for s in sen:
    if s == " ":
        finalList.append(s)
        continue
    elif s in "?!.,/:;\'\"@#$%^&*()_-+=~<>":
        finalList.append(s)
        continue

    finalList.append(encryptedList[(plainList.index(s))])

finalList = "".join(finalList)
print("암호화된 문장 -> " + finalList)
    
