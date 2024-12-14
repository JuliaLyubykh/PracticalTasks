'''
Написать функцию, которая принимает список векторов в n-мерном пространстве,
возвращает их сумму.
Векторы представлены списками чисел одинаковой длины.
'''

# Сумма векторов вычисляется покомпонентно

def sum_vectors(vectors):
    result = [0] * len(vectors[0])
    for vector in vectors:
        result = map(sum, zip(result, vector))

    return tuple(result)
