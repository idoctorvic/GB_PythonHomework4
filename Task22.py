""" Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит 
сами элементы множеств. """

from random import randint

list1_length = int(input('Enter the length of the first massive: '))
list2_length = int(input('Enter the length of the second massive: '))

list1 = [randint(0, 10) for i in range(list1_length)]
list2 = [randint(0, 10) for i in range(list2_length)]
print(list1, list2, sep='\n')
print('- '*10)
diff_list = set(list1).intersection(set(list2))
print(*sorted(diff_list))