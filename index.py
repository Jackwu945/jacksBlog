# ©2021 梯子科技工作室制作
#高一五班 吴宇杰
def caesar_encode_classical(word):
    secret=''
    for c in word:
        if 'a'<= c <='w' or 'A'<= c <='W':
            secret+=(chr(ord(c)+3))
        elif 'x'<= c <='z' or 'X'<= c <='Z':
            secret+=(chr(ord(c)-23))
        elif c == ' ':
            secret+=c
    return secret

def caesar_encode_plus(word,move):
    secret=''
    for c in word:
        if 65<= ord(c) <=90 :#小写
            i=ord(c)+move
            while i > 90:
                i-=26
            secret+=chr(i)
        elif 97<= ord(c) <=122:
            i=ord(c)+move
            while i >122:
                i-=26
            secret+=chr(i)
        elif c == ' ':
            secret+=c
    return secret

def mkkey():
    import random
    key={}
    upkey=[]
    lowkey = []
    low=[]
    for i in range(65,91):
        upkey.append(chr(i))
    for j in range(97,123):
        lowkey.append(chr(j))

    up=random.sample(upkey,26)
    for u in up:
        low.append(u.lower())

    Upperkey=dict(zip(upkey,up))
    Lowerkey = dict(zip(lowkey, low))
    return [Upperkey,Lowerkey]


def caesar_encode_proplus(word,dic):
    secret=''
    for w in word:
        if 65<= ord(w) <=90:
            secret+=dic[0][w]
        elif 97<= ord(w) <=122:
            secret+=dic[1][w]
        elif w == ' ':
            secret+=w
    return secret


# #使用例1
# print(caesar_encode_classical('I love you China!'))
# #使用例2
# print(caesar_encode_plus('I love you China!',1024))
#使用例3
key=mkkey()
print(key)
print(caesar_encode_proplus('I love you China!',key))

