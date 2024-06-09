print('-------Фабрика функций-------')


def math_func(n):
    if n == 5:
        def exponentiation(x):
            return x ** 3

        return exponentiation

    elif n == 10:
        def division(x):
            return x // 2

    else:
        raise Exception('Я могу возводить в куб или делить на 2!')

    return division


my_operation = math_func(5)
my_operation_2 = math_func(10)
print(my_operation(5))
print(my_operation_2(10))

"""expon_1 = math_func(5)
expon_2 = math_func(10)
result = map(expon_1, my_operation)
print(list(result))

result = map(expon_2, my_operation)
print(list(result))"""

print('-------Лямбда-функции--------')

my_lambda = lambda x: x ** 2
print(my_lambda(x=20))


def lambda_1(x):
    return x ** 2


lamb_1 = lambda_1(20)
print(lamb_1)

print('------Вызываемые Объекты------')


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


my_rect = Rect(6, 9)
result = my_rect()
print(f'Площадь прямоугольника: {result}')