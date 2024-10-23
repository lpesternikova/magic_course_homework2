# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.
# Ввод:
# 1/2
# 2/3
# Вывод:
# 7/6  (будет еще круче если упростите до 1+1/6)

num1 = "1/2"
num2 = "2/3"

num3 = num1 + "/" + num2

drob1 = num3.split("/")

if drob1[1] == drob1[3]:
    result = int(drob1[0]) + int(drob1[2])
    print(str(result) + "/" + drob1[1])
elif drob1[1] != drob1[3]:
    m = int(drob1[1]) * int(drob1[3])
    result1 = int(drob1[0])*(m/int(drob1[1]))
    result2 = int(drob1[2])*(m/int(drob1[3]))
    result3 = result1+result2
    if result3 > m:
        print(str(result3 // m).strip(".0") + "+" + str(result3-m).strip(".0") + "/" + str(m))
    else:
        print(str(result3).strip(".0") + "/" + str(m))



