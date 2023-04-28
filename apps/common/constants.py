# from django.db.models import TextChoices


# class UserType(TextChoices):
#     PRODUCER = 'PRODUCER'
#     CONSUMER = 'CONSUMER'


n, m = map(int, input().split())

# Суммируем числа от 1 до n и записываем результат в total
total = sum(range(1, n+1))

# Если total равно m, то просто выводим числа от 1 до n через +
if total == m:
    print('+'.join(str(i) for i in range(1, n+1)) + '=' + str(m))

else:
    # Создаем список из чисел от 1 до n, каждое число в виде строки
    nums = [str(i) for i in range(1, n+1)]
    # Создаем список возможных комбинаций чисел
    combos = [[]]
    for num in nums:
        new_combos = []
        for combo in combos:
            for i in range(len(combo)+1):
                new_combo = combo.copy()
                new_combo.insert(i, num)
                new_combos.append(new_combo)
        combos = new_combos

    # Перебираем все комбинации чисел и ищем те, которые суммируются до m
    for combo in combos:
        if sum(int(''.join(combo[i])) for i in range(len(combo))) == m:
            # Выводим комбинацию с знаками "+"
            print('+'.join(combo) + '=' + str(m))
            break
