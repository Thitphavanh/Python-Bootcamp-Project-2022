import turtle
import random
tao = turtle.Pen()
tao.shape('turtle')
tao.pensize(2)
color_list = ['red', 'blue', 'yellow', 'orange', 'pink', 'green', 'purple',
              '#d6532b', '#612613', '#d12c2c', '#32ed8c', '#f26bc3', '#41ff3b']
tao.color('red')


def rectangle(size):
    tao.fd(size)
    tao.lt(90)
    tao.fd(size)
    tao.lt(90)
    tao.fd(size)
    tao.lt(90)
    tao.fd(size)
    tao.lt(90)


def goto(x, y):
    tao.penup()
    tao.goto(x, y)
    tao.pendown()


for i in range(30):
    color = random.choice(color_list)
    tao.color(color)
    x = random.randint(-500, 500)
    y = random.randint(-200, 200)
    size = random.randint(10, 100)
    goto(x, y)

    # ໃສ່ສີ ຫຼື ບໍ່ໃສ່ສີ
    fill = random.choice([True, False])
    rect = random.choice([True, False])
    if fill == True:
        tao.begin_fill()
        if rect == True:
            rectangle(size)
        else:
            tao.circle(size)
        tao.end_fill()
    else:
        if rect == True:
            rectangle(size)
        else:
            tao.circle(size)
