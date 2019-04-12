def show_pyramid(num):
    if num > 0:
        for n in range(num):
            print('*'*n)
    else:
        for n in range(abs(num), 0, -1):
            print('*'*(n-1))


def main():
    show_pyramid(10)

    show_pyrami(-10)


if __name__ == '__main__':
    main()
