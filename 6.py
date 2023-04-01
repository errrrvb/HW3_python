def IsSymmetric(a):
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]: # проверка на симметричность столбцов относительно диагонали
                return "NO"
    return "YES"
 
n = int(input())
a = []
for i in range(n):         # добавление элементов в список
    num = input().split()
    a.append(num)

print(IsSymmetric(a))
