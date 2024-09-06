def test_function():
    global x
    x = x + 1
    print("test_function меняет глобальную переменную")
    print("x = ", x)

    def inner_function():
        y = 2 * x
        print("y = ", y)
        print("Я в области видимости функции test_function")

    inner_function()


x = 5
test_function()
# inner_function()

# ОТВЕТ если раскомментировать inner_function()

# Traceback (most recent call last):
#   File "D:\Python\ns_dz\module_4_2.py", line 17, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# test_function меняет глобальную переменную
# x =  6
# y =  12
# Я в области видимости функции test_function