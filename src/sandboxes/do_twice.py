def main():

    def print_value(arg):
        print(arg)

    def print_twice(arg):
        print(arg)
        print(arg)

    def do_twice(func, arg):
        func(arg)
        func(arg)

    def do_four(func, arg):
        for i in range(4):
            func(arg)

    do_four(print_value, 'spam')


if __name__ == '__main__':
    main()