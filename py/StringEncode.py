from math import ceil


def to_base64(str):
    """
        encode a string to base64
    Args:
        str: the string value

    Returns: the string base64 value

    """
    step_1 = split(str)
    step_2 = to_ascii(step_1)
    step_3 = binary(step_2)
    step_4 = make_octet(step_3)
    step_5 = to_string(step_4)
    step_6 = cut_bin_6char(step_5)
    step_7 = refill_arr(step_6)
    step_8 = bin_to_base10(step_7)
    step_9 = to_char(step_8)
    step_10 = to_string(step_9)
    step_11 = refill_string(step_10)
    return step_11


def split(str):
    """
        that will split element and put them in an array
    Args:
        str: User's input

    Returns: array with user's split input

    """
    return [char for char in str]


def to_ascii(arr):
    """
        we are going to convert those letters with a ascii tab
    Args:
        arr: tab with letters

    Returns: tab with letters converted with ascii tab

    """
    return [ord(char) for char in arr]


def binary(arr):
    """
        we are going convert this numbers in binary
    Args:
        arr: tab with letters converted with ascii tab

    Returns: tab with binary numbers

    """
    return [str(bin(int(char)))[2:] for char in arr]


def make_octet(arr):
    """
        convert them in octet by adding if you need 0 at the beginning
    Args:
        arr: tab with binary numbers

    Returns: tab with octet numbers

    """
    return [char.zfill(8) for char in arr]


def to_string(arr):
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


def cut_bin_6char(str):
    """
        we are going to convert octet in base 64 and put all the elements in an array
    Args:
        str: we convert the octet in base 64 with 6 characters per elements

    Returns: return an array with base 64 elements

    """
    arr = []
    n = 6  # the index to cut the string for the base64

    # split the whole string into string of 6 character each
    for index in range(0, len(str), n):
        arr.append(str[index: index + n])

    return arr


def refill_arr(arr):
    """
        will put if its need O to complete the last element
    Args:
        arr: an array with base 64 elements

    Returns: an array with base 64 elements completed

    """
    return [char.zfill(6) for char in arr]


def bin_to_base10(arr):
    """
        we convert array with base 64 elements to base 10
    Args:
        arr: an array with base 64 elements

    Returns: an array with base 10 elements

    """
    return [int(char, 2) for char in arr]


def to_char(arr):
    """
        we match numbers with the ascii tab
    Args:
        arr: an array with base 10 elements

    Returns: an array with ascii's letters

    """
    return [chr(char + 65) for char in arr]


def refill_string(str):
    """
        will add "=" as many as we need to have a 8 multiple at the end for the string
    Args:
        str: an array with ascii's letters

    Returns: string of base 64 letter

    """
    return str.ljust(ceil(len(str)/8)*8, "=")
