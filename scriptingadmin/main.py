import argparse
import time

from ScriptAdmin import *

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interval", help='nombre_de_secondes', type=float)

# Parse and print the results
args = parser.parse_args()
a = True
if args.interval:
    print("Fetching data...")
    while a:
        try:
            metrics()
            time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nStopping program...")
            a = False
