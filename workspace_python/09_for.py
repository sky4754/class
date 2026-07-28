for i in range(5) :
    print(i)

for i in range(5) :
    print(i, end=' ')
print()

for i in reversed(range(5)) :
    print(i, end=' ')

print()
# 구구단
for a in range(2, 10) :
    for b in range(1, 10) :
        print(f" {a} x {b} = { a * b }" )

print("----------------")

import random
print(random.random())
print(random.randint(1,6))

# 주사위 3이 몇번만에 나오는지 출력
dice = -1
count = 0
while dice != 3 :
    dice = random.randint(1, 6)
    count += 1
    if dice == 3 :
        print(count)

print('------------')
'''
ㅁ
ㅁㅁ
ㅁㅁㅁ
ㅁㅁㅁㅁ
ㅁㅁㅁㅁㅁ
'''
for a in range(5) :
    for b in range(5) :
        if b <= a:
            print('ㅁ', end='')
    print()
print('--------------')
'''
ㅁㅁㅁㅁㅁ
ㅁㅁㅁㅁ
ㅁㅁㅁ
ㅁㅁ
ㅁ
'''
for a in range(5) :
    for b in range(5) :
        if b >= a:
            print('ㅁ', end='')
    print()
print('--------------')
for a in range(5) :
    for b in range(1,5,-1) :
            if a >= b >= 5 :
                print('*', end='')
            else :
                print('-', end='')
    print()
print('--------------')