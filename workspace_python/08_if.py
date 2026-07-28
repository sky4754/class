a = 10
b = 5
print( 3 < a < 20 )

if True : 
    print(1)
# print(2) # IndentationError: unindent does not match any outer indentation level
    print(2)

    if True :
        print(4)

if True : # pass 쓰지 않으면 에러 뜸.
    pass
else :
    pass

if 1 :
    print('참')

'''
파이썬에서 False란?
False, None, 0, 0.0, 빈 컨테이너(비어있는 문자열, 리스트, 튜플)
'''

a = []
if a :
    print('참')
else :
    print('거짓')


# sroce = input('점수 4개 입력, 띄어쓰기로 구분 : ')
# print(sroce, sroce.split(' '))
# sroce = sroce.split(' ')
# sum = int(sroce[0]) + int(sroce[1]) + int(sroce[2]) + int(sroce[3])
# avg = sum / len(sroce)

# if (0 <= int(sroce[0]) <= 100) and (0 <= int(sroce[1]) <= 100) and (0 <= int(sroce[2]) <= 100) and (0 <= int(sroce[3]) <= 100) : 
# # if 0 >= sroce[0] and sroce[0] >= 100 :

#     if avg >= 80 :
#         print('합격')
#     else :
#         print('불합격')
# else : 
#     print('잘못된 입력')


button = int(input('메뉴:'))

if button == 1:
    print('코카콜라')
elif(button) == 2:
    print('칠성사이다')
elif(button) == 3:
    print('환타')
else :
    print('제공하지 않는 메뉴')



# 스위치 : break 필요없음.
# 또는(은) | (파이프)

a = '여름'
match a :
    case '봄' :
        print('봄')
    case '여름' :
        print('여름')
    case _ :
        print('그 외')














