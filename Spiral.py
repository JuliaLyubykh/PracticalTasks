'''
Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали, выходящей из левого верхнего
угла и закрученной по часовой стрелке
'''

# Функция отвечает за создание матрицы
def spiralMaker(n):

    # Номера элементов матрицы
    m = 0
    k = 0

    # Шаг изменений переменных номеров элементов
    difm = 1
    difk = 0

    # Инициализация матрицы, заполненной нулями
    matrix = [[0]* n for j in range(n)]

    for i in range(1, n**2+1): # Поэлементно

        matrix[m][k] = i # Присвоение элемента

        # Проверка на выход за пределы
        newm = m+difm
        newk = k+difk
        if 0<=newm<n and 0<=newk<n and matrix[newm][newk] == 0:

            # Новые значения номеров элемента
            m = newm
            k = newk

        else:
            # Изменение шага номера элемента
            difm, difk  = -difk, difm

            # Новые значения номеров элемента
            m = m + difm
            k = k + difk

    return matrix

# Функция для вывода матрицы
def spiralPrinter(matrix):
    n = range(len(matrix)) # Переменная, равная размеру матрицы для перечисления
    for k in n:
        for m in n:
            print(matrix[m][k],end=' ') # Вывод элемента матрицы
        print()


spiralPrinter(spiralMaker(int(input()))) # Вводится размерность матрицы