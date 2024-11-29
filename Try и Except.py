def add_everything_up(a, b):

    if isinstance(a, str) or isinstance(b, str):
        return str(a) + str(b)

    try:

        return a + b
    except TypeError:

        print(f"Cannot add {type(a).__name__} and {type(b).__name__}")
        return None

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

