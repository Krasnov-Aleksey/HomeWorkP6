'''
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an= a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''
f_nun=int(input('Введите перый элемент '))
diff_num=int(input('Введите разность '))
count_num=int(input('Введите количество элементов '))
arith_prog=list()

for i in range(1,count_num+1):
    
    arith_prog.append(f_nun+(i-1)*diff_num)

print(arith_prog)
