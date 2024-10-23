# Создайте вручную список содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.
# Для списка: [1, 2, "3", "4", True, 5.5]
# Ответ:  {int: [1, 2, 5], float: [5.5], str: ["3", "4"], bool: [True]}

list1 = (1, 3, True, False, "str", "6", 6.8)
dict = {}

for elem in list1:
    if type(elem) == str:
        if str not in dict:
            dict["str"] = [elem]
        else:
            dict["str"].append(elem)
    elif type(elem) == int:
        if "int" not in dict:
            dict["int"] = [elem]
        else:
            dict["int"].append(elem)
    elif type(elem) == bool:
        if "bool" not in dict:
            dict["bool"] = [elem]
        else:
            dict["bool"].append(elem)
    elif type(elem) == float:
        if "float" not in dict:
            dict["float"] = [elem]
        else:
            dict["float"].append(elem)

print(dict)