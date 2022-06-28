from py.EncodeCommon import *


def to_string(base64):
    """
        decode a string to base64
    Args:
        base64: the string value

    Returns: the string user value

    """
    step_1 = remove_equal(base64)
    print(step_1)
    step_2 = string_split(step_1)
    print(step_2)
    step_3 = index_in_alphabet(step_2)
    print(step_3)
    step_bonus = binary(step_3)
    print(step_bonus)
    step_4 = fill_with_zero(step_bonus)
    print(step_4)
    step_5 = array_to_string(step_4)
    print(step_5)
    step_6 = divide_in_eight_part(step_5)
    print(step_6)
    step_7 = remove_last_element(step_6)
    print(step_7)
    step_8 = remove_first_zero(step_7)
    print(step_8)
    step_9 = to_ascii(step_8)
    print(step_9)
    step_bonus_2 = to_alphabet(step_9)
    print(step_bonus_2)
    step_10 = array_to_string(step_bonus_2)
    return step_10


def remove_equal(str):
    """
        if there is an "=" go delete it
    Args:
        str: string with user's input maybe with equal

    Returns: string with user's input without equal

    """
    return str.replace("=", "")


def index_in_alphabet(arr):
    """
        convert ascii numbers in alphabet
    Args:
        arr: array with ascii numbers

    Returns: array with alphabet letters

    """
    return [(ord(char) - 65) for char in arr]


def fill_with_zero(arr):
    """
        if character is not equal to six add zero at the beginning
    Args:
        arr:  array with user's binary numbers

    Returns:  array with user's binary numbers with added zero

    """
    return [char.zfill(6) for char in arr]


def divide_in_eight_part(str):
    """
        will divide them in part with eight elements each
    Args:
        arr: one string with all elements

    Returns:  an array with eight element in each part

    """
    arr = []
    n = 8  # the index to cut the string for the base64

    # split the whole string into string of 6 character each
    for index in range(0, len(str), n):
        arr.append(str[index: index + n])

    return arr


def remove_last_element(arr):
    """
      if there an element at the end it will remove it
    Args:
        arr:  array with user's binary numbers

    Returns:  array with user's binary numbers without the last element

    """
    if arr[len(arr) - 1] != 8:
        arr.pop()
    return arr


def remove_first_zero(arr):
    """
      if there an zero at the beginning it will remove it
    Args:
        arr:  array with user's binary numbers

    Returns:  array without zero

    """

    return [char.replace("0", "", 1) for char in arr]


def to_ascii(arr):
    """
        convert binary numbers in ascii numbers
    Args:
        arr:  array with user's binary numbers

    Returns: array with ascii numbers

    """
    return arr.decode()


def to_alphabet(arr):
    """
    convert ascii numbers into letters
    Args:
        arr: array with ascii numbers

    Returns: array with alphabet letters

    """
    return [chr(char) for char in arr]
