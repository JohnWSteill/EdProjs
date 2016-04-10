#!/usr/bin/env python
import sys
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="return square", type=int)
parser.add_argument("--verbose", help="verbose option", action="store_true")
parser.add_argument("--cube", help="optional cube", type=int)
args = parser.parse_args()
print args.square**2
if args.verbose:
    print("Verbose style!")
if args.cube:
    print(args.cube**3)
