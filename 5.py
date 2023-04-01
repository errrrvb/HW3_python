n = input().split() # преобразовываем строку в список
count = 0
for i in range(len(n)):
    for k in range(i+1, len(n)): # прибавляем к индексу i единицу, дабы сравнить цифры. делаем ограничение в длинну списка(не более)
        if n[i] == n[k]:
            count += 1
print(count)