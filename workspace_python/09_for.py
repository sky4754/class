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
    for b in range(4,-1,-1) :
            if 0 + a >= b :
                print('*', end='')
            else :
                print('-', end='')
    print()
print('--------------')

for a in range(5):
    for b in range( 5 - a - 1):
        print(' ', end='')

    for b in range(a * 2 + 1):
        print('*', end='')

    print()
print('--------------')

# for j in range(4,-1,-1) :
#     # print(j)
#     for i range(j) :
#         print('-', end='')

#     k = ((4-j)*2)


print('--------------')
# import turtle as t
# t.shape('turtle')
# # t.forward(100)
# # t.right(90)
# # t.left(45)

# while True :
#     print(1)

print('------------')


print('------------')

# c = int(input('피라미드 높이: '))

# for a in range(c):
#     for b in range( c - a - 1):
#         print(' ', end='')

#     for b in range(a * 2 + 1):
#         print('*', end='')

#     print()

print('------------')

for a in range(5):
    for b in range( 5 - a - 1):
        print('-', end='')

    for c in range(a * 2 + 1):
        print('*', end='')

    print()













