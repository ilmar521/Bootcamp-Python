
def divide_func():
    try:
        x = 5 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")

divide_func()
