alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Uencal = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Ualpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

cipherText = input('복호화시킬 문장을 입력하세요 --> ')
inp = input('알파벳을 옮길 자리수를 입력하세요 --> ')
temp = 0
Utemp = 0
c = 0

#알파벳 순서 옮기기

while c < int(inp):
    for i in range(26):    
        if i == 0:
            temp = encal[0]  #소문자    
            encal[0] = encal[25]

            Utemp = Uencal[0]  #대문자
            Uencal[0] = Uencal[25]     
    
        elif i == 1:
            encal[1] = temp  #소문자
            Uencal[1] = Utemp  #대문자
    
        else : 
            encal[i] = alpha[i-1]  #소문자
            Uencal[i] = Ualpha[i-1]  #대문자
        

    for i in range(len(encal)):
        alpha[i] = encal[i]  #소문자
        Ualpha[i] = Uencal[i]  #대문자

    c += 1

key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Ukey = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 예) 알파벳을 2번 옮겼을 때,
# key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# encal = ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']

# Ukey = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# Uencal = ['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X']

# hansei = fylqcg


#복호화 하기
try:
    n = 0
    LcT = list(cipherText) #Fg kw lykc gq Kglhsl

    for j in cipherText:
        if j == " ":
            n += 1
            continue

        if j.isupper():
            LcT[n] = Ukey[Uencal.index(j)]
            n += 1
            continue

        if j == ',' or j == '.' or j == '?' or j == '!':
            LcT[n] == j
            n += 1
            continue


        LcT[n] = key[encal.index(j)]

        n += 1

    decT = ''.join(LcT)
    print(decT)
except:
    print(", . ! ? 를 제외한 특수문자는 사용이 불가합니다.")
input( "아무키를 눌러서 종료...")