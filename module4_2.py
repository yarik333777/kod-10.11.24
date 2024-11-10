def test_function():
    def inner_function():
        print('Я в области видимасти функции test_functon')

    return inner_function()

inner_function()