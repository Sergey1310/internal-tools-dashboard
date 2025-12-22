import turtle
import math

def square(t, length = 100):
    """Рисует квадрат со стороной length и используя t как объект Turtle"""
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, length = 100, steps = 4, angle = 90):
    """Рисует steps отрезков с длинной length пикселей и углом между ними angle градусов
    используя t как объект Turtle"""
    for i in range(steps):
        t.fd(length)
        t.lt(angle)


def polygon(t, length = 100, steps = 4):
    """Рисует полигон с steps количеством углов, длинной стороны length и
    используя t как объект Turtle"""
    angle = 360 / steps
    polyline(t, length, steps, angle)

def circle(t, radius):
    """Рисует круг с радиусом radius и используя botb как объект Turtle"""
    arc(t, radius, 360)

def arc(t, radius, angle):
    """Рисует окружность или её часть с радиусом radius охватывающую угол angle и
     используя t как объект Turtle"""
    arc_length = 2 * math.pi * radius * abs(angle) / 360
    steps = int(arc_length / 4) + 3
    step_length = arc_length / steps
    step_angle = angle / steps
    t.lt(step_angle/2)
    polyline(t, step_length, steps, step_angle)
    t.rt(step_angle/2)

def petal (t, length, wide):
    radius = (length * length + wide * wide) / (4 * wide)
    angle = 4 * math.atan(wide / length) * 180 / math.pi
    turn = 180 - angle
    arc(t, radius, angle)
    t.lt(turn)
    arc(t, radius, angle)
    t.lt(turn)

def flower (t, petals, length, wide):
    for i in range(petals):
        petal(t, length, wide)
        t.lt(360/petals)

def pai (t, length = 100, steps = 4, angle = 90):
    for i in range(steps):
        t.fd(length)
        t.lt(angle)
        t.rt(90)
        t.fd(length)
        t.bk(length)
        t.lt(90)

def main():
    bob = turtle.Turtle()
    pai(bob, 100)
    turtle.mainloop()
if __name__ == '__main__':
    main()