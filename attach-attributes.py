#!/usr/bin/python

import sys
import argparse

sys.path.append('./')

from src.utils.read_csv import read_csv
from src.utils.list_to_dict import list_to_dict
from src.utils.map_to_list_csv import map_to_list_csv
from src.gephi.write_csv import write_csv

print("")
print("-----------------------------")
print("Attach attributes")
print("-----------------------------")
print("")

parser = argparse.ArgumentParser(description="Attaches further attributes to a given attributes CSV")
required_parser = parser.add_argument_group('required named arguments')
required_parser.add_argument("--attributes-file", dest="attrs", help="Attributes, a given file with attributes for Gephi", required=True)
required_parser.add_argument("--expartners-file", dest="expartners", help="File containing a list of names that used to be partners", required=True)
required_parser.add_argument("--zebra-file", dest="zebra", help="File containing an export of Zebra", required=True)

args = parser.parse_args()

attributes_file = args.attrs
expartners_file = args.expartners
zebra_file = args.zebra

print("Reading source files...")

attributes_raw = read_csv(attributes_file)
attributes = list_to_dict(attributes_raw[1:])

expartners = read_csv(expartners_file)[1:]
zebra_file = read_csv(zebra_file)[1:]

print("Normalizing Zebra export...")
zebra_list = dict()
for entry in zebra_file:
    name = entry[2] + " " + entry[1]
    startdate = entry[6]
    location = entry[4]
    zebra_list[name] = [startdate, location]

print("Attach expartner flag and start date...")

for name, person_attributes in attributes.items():
    person_attributes.append(1 if [name] in expartners else 0)
    if name in zebra_list:
        person_attributes.append(zebra_list[name][0])
        person_attributes.append(zebra_list[name][1])
    else:
        person_attributes.append("")
        person_attributes.append("")

print("Write to original attributes CSV...")

attributes_csv = map_to_list_csv(attributes, ['Name', 'Roles', 'Is ex-partner', 'Start date', 'Location'])
write_csv(attributes_csv, attributes_file)

print("All done!")
