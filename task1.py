# Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

n = "йцу"
result = 0

for elem in list1:
    if elem == n:
        result += 1
    else:
        result == result
    if result == 2:
        print(list1.index(elem, (list1.index(elem)+1)))
        break
else:
    print("Я не нашел такого значения")
      