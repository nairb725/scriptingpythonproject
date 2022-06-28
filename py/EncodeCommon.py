
def string_split(str):
    """
        that will split element and put them in an array
    Args:
        str: User's input

    Returns: array with user's split input

    """
    return [char for char in str]


def elts_to_ascii(arr):
    """
        we are going to convert those letters with a ascii tab
    Args:
        arr: tab with letters

    Returns: tab with letters converted with ascii tab

    """
    return [ord(char) for char in arr]


def array_to_string(arr):
    """
        will pul all the element in one string
    Args:
        arr: tab with octet numbers

    Returns: all the octet in one string

    """
    str = ""
    for i in arr:
        str += i

    return str