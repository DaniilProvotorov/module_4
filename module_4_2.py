


def test_function():
    def inner_function(x):
        print(x)
    inner_function('Я в области видимости функции test_function')
#inner_function('Я в области видимости функции test_function')- выдает ошибку т.к. вызываем в пространстве видимости глобальном, а переменная в локальном пространстве


print(test_function())