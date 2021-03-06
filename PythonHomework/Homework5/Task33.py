# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

print('введите к (степень многочлена): ')
pow = int(input()) 
list_of_coeffs = [randint(0, 100) for i in range(pow+1)] 

def create_polynom(list, k):

    polynom = [str(list[i]) + '*x^' + str(k-i) for i in range(k-1) if list[i] != 0]

    if list[k-1] != 0:
        polynom.append(str(list[k-1])+'*x')
    if list[k] != 0:
        polynom.append(str(list[k])) 
    return polynom

result = ' + '.join(create_polynom(list_of_coeffs, pow))  + ' = 0'
str = result.replace('1*x', 'x')

print(str)

with open('polynom.txt', 'w') as data:
    data.write(str)
