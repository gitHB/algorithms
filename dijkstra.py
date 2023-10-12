import math


def arg_min(solve_table, inspected_vertex):
    vertex_with_min_weight = -1  # если на выходе -1 значит просмотрены все вершины
    max_weight = math.inf  # максимальное значение
    for vertex, curr_vertex_weight in enumerate(solve_table):
        if curr_vertex_weight < max_weight and vertex not in inspected_vertex: # находим минмальные значения для еще не просмотренных вершин
            max_weight = curr_vertex_weight
            vertex_with_min_weight = vertex  # индекс мин значения будет искомой вершиной

    return vertex_with_min_weight


adjacency_matrix = ((0, 3, 1, 3, math.inf, math.inf),
                                 (3, 0, 4, math.inf, math.inf, math.inf),
                                 (1, 4, 0, math.inf, 7, 5),
                                 (3, math.inf, math.inf, 0, math.inf, 2),
                                 (math.inf, math.inf, 7, math.inf, 0, 4),
                                 (math.inf, math.inf, 5, 2, 4, 0))

number_of_vertex = len(adjacency_matrix)    # число вершин в графе
solve_table = [math.inf] * number_of_vertex # последняя строка таблицы

vertex = 0                             # стартовая вершина (нумерация с нуля)
inspected_vertex = {vertex}            # просмотренные вершины
solve_table[vertex] = 0                # нулевой вес для стартовой вершины
vertex_links = [0] * number_of_vertex  # оптимальные связи между вершинами

while vertex != -1:          # цикл, пока не просмотрим все вершины
    for curr_vertex, weight in enumerate(adjacency_matrix[vertex]):     # перебираем все связанные(не нулевые) вершины с вершиной vertex
        if curr_vertex not in inspected_vertex:                         # если вершина еще не просмотрена
            curr_vertex_weight = solve_table[vertex] + weight           # прибавляем текущий вес связи для вершины
            if curr_vertex_weight < solve_table[curr_vertex]:           # если текущий вес связи получился меньше
                solve_table[curr_vertex] = curr_vertex_weight           # то сохраняем новое значение
                vertex_links[curr_vertex] = vertex                      # связываем вершину curr_vertex с вершиной vertex

    vertex = arg_min(solve_table, inspected_vertex)   # выбираем следующий узел с наименьшим весом
    if vertex >= 0:                                   # выбрана очередная вершина
        inspected_vertex.add(vertex)                  # добавляем новую вершину в рассмотренные

print(solve_table, vertex_links, sep="\n")

# формирование оптимального маршрута:
start = 0
end = 4
path = [end]
while end != start:
    end = vertex_links[path[-1]]
    path.append(end)

print(path)