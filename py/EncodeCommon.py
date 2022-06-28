
def string_split(str):
    """
        Will split a string for each char and put them in an array
    Args:
        str: a string to split

    Returns: the array with a char in each cell

    """
    return [char for char in str]


def elts_to_ascii(arr):
    """
        Convert all char in the array to its equivalent in ascii
    Args:
        arr: list with char

    Returns: tab with ascii value

    """
    return [ord(char) for char in arr]


def array_to_string(arr):
    """
        Put all the element of an array in one string
    Args:
        arr: tab with string in each cell

    Returns: the recompose string

    """
    str = ""
    for i in arr:
        str += i

    return str