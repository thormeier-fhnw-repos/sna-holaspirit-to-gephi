#!/usr/bin/python

import sys
import argparse

sys.path.append('./')

from src.utils.list_to_dict import list_to_dict
from src.utils.read_csv import read_csv
from src.utils.map_to_list_csv import map_to_list_csv

from src.gephi.write_csv import write_csv

print("")
print("-----------------------------")
print("Anonymize attributes")
print("-----------------------------")
print("")

parser = argparse.ArgumentParser(description="Anonymizes a given attributes CSV")
required_parser = parser.add_argument_group('required named arguments')
required_parser.add_argument("--attributes-file", dest="attrs", help="Attributes, a given file with attributes for Gephi", required=True)
required_parser.add_argument("--person-file", dest="persons", help="Personss, a list of persons and their anonymized tokens", required=True)

args = parser.parse_args()

attributes_file = args.attrs
persons_file = args.persons

print("Reading attributes file...")
attributes_raw = read_csv(attributes_file)
attributes = list_to_dict(attributes_raw[1:])

print("Reading persons file...")
persons = list_to_dict(read_csv(persons_file)[1:])

print("Anonymizing...")

anonymized_attributes = list()
for key, value in attributes.items():
    name = persons[key][0]
    row = value
    row.insert(0, name)
    anonymized_attributes.append(row)

print("Write anonymized attributes to attributes file again")

anonymized_attributes.insert(0, attributes_raw[0])
write_csv(anonymized_attributes, attributes_file)

print("All done!")
