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