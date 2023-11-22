import turtle
import ru_local as ru


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

    elif action == 11:
        turtle.up()
        turtle.goto(-300, 0)
        turtle.down()
        dragon(deep, length)

    turtle.update()
    turtle.done()

