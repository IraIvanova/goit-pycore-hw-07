from exceptions import AddressBookError


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AddressBookError as e:
            return str(e)

    return inner