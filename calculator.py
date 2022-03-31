from prompt_toolkit.shortcuts import button_dialog, input_dialog, message_dialog
from NumberValidator import FloatValidator
import math


def calculator():
    run = True

    while run:

        result = button_dialog(
            title='Калькулятор',
            buttons=[
                ('+', "+"),
                ('-', "-"),
                ('*', "*"),
                ('/', "/"),
                ('//', "//"),
                ('%', "%"),
                ('**', "**"),
                ('remainder', "remainder"),
                ('atan2', "atan2"),
                ('fmod', "fmod"),
                ('copysign', "copysign"),
                ('параллелепипед', "параллелепипед"),
                ('Назад', None)
            ],
        ).run()

        if result is None:
            run = False
            continue

        try:
            a, b = 0, 0
            if result != "параллелепипед":
                a, b = get_numbers()
                if not a:
                    continue

            if result == "+":
                show_result(a + b)
            elif result == "-":
                show_result(a - b)
            elif result == "*":
                show_result(a * b)
            elif result == "/":
                show_result(a / b)
            elif result == "//":
                show_result(a // b)
            elif result == "%":
                show_result(a // b)
            elif result == "**":
                show_result(a ** b)
            elif result == "remainder":
                show_result(math.remainder(a, b))
            elif result == "atan2":
                show_result(math.atan2(a, b))
            elif result == "fmod":
                show_result(math.fmod(a, b))
            elif result == "copysign":
                show_result(math.copysign(a, b))
            elif result == "параллелепипед":
                lm = lambda l, w, h: 2 * h * (l + w)
                lm2 = lambda l, w, h: 4 * l + 4 * w + 4 * h
                l, w, h = get_parallelepiped()
                if not l:
                    continue
                show_result("Площадь: {}\nПериметр: {}".format(lm(l, w, h), lm2(l, w, h)))
        except Exception as e:
            show_error(str(e))


def get_numbers():
    first_number = input_dialog(title='Калькулятор', text='Введите первое число', validator=FloatValidator()).run()
    if first_number is None or first_number == "":
        return False, False

    second_number = input_dialog(title='Калькулятор', text='Введите второе число', validator=FloatValidator()).run()
    if second_number is None or second_number == "":
        return False, False

    return float(first_number), float(second_number)


def get_parallelepiped():
    length = input_dialog(title='Калькулятор', text='Введите длину', validator=FloatValidator()).run()
    if length is None or length == "":
        return False, False

    width = input_dialog(title='Калькулятор', text='Введите ширину', validator=FloatValidator()).run()
    if width is None or width == "":
        return False, False

    height = input_dialog(title='Калькулятор', text='Введите высоту', validator=FloatValidator()).run()
    if height is None or height == "":
        return False, False

    return float(length), float(width), float(height)


def show_result(res):
    message_dialog(
        title='Результат',
        text=str(res)).run()


def show_error(text: str):
    message_dialog(
        title='Ошибка',
        text=text).run()
