SPACE_BEFORE_MINUS  = 4
SPACE_BEFORE_VERT = 14

def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

# Сегменты рисуют одну из сторон каждой клетки, конечный сегмент завершает линию или ряд.
def horizontal_segment():
    print('+' + ('  -' * SPACE_BEFORE_MINUS ) + '  ', end=' ')
def horizontal_segment_end():
    print('+' + ('  -' * SPACE_BEFORE_MINUS ) + '  +', end=' ')


def vertical_segment():
    print('|' + (' ' * SPACE_BEFORE_VERT), end=' ')
def vertical_segment_end():
    print('|' + (' ' * SPACE_BEFORE_VERT) + '|', end=' ')





def horizontal_segment_paint_twice():
    horizontal_segment()
    horizontal_segment_end()

def horizontal_segment_paint_four():
    horizontal_segment()
    do_twice(horizontal_segment)
    horizontal_segment_end()

# Линия - создаёт линию из сегментов заданной длины, завершая конечным сегментом
def horizontal_line(paint):
    paint()




def vertical_segment_paint_twice():
    vertical_segment()
    vertical_segment_end()


def vertical_segment_paint_four():
    vertical_segment()
    do_twice(vertical_segment)
    vertical_segment_end()

def vertical_line(paint):
    paint()


# Сегмент сетки рисует один ряд из горизонтальных и вертикальных линий заданной длинны
def grid_segment(horizontal_painter, vertical_painter):
    horizontal_painter()
    print()
    vertical_painter()
    print()
    vertical_painter()
    print()
    vertical_painter()
    print()
    vertical_painter()
    print()

def grid_segment_twice():
    grid_segment(horizontal_segment_paint_twice,vertical_segment_paint_twice)
    grid_segment(horizontal_segment_paint_twice,vertical_segment_paint_twice)
    horizontal_line(horizontal_segment_paint_twice)


def grid_segment_four():
    grid_segment(horizontal_segment_paint_four,vertical_segment_paint_four)
    grid_segment(horizontal_segment_paint_four,vertical_segment_paint_four)
    grid_segment(horizontal_segment_paint_four,vertical_segment_paint_four)
    grid_segment(horizontal_segment_paint_four,vertical_segment_paint_four)
    horizontal_line(horizontal_segment_paint_four)

# основная программа, рисует сетку из сегментов сетки, завершая нижней горизонтальной линией.



def main():

    grid_segment_twice()
    print()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print()
    grid_segment_four()

if __name__ == '__main__':
    main()