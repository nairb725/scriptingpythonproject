def split(str):
    """
        that will split element and put them in an array
    Args:
        str: User's input

    Returns: array with user's split input

    """
    return [char for char in str]


def to_ascii(char):
    """
        we are going to convert those letters with a ascii tab
    Args:
        char: tab with letters

    Returns: tab with letters converted with ascii tab

    """
    return ord(char)


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
    return [bin(char) for char in split(value)]


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
    will put if its need O to complete the last element
    Args:
        arr: an array with base 64 elements

    Returns: an array with base 64 elements completed

    """
    return arr


def bin_to_ascii(arr):
    """
    we convert array with base 64 elements to base 10
    Args:
        arr: an array with base 64 elements

    Returns: an array with base 10 elements

    """
    return arr


def to_char(arr):
    """
    we match numbers with the ascii tab
    Args:
        arr: an array with base 10 elements

    Returns:  an array with ascii's letters

    """
    return arr


def refill_string(str):
    """
    will add "=" as many as we need to have a 8 multiple at the end for the string
    Args:
        str: an array with ascii's letters

    Returns: string of base 64 letter 

    """
    return str


# Taking an input values from user
values = input("Enter the Values: ")

# Driver code
print(split(values))
print(binary(values))
print(byte(values))
