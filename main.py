from py.StringDecode import *
from py.StringEncode import *
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("Base64")
parser.add_subparsers("encode", "decode")
#group.add_argument("-S", "-f")

# subparsers = parser.add_subparsers("encode", "decode")

# Taking an input values from user
# values = input("Enter the Values: ")

# print(to_base64(values))
