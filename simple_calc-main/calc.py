import math


def add(a, b):
    return (a + b)


def sub(a, b):
    return (a - b)


def mul(a, b):
    return (a * b)


def div(a, b):
    return (a / b)


def display_calc():
    print('The best calculator')

    print('CHOICES')
    print('1.add \t 2.subtract \n 3.divide \t 4.multiplication \n 5.Squareroot')
    choice = input('Enter choice: ')

    f_number = input("Enter number: ")
    f_number = int(f_number)
    s_number = input("Enter second number: ")
    s_number = int(s_number)

    if choice == '1':
        add_func = add(f_number, s_number)
        print(add_func)

    elif choice == '2':
        sub_func = sub(f_number, s_number)
        print(sub_func)

    elif choice == '3':
        div_func = div(f_number, s_number)
        print(div_func)

    elif choice == '4':
        mul_func = mul(f_number, s_number)
        print(mul_func)

    elif choice == '5':
        number = int(input("Enter number: "))
        square_root = math.sqrt(number)
        print(square_root)
    else:
        print('Read the manual: choice not           avavailble')


display_calc()