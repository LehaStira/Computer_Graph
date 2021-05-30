import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def get_func(x,y):
    z = np.sin(x) * np.cos(y)
    return z


def get_xyz(h, minx, maxx, miny, maxy):
    x = [i for i in range(minx, maxx, h)]
    y = [i for i in range(miny, maxy, h)]
    xgrid, ygrid = np.meshgrid(x,y)
    z = list()
    for i in xgrid:
        for j in ygrid:
            z.append(get_func(i,j))
    #y = [get_func(i) for i in x]
    return xgrid, ygrid, z


def set_title(my_ax):
    my_ax.set_title('Лабораторная работа №2')


def set_labels(my_ax):
    my_ax.set_xlabel("X")
    my_ax.set_ylabel('Y')


def set_text(my_ax):
    label_string = 'y = x*sin(√(x+b-0.0084))'
    my_ax.text(0, 600, f'{label_string}', fontsize = 15)


def get_range_x():
    res = np.arange(0, 2*pi)
    return res


def get_range_y():
    res = np.arange(0, pi)
    return res


def graph():  # color_line, my_linestyle, my_marker, step, transparency, width, minx, maxx, miny, maxy):
    #my_ax = plt.axes()
    my_fig = plt.figure(figsize=(7,4))
    ax_3d = my_fig.add_subplot(projection = '3d')
    x = get_range_x()
    y = get_range_y()
    xgrid, ygrid = np.meshgrid(x,y)
    zgrid = get_func(xgrid, ygrid)
    ax_3d.plot_surface(xgrid, ygrid, zgrid)
    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')
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


def get_scatter_y():
    min_y = int(input('Введите минимальное значение для y: '))
    #min_x = checking_odz(min_x)
    max_y = int(input('Введите максимальное значение для y: '))
    return min_y, max_y


def main():
    """
    Пятый вариант
    :return:
    """
    #min_x, max_x = get_scatter_x()
    #min_y, max_y = get_scatter_y()
    #my_step = get_step()
    #my_color = get_color()
    #y_linestyle = get_linestyle()
    #my_marker = get_marker()
    #my_transp = get_coef_of_transparency()
    #my_width = get_width()
    graph()#color_line=my_color,
          #my_linestyle=my_linestyle,
          #my_marker=my_marker,
          #tep=my_step,
          #transparency=my_transp,
          #width=my_width,
          #minx = min_x,
          #maxx = max_x,
          #miny = min_y,
          #maxy = max_y)


if __name__ == '__main__':
    main()
