SPACE_BEFORE_MINUS  = 4
SPACE_BEFORE_VERT = 14

# Сегметы рисуют одну из сторон каждой клетки, конечный сегмент завершает линию или ряд.
def horizontal_segment():
    print('+' + ('  -' * SPACE_BEFORE_MINUS ) + '  ', end=' ')
def horizontal_segment_end():
    print('+' + ('  -' * SPACE_BEFORE_MINUS ) + '  +', end=' ')


def vertical_segment():
    print('|' + (' ' * SPACE_BEFORE_VERT), end=' ')
def vertical_segment_end():
    print('|' + (' ' * SPACE_BEFORE_VERT) + '|', end=' ')



# Линия - создаёт линию из сегментов заданной длинны, завершая конечным сегментом
def horizontal_line(arg = 2):
    arg = arg - 1
    for i in range(arg):
        horizontal_segment()
    horizontal_segment_end()

def vertical_line(arg = 2):
    arg = arg - 1
    for i in range(arg):
        vertical_segment()
    vertical_segment_end()


# Сегмент сетки рисует один ряд из горизонтальных и вертикальных линий заданной длинны
def grid_segment(arg = 2):
    horizontal_line(arg)
    print()
    for i in range(4):
        vertical_line(arg)
        print()


# основная программа, в цыкле рисует сетку из сегментов сеити, завершая нижней горизонтальной линией.
def net_painter(arg = 1):
    for i in range(arg):
        grid_segment(arg)
    horizontal_line(arg)


def main():

    net_painter(1)

if __name__ == '__main__':
    main()