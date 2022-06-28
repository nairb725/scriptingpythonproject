from EncodeCommon import *


def to_string(base64):
    """
        decode a string to base64
    Args:
        base64: the string value

    Returns: the string user value

    """
    return


def binary(str):
    """
        that will put user's elements in a string
    Args:
        str: string with user's input

    Returns: string with user's elements

    """
    return


def remove_equal(str):
    """
        if there is an "=" go delete it
    Args:
        str: string with user's input maybe with equal

    Returns: string with user's input without equal

    """
    return


def array(arr):
    """
        put all element in an array
    Args:
        arr: string with user's input without equal

    Returns: array with user's elements

    """
    return


def alphabet(arr):
    """
       match the numbers with the alphabet
    Args:
        arr: array with user's elements

    Returns: array with user's elements

    """
    return


def binary(arr):
    """
        convert numbers into binary mode
    Args:
        arr: array with user's elements

    Returns: array with user's binary numbers

    """
    return


def add(arr):
    """
        if character is not equal to 6 add 0 at the beginning
    Args:
        arr:  array with user's binary numbers

    Returns:  array with user's binary numbers with added 0

    """
    return


def one_string(arr):
    """
        will contains all elements in 1 string
    Args:
        arr:  array with user's binary numbers with added 0

    Returns:  one string with all elements

    """
    return


def divide_in_eight_part(arr):
    """
        will divide them in part with 8 elements each
    Args:
        arr: one string with all elements

    Returns:  an array with eight element in each part

    """
    return


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

