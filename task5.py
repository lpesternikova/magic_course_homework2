# В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

str1 = "САМАЯ Длинная строка в мире, мире строка f hj hj yu yu ooo ooo ooo ooo ooo ooo жажаж жажаж жажаж строка !строка, строкка самая длинная ?или может не самая или не длинная."
str2 = str1.replace(",","") 
str3 = str2.replace(".","") 
str4 = str3.replace("!","") 
str5 = str4.replace("?","")
str6 = str5.lower()

list1 = str6.split(" ")
dict = {}

for elem in list1:
    if elem in dict:
        dict[elem] += 1
    else:
        dict[elem] = 1

sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse=True)
print(sorted_dict[0:10:])
