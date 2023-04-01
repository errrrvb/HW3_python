n = int(input()) 
a = '0'
curr = 0
for i in range(10):       # создаем последовательность
    if curr == len(a):
        b = ''
        for i in range(len(a)):
            if a[i] == '0':
                b += '1'
            else:
                b += '0'
        a += b
    curr +=1

ans = ''
a.split()
for i in range(n): # в ответ записываем только нужную последовательность цифр
    ans += a[i]
print(ans)










