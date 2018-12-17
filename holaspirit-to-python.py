#!/usr/bin/python

import sys
import argparse

sys.path.append('./')

from src.utils.error import error
from src.utils.read_csv import read_csv
from src.utils.anonymize import anonymize
from src.utils.map_to_list_csv import map_to_list_csv

from src.holaspirit.get_circle import get_circle
from src.holaspirit.get_role import get_role
from src.holaspirit.get_person_dict import get_person_dict
from src.holaspirit.get_distinct_rows import get_distinct_rows
from src.holaspirit.match_persons import match_persons

from src.gephi.build_matrix import build_matrix
from src.gephi.combine_matrices import combine_matrices
from src.gephi.write_csv import write_csv

print("")
print("-----------------------------")
print("Holaspirit to Gephi converter")
print("-----------------------------")
print("")

# Arguments

parser = argparse.ArgumentParser(description="Convert an export of roles and circles of Holaspirit to Gephi CSV")
parser.add_argument("--anonymize", dest="anonymize", default=False, action="store_true", help="Determines if the names of people should be anonymized")

required_parser = parser.add_argument_group('required named arguments')
required_parser.add_argument("--source-file", dest="source_file", help="Source file: The Holaspirit CSV export", required=True)
required_parser.add_argument("--target-file", dest="target_relations", help="Target file for relations", required=True)

args = parser.parse_args()

source = args.source_file
target_relations = args.target_relations
should_anonymize = args.anonymize

# Source file and some stats

print("Reading source file", source)
data_raw = read_csv(source)
print("  - Number of rows read:", len(data_raw) - 1)

print("Identifying distinct nodes")
persons = get_distinct_rows(data_raw, lambda row: row[0] + " " + row[1], lambda value: len(value) > 1)
print("  - Number of persons, i.e. nodes:", len(persons))

print("Identifying distinct roles")
roles = get_distinct_rows(data_raw, get_role, lambda value: True)
print("  - Number of distinct roles:", len(roles))

print("Identifying distinct circles")
circles = get_distinct_rows(data_raw, get_circle, lambda value: True)
print('  - Number of distinct circles:', len(circles))


# Anonymize

person_name_map = anonymize(persons, should_anonymize)
anonymized_persons = list(person_name_map.values())


# Actually creating a bit of structure

print("Creating roles relationship structure")
print("  - Matching persons with their roles...")
persons_with_roles = get_person_dict(data_raw, person_name_map, get_role)
print("  - Number of assigned roles in total:", sum([len(roles) for persons, roles in persons_with_roles.items()]))
print("  - Matching persons that have same roles")
relations_roles = match_persons(persons_with_roles, lambda value: 1 if value == "Lead Link" or value == "Rep Link" else 0.5)
print("  - Number of found relations:", len(relations_roles))

print("Creating circles relationship structure")
print("  - Matching persons with their circles...")
persons_with_circles = get_person_dict(data_raw, person_name_map, get_circle)
print("  - Number of assigned circles in total:", sum([len(circles) for persons, circles in persons_with_circles.items()]))
print("  - Matching persons that have same circles")
relations_circles = match_persons(persons_with_circles, lambda value: value[1])
print("  - Number of found relations:", len(relations_circles))


# Building matrices

print("Creating matrix for persons matched by their roles...")
roles_matrix = build_matrix(anonymized_persons, relations_roles)

print("Creating matrix for persons matched by their circles...")
circles_matrix = build_matrix(anonymized_persons, relations_circles)


# Combining matrices

relations_matrix = combine_matrices(roles_matrix, circles_matrix, anonymized_persons)


# Writing matrices to CSV

print("Writing relations matrix to ", target_relations, "...")
write_csv(relations_matrix, target_relations)

if should_anonymize:
    print("Should anonymize: Writing a map to anonymize_map.csv...")
    person_name_list = map_to_list_csv(person_name_map, ("Clear text", "Anonymized"))
    write_csv(person_name_list, "anonymize_map.csv")

print("All done!")
