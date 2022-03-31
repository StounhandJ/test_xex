def matrix():
    count_column = input_dialog(title='Матрица', text='Кол-во столбцов в матрице', validator=NumberValidator()).run()
    if count_column is None or count_column == "":
        return

    count_row = input_dialog(title='Матрица', text='Кол-во строк в матрице', validator=NumberValidator()).run()
    if count_row is None or count_row == "":
        return

    start_number = input_dialog(title='Матрица', text='Начальное число', validator=FloatValidator()).run()
    if start_number is None or start_number == "":
        return

    indent_number = input_dialog(title='Матрица', text='Шаг, то число на которое должно увеличиваться',
                                 validator=FloatValidator()).run()
    if indent_number is None:
        return

    arr = []
    current_number = int(start_number)
    for y in range(0, int(count_row)):
        arr.append([])
        for x in range(0, int(count_column)):
            arr[y].append(current_number)
            current_number += int(indent_number)

    arr_str = ""
    for line in arr:
        arr_str += "{}\n".format(' '.join(str(l) for l in line))

    message_dialog(
        title='Результат',
        text=arr_str).run()