from typing import get_args

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import pi
from pprint import pprint


def get_range_x():
    res = np.arange(0, 2*pi)
    return res


def get_range_y():
    res = np.arange(0, pi)
    return res


def get_snood(x, y):
    return np.meshgrid(x,y)


def get_type_graph():
    """
    :return: user input, what type of graph he prefer
    """
    dict_of_graph = {
        1: 'surface',
        2: 'wireframe',
        3: 'scatter',
        4: 'contour'
    }
    input_string = """Меню выбора типа графика:
            Нажмите 1, для "surface"
            Нажмите 2, для "wireframe"
            Нажмите 3, для "scatter"
            Нажмите 4, для "contour"
    Ваш ввод:                                  
        """
    my_answer = int(input(input_string) or 4)
    return dict_of_graph[my_answer]


def get_color():
    """
    :return: color of line, that user prefer
    """
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


def get_x_stride():
    """
    :return: x stride from user input which user prefer
    """
    step = int(input('Введите шаг по x: '))
    return step


def get_y_stride():
    """
    :return: y stride from user input which user prefer
    """
    step = int(input('Введите шаг по y: '))
    return step


def get_count_of_slices():
    """
    :return: count of slice (size slice) that user prefer
    """
    slices = int(input('Введите количество слоёв (максимум 4), ') or 3)
    if slices > 4 or slices <=0:
        return ValueError('Неверно введенное количество слоёв')
    return slices


def func(x, y):
    z = np.sin(x) * np.cos(y)
    return z


def get_first_step_zgrid(old, count):
    """
    first step of making zgrid valide for api of 3d
    :return: initial transformed zgrid
    """
    res = list()
    old = list(old)
    print(len(old))
    for i in range(count):
        print(f'i = {i}')
        print(f' old[i]  = {old[i]}')
        arr_to_append = old[i]
        res.append(arr_to_append)
    return res


def get_final_step_of_zgrid(old, default_count = 4):
    """
    final setting of zgrid
    :param old: old version of zgrid from before step
    :param default_count: count of slicels that we need to have
    :return:
    """
    count_of_slices = len(old)  # count_of_slices that we have
    res = old
    # если у нас слоев меньше 32, всё остальное нужно забить нулями, необходимость функции
    if count_of_slices<default_count:
        for i in range(count_of_slices, default_count):
            res.append([])
            for j in range(7):
                res[i].append(0)
    return res


def set_zgrid(x_grid, y_grid, count_of_slice):
    """
    Setting of zgrid on three steps.
    0. Setting zgrid by meshgrid
    1. 2. adapt this value for needings of api funtction
    :param x_grid:
    :param y_grid:
    :param count_of_slice:
    :return: zgriid
    """
    zero_step_zgrid = func(x_grid, y_grid)
    first_step_zgrid = get_first_step_zgrid(
        old =  zero_step_zgrid,
        count = count_of_slice
    )
    final_zgrid = get_final_step_of_zgrid(old = first_step_zgrid)
    return final_zgrid


def get_function_plot(ax3d, type_graph):
    """
    :param ax3d: we take function from here
    :param type_graph: type, depending of which we get function
    :return:
    """
    if type_graph == 'surface':
        res = ax3d.plot_surface
    elif type_graph == 'wireframe':
        res = ax3d.plot_wireframe
    elif type_graph == 'scatter':
        res = ax3d.scatter
    elif type_graph == 'contour':
        res = ax3d.contour
    return res


def second_plot(x, y, color_line):
    my_ax = plt.axes()
    my_ax.plot(x, y,
               color=color_line)
    plt.grid(True)
    plt.show()


def make_graph(color, type_graph, r, c, xgrid, ygrid, zgrid):
    my_fig = plt.figure(figsize=(10, 7))
    ax_3d = my_fig.add_subplot(projection='3d')

    function_plot = get_function_plot(ax_3d, type_graph)
    try:
        function_plot(xgrid, ygrid, zgrid, rstride = r, cstride = c, color = color)
    except Exception as err:
        if type_graph == 'scatter':
            function_plot(xgrid, ygrid, zgrid, color = color)
        else:
            print(f'Exception = {err}')
            #function_plot(xgrid, ygrid, zgrid)

    ax_3d.set_xlabel('x')
    ax_3d.set_ylabel('y')
    ax_3d.set_zlabel('z')

    plt.show()
    second_plot(x = ygrid,
                y = zgrid,
                color_line=color)


def main():
    x = get_range_x()
    y = get_range_y()
    x_grid, y_grid = get_snood(x, y)
    my_color = get_color()
    my_type = get_type_graph()
    r_stride = get_x_stride()
    c_stride = get_y_stride()
    count_of_slices = get_count_of_slices()
    z_grid = set_zgrid(x_grid, y_grid, count_of_slices)
    print()
    pprint(f'ITS ZGRIIID = {z_grid}')
    print(len(z_grid))
    make_graph(color = my_color,
               type_graph=my_type,
               r = r_stride,
               c = c_stride,
               xgrid= x_grid,
               ygrid=y_grid,
               zgrid=z_grid)


if __name__ == '__main__':
    main()