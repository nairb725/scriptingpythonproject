import argparse

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interval", help='nombre_de_secondes')

# Parse and print the results
args = parser.parse_args()
if args.interval:
    print("script ok")

