def max_points(points):
    # Количество этажей
    num_floors = len(points)

    # Создаем таблицу dp, копируем последнюю строку из points
    dp = points[-1][:]

    # Заполняем таблицу dp, двигаясь снизу вверх
    for i in range(num_floors - 2, -1, -1):
        # Создаем временный массив для текущего этажа
        current_dp = [0] * len(points[i])
        for j in range(len(points[i])):
            # Находим максимальное количество баллов, которое можно набрать, спускаясь вниз
            current_dp[j] = points[i][j] + max(dp[j], dp[j + 1])
        print("current_points", current_dp)
        # Обновляем dp для следующей итерации
        dp = current_dp
    # Возвращаем максимальное количество баллов, которое можно набрать с 10-го этажа
    return dp[0]


# Пример входных данных
points = [
    [5],
    [3, 8],
    [6, 2, 9],
    [1, 5, 3, 7],
    [4, 8, 2, 6, 9],
    [7, 1, 4, 3, 5, 2],
    [5, 6, 3, 8, 7, 2, 1],
    [3, 7, 2, 9, 1, 4, 6, 5],
    [8, 1, 5, 7, 6, 3, 2, 4, 9],
    [6, 5, 9, 2, 3, 8, 1, 4, 7, 5]
]

# Вызываем функцию и выводим результат
print("Максимальное количество баллов, которое можно набрать:", max_points(points))
