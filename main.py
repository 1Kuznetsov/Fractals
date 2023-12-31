# Kuznetsov Igor - 100, Yadreeva Maria - 75
import turtle
import ru_local as ru

turtle.hideturtle()


def square(order, size):
    if size <= 1:
        return None
    turtle.speed(500)
    turtle.pensize(2)
    for i in range(4):
        turtle.forward(size)
        turtle.rt(90)
    turtle.up()
    turtle.rt(10)
    turtle.forward(size * 0.1)
    turtle.down()
    square(order*0.9, size * 0.9)


def color_tree(order, size):
    turtle.speed(600)
    turtle.colormode(255)
    cg = 255 - int(order * (250/6)) % 255
    turtle.color(0, cg, 0)

    if order == 0:
        return None
    turtle.forward(size)
    turtle.right(45)
    color_tree(order - 1, size * 0.6)
    turtle.left(90)
    color_tree(order - 1, size * 0.6)
    turtle.right(45)
    turtle.backward(size)


def color_tree_2(order, size):
    turtle.left(90)
    color_tree(order, size)


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


def new_fractal(order, size):
    if order == 0:
        return turtle.fd(size)

    turtle.fd(size)
    turtle.lt(60)
    new_fractal(order - 1, size)
    turtle.lt(180)
    new_fractal(order - 1, size)
    turtle.lt(60)
    new_fractal(order - 1, size)
    turtle.lt(180)
    new_fractal(order - 1, size)
    turtle.lt(120)
    new_fractal(order - 1, size)
    turtle.lt(180)
    new_fractal(order - 1, size)
    turtle.lt(60)
    new_fractal(order - 1, size)
    turtle.lt(180)
    new_fractal(order - 1, size)
    turtle.lt(60)
    turtle.fd(size)


def snowflake(order, size):
    for t in range(2):
        ice_fractal_2(order, size)
        turtle.rt(180)


def new_fractal_2(n, size):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtle.left(angle)
            turtle.forward(size)


def new_fractal_2_2(n, size):
    for i in range(0, 100, 5):
        new_fractal_2(n, i)
        turtle.left(20)


if __name__ == '__main__':
    turtle.tracer(0)
    print(ru.FUNCTIONS)
    action = int(input(ru.CHOICE))
    deep = int(input(ru.ORDER))
    length = float(input(ru.SIZE))

    turtle.up()
    turtle.goto(-200, 0)
    turtle.down()

    if action == 1:
        square(deep, length)

    if action == 2:
        color_tree_2(deep, length)

    if action == 3:
        fractal_branch_2(deep, length)

    if action == 4:
        Koch_curve(deep, length)

    if action == 5:
        snowflake_Koha(deep, length)

    if action == 6:
        minkowski(deep, length)

    elif action == 7:
        ice_fractal_1(deep, length)

    elif action == 8:
        ice_fractal_2(deep, length)

    if action == 9:
        levi_curve(deep, length)

    elif action == 10:
        new_fractal(deep, length)

    elif action == 11:
        dragon(deep, length)

    elif action == 12:
        new_fractal_2_2(deep, length)

    elif action == 13:
        snowflake(deep, length)

    turtle.update()
    turtle.done()
