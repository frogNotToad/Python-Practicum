name = input()
a = int(input())
b = int(input())
c = int(input())

s1 = f'{b}кг * {a}руб/кг'
s2 = f'{a * b}руб'
s3 = f'{c - a * b}руб'

print('================Чек================')
print('Товар:' + ' ' * (29 - len(name)) + name)
print('Цена:' + ' ' * (30 - len(s1)) + s1)
print('Итого:' + ' ' * (29 - len(s2)) + s2)
print('Внесено:' + ' ' * (24 - len(str(c))) + str(c) + 'руб')
print('Сдача:' + ' ' * (29 - len(s3)) + s3)
print('===================================')
