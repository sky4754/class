# w : 수정 가능
file = open('hello.txt', 'w')
file.write('eng\n123\n한글')
file.flush() # 버퍼가 꽉 차지 않아도 내보내기
             # 즉시 반영 
file.close()

# 한글 캐릭터 셋
# utf-8, euc-kr, cp949
file = open('hello2.txt', 'w', encoding='utf-8')
file.write('eng\n123\n한글')
file.close()

# r : 읽기 전용
file = open('hello.txt', 'r')
s = file.read()
file.close()
print(s)

file = open('hello2.txt', 'r', encoding='utf-8')
s = file.read()
file.close()
print(s)

print('-------')
file = open('hello.txt', 'r')
s = file.read(10)
file.close()
print(s)

print('-------')
file = open('hello.txt', 'r', buffering=1)
s = file.read()
file.close()
print(s)

print('-------')
file = open('hello.txt', 'r')
while True :
    chunk = file.read(2)
    if not chunk :
        break
    print(chunk)
file.close()

print('-------')
file = open('a.webp', 'rb')
s = file.read()
file.close()
print(s)

with open('hello.txt', 'r') as file :
    s = file.read()
    print(s)

a = [1,2,3,4]
with open('array1.txt', 'w') as file : 
    # file.write(str(file))
    file.write(str(a))
print(str(a))

with open('array1.txt', 'r') as file : 
    b = file.read()
    print( type(b), b )
    c = list(b)
    print( type(c), c )

print('------------')

import pickle

name = 'eng한'
age = 20
adress = 'a가'
arr = [1,2,3,4,5]
score = {
    '직업': '학생',
    '음식': '무침'
}

with open ('pickle.p', 'wb') as f :
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(adress, f)
    pickle.dump(arr, f)
    pickle.dump(score, f)

with open ('pickle.p', 'rb') as f :
    # dump 순서대로 꺼낸다.
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    print(p2['음식'])

    # dump한 만크만 꺼낼 수 있다.
    # p2 = pickle.load(f) # EOFError: Ran out of input
    # print(p2, type(p2)) # EOF = End Of File

# pickle 보다 대용량에 특화된 라이브러리
# import joblib

# a 이어 쓰기
with open('hello.txt', 'a') as f :
    f.write('123')
    # f.read()

# + 
# 쓰기 계열에 붙어있으면 읽기 가능해짐
# 읽기 계열에 붙어있으면 쓰기 가능해짐

# 문제1. 단어 중 대소문자 구분없이 c를 포함하는 단어를 출력하시오. 단 , . 은 출력하지 마시오

# 1. word.txt를 읽고 쓰기 전용으로 바꾸고 터미널에 출력한다.
# 2. split 써서 리스트 만든다. 
print('----------')
with open('word.txt', 'r') as file :
    text = file.read()
    # print(text)
    a = text.split()
    # print(a)
    # for i in a :
    #     # print(i)
    #     b = i.split('c')
    #     if len(b) > 1 :
    #         c = i.split('.')
    #         d = ''.join(c)
    #         e = i.split(',')
    #         f = ''.join(e)
    #         print(f)
    for i in a :
         # print(i)
        if i.find('c') != -1 :
            b = i.replace(',','') 
            c = b.replace('.','')
            print(c)




    
  



