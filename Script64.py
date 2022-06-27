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


def binary(value):
    """
    we are going convert this numbers in binary
    Args:
        value: tab with letters converted with ascii tab

    Returns: tab with binary numbers

    """
    return [bin(char) for char in split(value)]


def byte(value):
    """
    convert them in octet by adding if you need 0 at the beginning
    Args:
        value: tab with binary numbers

    Returns: tab with octet numbers

    """
    return [bytes(char) for char in binary(value)]


def to_string(arr):
    """
    will pul all the element in one string
    Args:
        arr: tab with octet numbers

    Returns: all the octet in one string

    """
    return


def to_base64(arr):
    """
        we are going to convert octet in base 64 and put all the elements in an array
    Args:
        arr: we convert the octet in base 64 with 6 characters per elements

    Returns: return an array with base 64 elements

    """
    return_arr = []
    str = ""  # the global string
    n = 6  # the index to cut the string for the base64

    for i in arr:
        str += i

    # split the whole string into string of 6 character each
    for index in range(0, len(str), n):
        return_arr.append(str[index: index + n])

    return return_arr


def refill_arr(arr):
    """

    Args:
        arr:

    Returns:

    """
    return arr


def bin_to_ascii(arr):
    """

    Args:
        arr:

    Returns:

    """
    return arr


def to_char(arr):
    """

    Args:
        arr:

    Returns:

    """
    return arr


def refill_string(str):
    """

    Args:
        str:

    Returns:

    """
    return str


# Taking an input values from user
values = input("Enter the Values: ")

# Driver code
print(split(values))
print(binary(values))
print(byte(values))
