import turtle
import ru_local as ru

# def square(order, size):
#     if order == 0:
#         return turtle.fd(size)
#
#
# def binary_tree(order, size):
#     if  order == 0:
#         return turtle.fd(size)


def fractal_branch(order, size):
    if order == 0:
        turtle.left(180)
        return

    x = size / (order + 1)

    turtle.pensize(3)
    turtle.speed(300)


    for i in range(order):
        turtle.forward(x)
        turtle.left(45)
        fractal_branch(order - i - 1, 0.5 * x * (order - i - 1))
        turtle.left(90)
        fractal_branch(order - i - 1, 0.5 * x * (order - i - 1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)

def fractal_branch_2(order, size):
    turtle.up()
    turtle.left(90)
    turtle.down()
    fractal_branch(order, size)


def Koch_curve(order, size):
    if order == 0:
        return turtle.fd(size)
    Koch_curve(order - 1, size / 3)
    turtle.lt(60)
    Koch_curve(order - 1, size / 3)
    turtle.rt(120)
    Koch_curve(order - 1, size / 3)
    turtle.lt(60)
    Koch_curve(order - 1, size / 3)

def snowflake_Koha(order, size):
    for i in range(3):
        Koch_curve(order, size)
        turtle.right(120)


def levi_curve(order, size):
    if order == 0:
        return turtle.forward(size)
    turtle.speed(400)
    turtle.left(45)
    levi_curve(order - 1, size / 2)
    turtle.right(90)
    levi_curve(order - 1, size / 2)
    turtle.left(45)

# def Mashas_new_quarter_square(order, size):
#     for i in range(6):
#         turtle.fd(size)
#         turtle.rt(90)
# def Mashas_new_quarter(order, size):
#     if size <= 1:
#         return None
#
#     turtle.speed(400)
#     turtle.pensize(2)
#
#     Mashas_new_quarter_square(order, size)
#     turtle.lt(5)
#     return Mashas_new_quarter(order, 0.9 * size)


def minkowski(order, size):
    if order == 0:
        return turtle.fd(size)

    minkowski(order - 1, size)
    turtle.lt(90)
    minkowski(order - 1, size)
    turtle.rt(90)
    minkowski(order - 1, size)
    turtle.rt(90)
    minkowski(order - 1, size)
    minkowski(order - 1, size)
    turtle.lt(90)
    minkowski(order - 1, size)
    turtle.lt(90)
    minkowski(order - 1, size)
    turtle.rt(90)
    minkowski(order - 1, size)


def ice_fractal_1(order, size):
    if order == 0:
        return turtle.fd(size)

    ice_fractal_1(order - 1, size / 2)
    turtle.lt(90)
    ice_fractal_1(order - 1, size / 4)
    turtle.rt(180)
    ice_fractal_1(order - 1, size / 4)
    turtle.lt(90)
    ice_fractal_1(order - 1, size / 2)


def ice_fractal_2(order, size):
    if order == 0:
        return turtle.fd(size)

    ice_fractal_2(order - 1, size / 2)
    turtle.lt(120)
    ice_fractal_2(order - 1, size / 4)
    turtle.rt(180)
    ice_fractal_2(order - 1, size / 4)
    turtle.lt(120)
    ice_fractal_2(order - 1, size / 4)
    turtle.rt(180)
    ice_fractal_2(order - 1, size / 4)
    turtle.lt(120)
    ice_fractal_2(order - 1, size / 2)


def dragon(order, size, angle='-'):
    if order == 0:
        return turtle.fd(size)

    if angle == '-':
        turtle.lt(45)
    else:
        turtle.rt(45)

    dragon(order - 1, size, '-')

    if angle == '-':
        turtle.rt(90)
    else:
        turtle.lt(90)

    dragon(order - 1, size, '+')

    if angle == '-':
        turtle.lt(45)
    else:
        turtle.rt(45)


if __name__ == '__main__':
    turtle.tracer(0)

    action = int(input(ru.CHOICE))
    deep = int(input(ru.ORDER))
    length = float(input(ru.SIZE))

    if action == 3:
        fractal_branch_2(deep, length)

    if action == 4:
        Koch_curve(deep, length)

    if action == 5:
        snowflake_Koha(deep, length)

    if action == 6:
        turtle.up()
        turtle.goto(-700, 0)
        turtle.down()
        minkowski(deep, length)

    elif action == 7:
        turtle.up()
        turtle.goto(-700, 0)
        turtle.down()
        ice_fractal_1(deep, length)

    elif action == 8:
        turtle.up()
        turtle.goto(-700, 0)
        turtle.down()
        ice_fractal_2(deep, length)

    if action == 9:
        levi_curve(deep, length)

    elif action == 11:
        turtle.up()
        turtle.goto(-300, 0)
        turtle.down()
        dragon(deep, length)

    turtle.update()
    turtle.done()

