""" Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только 
по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них 
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора 
черники. Эта система состоит из управляющего модуля и нескольких 
собирающих модулей. Собирающий модуль за один заход, находясь 
непосредственно перед некоторым кустом, собирает ягоды с этого куста и 
с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое 
может собрать за один заход собирающий модуль, находясь перед некоторым 
кустом заданной во входном файле грядки. """

from random import randint

bush_numbers = int(input('How any bushes of blueberry: '))
bush_yield = [randint(1, 10) for _ in range(bush_numbers)]
berry_yield = []

for i in range(1, bush_numbers):
    if i < bush_numbers - 1:
        berry_yield.append(bush_yield[i] + bush_yield[i + 1] + bush_yield[i - 1])
    else:
        berry_yield.append(bush_yield[i] + bush_yield[0] + bush_yield[i - 1])
        
print(bush_yield) # The list of yields of each bush
print(berry_yield) # The list of summs of 3 neighbouring bushes.
print(f'The maximum yield from 3 bushes will be {max(berry_yield)}')