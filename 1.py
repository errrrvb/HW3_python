def can_eat(a1,b1,a2,b2):    # Функция работает по шахматным правилам (в нашем случаем по правилам хода коня)
    if abs(a1-b1) == 1:
        if abs(a2-b2) == 2:
            return "True"
    elif abs(a2-b2) == 1:
        if abs(a1-b1) == 2:
            return "True"
    
    return "False"

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

print(can_eat(a1,b1,a2,b2))