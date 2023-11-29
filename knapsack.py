def knapsack(values, weights, capacity):
    """
    Решение задачи о рюкзаке с использованием динамического программирования.
    :param values: Список значений предметов.
    :param weights: Список весов предметов.
    :param capacity: Вместимость рюкзака.
    :return: Максимально возможная сумма значений предметов, которые можно уложить в рюкзак.
    """
    n = len(values)
    # Base case initialization
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                # Стоимость предмета + максимальноя стоимость без учета этого предмета
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Если вес предмета больше вместимости рюкзака w,
                # то этот предмет не может быть включен в оптимальное решение.
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]


# Пример использования функции
values = [1500, 2000, 2500]
weights = [1, 3, 4]
capacity = 4

max_value = knapsack(values, weights, capacity)
print("Максимальная стоимость: ", max_value)
