
def string_split(str):
    """
        Will split a string for each char and put them in an array
    Args:
        str: a string to split

    Returns: the array with a char in each cell

    """
    return [char for char in str]


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