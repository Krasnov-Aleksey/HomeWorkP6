'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

from random import randint

min_num=int(input('Введите минимальное значение '))
max_num=int(input('Введите максимальное значение '))


my_list=[randint(-10,10) for _ in range(20)]
res_list=list()

for i in range(len(my_list)):
    if my_list[i]>min_num and my_list[i]<max_num:
        res_list.append(i)
        

print(my_list)
print(res_list)

