# В файле находится N натуральных чисел, записанных через пробел.
#  Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

def get_numbers(link):
    data = open(link, 'r')
    list_of_numbers = data.read() + ' '
    list_of_numbers = list(map(int, list_of_numbers.split()))
    data.close
    return list_of_numbers

def find_number(list):
    number = ''
    for i in range(len(list)):
        if not list[i] - 1 == list[i-1]:
            number = list[i]-1
    return number

path_to_numbers = 'file_for_35.txt'
sequence = get_numbers(path_to_numbers)

print(f'Последовательность из файла: {sequence}')
print(f'Искомое число: {find_number(sequence)}')

