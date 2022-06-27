def split(str):
    """
        that will split element and put them in an array
    Args:
        str: 

    Returns:

    """
    return [ord(char) for char in str]


def binary(value):
    """

    Args:
        value:

    Returns:

    """
    value = split(value)
    return [bin(char) for char in value]


def to_base64(arr):
    """
        we are going to convert octet in base 64
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


# Taking an input values from user
values = input("Enter the Values: ")

# Driver code
print(split(values))
print(binary(values))
