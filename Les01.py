'''
value = None
print(type(value))
a = 123
b = 1.23
print(a)
print(b)
value = 1234
print(value)
print(type(value))

s  ='qwerty'
print(s)
print(a, ' - ',b, ' - ',s)
print('{1} - {2} - {0}'.format(a,b,s))
print(f'{a} - {b} - {s}')

f= False
print(f)
'''
'''
list = ['1','2','3',1,2,3]
col = []
print(list)
'''
'''
print('Введите а:')
a = int(input())
print('Введите b:')
b = int(input())
print(a,b,' ', a+b)
#print('{} {}'.format(a,b))
#print(f'{a} {b}')
'''
'''
a= 1.3123
b = 3
c = round(a*b,3)
print(c)
'''
'''
a = 3
a +=5
print(a)
'''
'''
a= 1<3 and 5!=2
print(a)
'''
'''
a = 1 < 3 < 5
print(a)

func = 1
t = 4
x = 2
print(func<t>(x))
'''
'''
f = 1 > 2 or 4 < 6
print(f)

p = [1,2,3,4]
print(p)
print( not 2 in p)

is_add = not p[0] %2 
print(is_add)
'''
'''
a = int(input('a = '))
b = int(input('b = '))
if a>b:
    print(a)
else:
    print(b)
'''
'''
org = 25
inv = 0
while org !=0:
    inv = inv * 10 + (org % 10)
    org //= 10
print(inv)
'''
'''
for i in range(0,6,2):
    print(i)
'''
'''
a = list(range(4,10))
print(a)
print(len(a))
a[2] = 45
print(a)

for i in range (10):
    i = i**2
    print(i)
'''

def fun(x):
    x = x ** 2
    return x

print(fun(4))