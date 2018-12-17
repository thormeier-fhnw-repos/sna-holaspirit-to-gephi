#!/usr/bin/python

import sys
import argparse

sys.path.append('./')

from src.utils.read_csv import read_csv
from src.utils.map_to_list_csv import map_to_list_csv

from src.holaspirit.get_distinct_rows import get_distinct_rows
from src.holaspirit.create_person_roles_map import create_person_roles_map

from src.gephi.write_csv import write_csv

print("")
print("-----------------------------")
print("Holaspirit roles to gephi attributes")
print("-----------------------------")
print("")

parser = argparse.ArgumentParser(description="Convert an export of roles and circles of Holaspirit to Gephi attributes CSV")
required_parser = parser.add_argument_group('required named arguments')
required_parser.add_argument("--source-file", dest="source_file", help="Source file: The Holaspirit CSV export", required=True)
required_parser.add_argument("--target-file", dest="target_attributes", help="Target file for attributes", required=True)

args = parser.parse_args()

source = args.source_file
target_attributes = args.target_attributes

# Source file and some stats

print("Reading source file", source)
data_raw = read_csv(source)
print("  - Number of rows read:", len(data_raw) - 1)

print("Identifying distinct nodes")
persons = get_distinct_rows(data_raw, lambda row: row[0] + " " + row[1], lambda value: len(value) > 1)
print("  - Number of persons, i.e. nodes:", len(persons))

print("Mapping persons to rows")
persons_role_map = create_person_roles_map(data_raw)

print("Writing attributes to CSV at " + target_attributes + "...")
person_role_map_csv = map_to_list_csv(persons_role_map, ("Name", "Roles"))
write_csv(person_role_map_csv, target_attributes)

print("All done!")
