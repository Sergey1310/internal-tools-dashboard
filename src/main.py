def main():

    def right_justify(text):
        length = len(text)
        return (' ' * (70 - length)) + text

    print(right_justify("Hello World"))

if __name__ == "__main__":
    main()
