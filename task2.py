# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

spisok = str(input())
b = 0
result = 0 

for elem in spisok:
    #print(spisok.index(elem))
    b = spisok.index(elem)
    if b % 2 != 0:
        result += int(elem)
print(result)