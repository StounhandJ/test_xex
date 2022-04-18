from prompt_toolkit.shortcuts import button_dialog
from counting import counting
from matrix import matrix
from calculator import calculator

run = True

while run:

    result = button_dialog(
        title='Задание',
        buttons=[
            ('Калькулятор', 0),
            ('Подсчет', 1),
            ('Матрица', 2),
            ('Выход', None)
        ],
    ).run()

    if result is None:
        run = False
    elif result == 0:
        calculator()
    elif result == 1:
        counting()
    elif result == 2:
        matrix()


def counting():
    res = input_dialog(title='Подсчет в строке',
                       text='Введите строку для подсчёта количества разделителей').run()
    if res is None:
        return

    message_dialog(
        title='Результат',
        text="Количество символов = {}\nКоличество пробелов = {}\nКоличество запятых = {}".format(
            len(re.findall(r'[\w]', res)),
            len(re.findall(r'[\s]', res)),
            len(re.findall(r'[,]', res))
        )).run()


