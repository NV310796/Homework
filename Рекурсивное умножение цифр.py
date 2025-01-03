from itertools import count


def get_multiplied_digits(number):
    if number == 0:
        number = 1
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return number
    elif number != '':
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(52525))
print(get_multiplied_digits(8))
print(get_multiplied_digits(40203))
print(get_multiplied_digits(402030))



