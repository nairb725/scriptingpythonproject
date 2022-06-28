from EncodeCommon import *


def to_string(base64):
    """
        decode a string to base64
    Args:
        base64: the string value

    Returns: the string user value

    """
    step_1 = remove_equal(base64)
    step_2 = string_split(step_1)
    step_3 = elts_to_ascii(step_2)
    step_4 = make_octet(step_3)
    step_5 = array_to_string(step_4)
    step_6 = cut_bin_6char(step_5)
    step_7 = refill_arr(step_6)
    step_8 = bin_to_base10(step_7)
    step_9 = to_char(step_8)
    step_10 = array_to_string(step_9)
    step_11 = array_to_string(step_10)
    return step_11


def remove_equal(str):
    """
        if there is an "=" go delete it
    Args:
        str: string with user's input maybe with equal

    Returns: string with user's input without equal

    """
    return str


def array(arr):
    """
        put all element in an array
    Args:
        arr: string with user's input without equal

    Returns: array with user's elements

    """
    return arr


def binary(arr):
    """
        convert numbers into binary mode
    Args:
        arr: array with user's elements

    Returns: array with user's binary numbers

    """
    return arr


def add(arr):
    """
        if character is not equal to 6 add 0 at the beginning
    Args:
        arr:  array with user's binary numbers

    Returns:  array with user's binary numbers with added 0

    """
    return arr


def one_string(arr):
    """
        will contains all elements in 1 string
    Args:
        arr:  array with user's binary numbers with added 0

    Returns:  one string with all elements

    """
    return arr


def divide_in_eight_part(arr):
    """
        will divide them in part with 8 elements each
    Args:
        arr: one string with all elements

    Returns:  an array with eight element in each part

    """
    return arr


def remove_zero(arr):
    """
      if there a 0 at the beginning remove it
    Args:
        arr:  array with user's binary numbers

    Returns:  array with user's binary numbers without 0

    """

    return arr.replace("0", "")


def ascii(arr):
    """
        convert binary numbers in ascii numbers
    Args:
        arr:  array with user's binary numbers

    Returns: array with ascii numbers

    """
    return arr.decode()


def alphabet(arr):
    """
        convert ascii numbers in alphabet
    Args:
        arr: array with ascii numbers

    Returns: array with alphabet letters

    """
    return [(ord(char) - 65) for char in arr]


def byte(str):
    """
        put elements in one string
    Args:
        arr: array with alphabet letters

    Returns: string with user's result

    """
    str = ""
    for i in arr:
        str += i

    return str

