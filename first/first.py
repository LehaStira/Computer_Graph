import matplotlib.pyplot as plt
from math import *


def get_func(x):
    b = 3.4
    y = x * sin(sqrt(x + b - 0.0084))
    return y


def get_xy(h, minx, maxx):
    # h = 100
    x = [i for i in range(minx, maxx, h)]
    #x = list()
    #for i in range(minx, maxx, h):
    #    if i<0:
    #        print('Недопустимое значение для x')
    #        print('Область допустимых значений для x в данной функции начинается с нуля')

    #y = list()
    #try:
    #for i in x:
    #    try:
    #        tmp = get_func(i)
    #    except ValueError:
    #        print('Недопустимое значение для x')
    #        print('Область допустимых значений для x в данной функции начинается с нуля')
    #        tmp = 0
    #    y.append(tmp)

    #except
    y = [get_func(i) for i in x]
    return x, y


def set_title(my_ax):
    my_ax.set_title('Лабораторная работа №1')


def set_labels(my_ax):
    my_ax.set_xlabel("X")
    my_ax.set_ylabel('Y')


def set_text(my_ax):
    label_string = 'y = x*sin(√(x+b-0.0084))'
    my_ax.text(0, 600, f'{label_string}', fontsize = 15)


def graph(color_line, my_linestyle, my_marker, step, transparency, width, minx, maxx):
    my_ax = plt.axes()
    set_title(my_ax)
    set_labels(my_ax)
    x, y = get_xy(step, minx, maxx)
    set_text(my_ax)
    my_ax.plot(x, y,
               color=color_line,
               linestyle=my_linestyle,
               marker=my_marker,
               alpha=transparency,
               linewidth=width)
    plt.grid(True)
    plt.show()


def get_linestyle():
    dict_of_linestyles = {
        1: '-',
        2: '--',
        3: '-.',
        4: ':'
    }
    input_string = """Меню выбора стиля линии:
            Нажмите 1, для -
            Нажмите 2, для --
            Нажмите 3, для -.
            Нажмите 4, для :
    Ваш ввод:                                  
        """
    my_style = int(input(input_string) or 1)
    return dict_of_linestyles[my_style]


def get_color():
    dict_of_colors = {
        1: 'blue',
        2: 'red',
        3: 'violet',
        4: 'green',
        5: 'yellow'
    }
    input_string = """Меню выбора цвета графика:
        Нажмите 1, чтобы чтобы цвет графика был голубым (по-умолчанию)
        Нажмите 2, чтобы цвет графика был красным
        Нажмите 3, чтобы цвет графика был фиолетовым
        Нажмите 4, чтобы цвет графика был зеленым
        Нажмите 5, чтобы цвет графика был желтым 
Ваш ввод:                                  
    """
    my_color = int(input(input_string) or 1)
    return dict_of_colors[my_color]


def get_step():
    input_string = 'Введите шаг: '
    res = int(input(input_string))
    return res


def get_marker():
    dict_of_markers = {
        1: '.',
        2: '_',
        3: 'x',
        4: 'o'
    }
    input_string = """Меню выбора маркера:
            Нажмите 1, для .
            Нажмите 2, для _
            Нажмите 3, для х
            Нажмите 4, для о 
    Ваш ввод:                                  
        """
    my_color = int(input(input_string) or 1)
    return dict_of_markers[my_color]


def get_coef_of_transparency():  # Коэффициент прозрачности
    input_string = "Введите коэффициент прозрачности (от 0.0 до 1.0): "
    res = float(input(input_string) or 1)
    return res


def get_width():
    input_string = "Введите толщину линии: "
    width = float(input(input_string) or 1)
    return width


def checking_odz(x):
    if x<0:
        print('Недопустимое значение для x')
        print('Область допустимых значений для x в данной функции начинается с нуля')
        x = 0
    return x


def get_scatter_x():
    min_x = int(input('Введите минимальное значение для x: '))
    min_x = checking_odz(min_x)
    max_x = int(input('Введите максимальное значение для x: '))
    return min_x, max_x


def main():
    """
    Десятый вариант
    :return:
    """
    min_x, max_x = get_scatter_x()
    my_step = get_step()
    my_color = get_color()
    my_linestyle = get_linestyle()
    my_marker = get_marker()
    my_transp = get_coef_of_transparency()
    my_width = get_width()
    graph(color_line=my_color,
          my_linestyle=my_linestyle,
          my_marker=my_marker,
          step=my_step,
          transparency=my_transp,
          width=my_width,
          minx = min_x,
          maxx = max_x)


if __name__ == '__main__':
    main()
