#!/usr/bin/python

import sys
import argparse

sys.path.append('./')

print("")
print("-----------------------------")
print("Attach attributes")
print("-----------------------------")
print("")

parser = argparse.ArgumentParser(description="Attaches further attributes to a given attributes CSV")
required_parser = parser.add_argument_group('required named arguments')
required_parser.add_argument("--attributes-file", dest="attrs", help="Attributes, a given file with attributes for Gephi", required=True)
required_parser.add_argument("--expartners-file", dest="expartners", help="File containing a list of names that used to be partners", required=True)
required_parser.add_argument("--startdates-file", dest="startdates", help="File containing a list of all start dates of all names", required=True)

args = parser.parse_args()

attributes_file = args.attrs
expartners_file = args.expartners
startdates_file = args.startdates

print("Reading source files...")

attributes = read_csv(attributes_file)
expartners = read_csv(expartners_file)
startdates = read_csv(startdates_file)

print(attributes)

