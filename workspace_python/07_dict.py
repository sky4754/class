# 딕셔너리 선언
a = {}
a = dict()
print( type(a) )

b = {
    '이름': 'Halbae',
    '직업': '방패병',
    '스킬': {
        '공격': '방패로 쳐패기',
        '방어': '방패 들고 방어하기',
        'javascript': '중'
    }
}
print(b)

print('-'*30)
c = dict(a=10, b=20)
print(c)
print('-'*30)
print(b['이름'])
# print(b['이름2']) # KeyError: '이름2'

print( b.get('이름') )
print( b.get('이름2') ) # 없으면 None
print( b.get('이름2', '이름없음') ) # 없으면 두 번째 값으로 대체

print( b['스킬']['공격'])
print( b.get('스킬').get('공격') )
print( b.get('스킬2', {}).get('공격', 0) )

b['직업'] = '도적'
print(b)

b['직업2'] = '도적2' # 없으면 key 만들어 줌.
print(b)

print( '스킬' in b )
print( '공격' in b )
print( '공격' in b['스킬'] )
print( '공격' not in b['스킬'] )

print( len(b) ) # key의 개수

e = b.keys()
print( e )
f = b.values()
print( f )
# print( f[0] ) # TypeError: 'dict_values' object is not subscriptable
print( list(f)[0] )

g = b.items()
print( g )


# set
#   중복을 허용안함. 제거해서 관리한다.
#   순서는 보장하지 않는다.
a = 'hello'
print( list(a) )
print( set(a) ) # {'l', 'o', 'h', 'e'}


b = {
    '이름': 'Halbae',
    '직업': '방패병',
    '스킬': {
        '공격': '방패로 쳐패기',
        '방어': '방패 들고 방어하기',
        'javascript': '중'
    }
}

b.update(이름='타이거', 직업='강사')
b.update(이름='타이거', 직업='강사', 나이=20)
print(b)
c = b.pop('나이')
print(b)
print(c)
# c = b.pop('나이') # 없으면 에러
c = b.pop('나이', 0)
print(c)
# c = b.pop() # 전달인자 필수 # TypeError: pop expected at least 1 argument, got 0
# print(c)
print('-'*30)
c = b.popitem()
print(c)
print(b)

a = ['a', 'b', 'c']
b = {
    'a':0,
    'b':0,
    'c':0
}

c = dict.fromkeys(a)
print(c)

# key만 나온다.
for i in c :
    print(i)
    print(c[i])

for k, v, in c.items() :
    print(k, v)

print('-'*30)







