import turtle
import ru_local as ru


def minkowski(order, size):
    if order == 0:
        return turtle.forward(size)
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


if __name__ == '__main__':
    turtle.tracer(0)
    action = int(input(ru.CHOICE))

    while action != 0:
        deep = int(input(ru.ORDER))
        length = float(input(ru.SIZE))
        if action == 6:
            turtle.up()
            turtle.goto(-800, 0)
            turtle.down()
            minkowski(deep, length)

        action = int(input(ru.CHOICE))

    turtle.update()
    turtle.done()

