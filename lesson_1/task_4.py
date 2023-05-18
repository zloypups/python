# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите число вертикальных плиток шоколада:"))
m = int(input("Введите число горизонтальных плиток шоколада;"))
k = int(input("введите какое количество плиток шоколада вы хотите отломать"))


if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
