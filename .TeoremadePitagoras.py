from math import sqrt
print('Digite 0 para oque falta')
cat1 = float(input('Primeiro cateto vale: '))
cat2 = float(input('Segundo cateto vale: '))
hip = float(input('Hipotenusa vale: '))
if cat1 < 1:
    cat1 += sqrt(hip ** 2 - cat2 ** 2)
    print('O valor do primeiro cateto é: ', cat1)
if cat2 < 1:
    cat2 += sqrt(hip ** 2 - cat1 ** 2)
    print('O valor do segundo cateto é: ', cat2)
if hip < 1:
    hip += sqrt(cat1 ** 2 + cat2 ** 2)
    print('O valor da hipotenusa é: ', hip)
