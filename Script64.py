def split(str):
    return [ord(char) for char in str]


def binary(values):
    values = split(values)
    return [bin(char) for char in values]


"""
Transform the octet list to a base64 friendly list
"""


def toBase64(arr):
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
