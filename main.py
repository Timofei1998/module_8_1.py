def add_everything_up(a, b):
    try:
        add = a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return float(a) + float(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))