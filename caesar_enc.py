alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Uencal = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Ualpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
plainText = input('암호화 시킬 문장을 입력하세요 --> ')
inp = input('알파벳을 옮길 자리수를 입력하세요 --> ')
temp = 0
Utemp = 0
c = 0

#알파벳 순서 옮기기
while c < int(inp):
    for i in range(26):    
        if i == 0:
            temp = encal[0]     
            encal[0] = encal[25]
            
            Utemp = Uencal[0]
            Uencal[0] = Uencal[25]     
    
        elif i == 1:
            encal[1] = temp
            Uencal[1] = Utemp
    
        else : 
            encal[i] = alpha[i-1]
            Uencal[i] = Ualpha[i-1]

    for i in range(len(encal)):
        alpha[i] = encal[i]
        Ualpha[i] = Uencal[i]
    
    c += 1

key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Ukey = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# 알파벳을 2번 옮겼을 때,

# ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']

# hansei = fylqcg


#암호화 하기
try:
    n = 0
    LpT = list(plainText)

    for j in plainText:
        if j == " ":
            n += 1
            continue
    
        if j.isupper():
            LpT[n] = Uencal[Ukey.index(j)]
            n += 1
            continue

        if j == ',' or j == '.' or j == '?' or j == '!':
            LpT[n] == j
            n += 1
            continue


    
        LpT[n] = encal[key.index(j)]

        n += 1

    encT = ''.join(LpT)
    print(encT)
except:
    print(", . ! ? 를 제외한 특수문자는 사용이 불가합니다.")
input("아무키를 눌러서 종료...")
    








