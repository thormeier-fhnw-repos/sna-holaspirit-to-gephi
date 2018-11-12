#!/usr/bin/python

import sys

sys.path.append('./')

from src.utils.error import error
from src.utils.get_parameter import get_parameter
from src.utils.read_csv import read_csv

from src.holaspirit.get_circle import get_circle
from src.holaspirit.get_role import get_role
from src.holaspirit.get_person_dict import get_person_dict
from src.holaspirit.get_distinct_rows import get_distinct_rows
from src.holaspirit.match_persons import match_persons

from src.gephi.build_matrix import build_matrix
from src.gephi.write_csv import write_csv

print("")
print("-----------------------------")
print("Holaspirit to Gephi converter")
print("-----------------------------")
print("")

source = get_parameter("source-file")
target_roles = get_parameter("target-roles-file")
target_circles = get_parameter("target-circles-file")
anonymize = True if get_parameter("anonymize") is not None else False

if source is None:
    error("Please provide a file to read.")

if target_roles is None:
    error("Please provide a target file name for the roles relationship CSV.")

if target_circles is None:
    error("Please provide a target file name for the circles relationship CSV.")

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

# Actually creating a bit of structure

print("Creating roles relationship structure")
print("  - Matching persons with their roles...")
persons_with_roles = get_person_dict(data_raw, get_role)
print("  - Number of assigned roles in total:", sum([len(roles) for persons,roles in persons_with_roles.items()]))
print("  - Matching persons that have same roles")
relations_roles = match_persons(persons_with_roles, lambda value: 2 if value == "Lead Link" or value == "Rep Link" else 1)
print("  - Number of found relations:", len(relations_roles))

print("Creating circles relationship structure")
print("  - Matching persons with their circles...")
persons_with_circles = get_person_dict(data_raw, get_circle)
print("  - Number of assigned circles in total:", sum([len(circles) for persons,circles in persons_with_circles.items()]))
print("  - Matching persons that have same circles")
relations_circles = match_persons(persons_with_circles, lambda value: 1)
print("  - Number of found relations:", len(relations_circles))

# Building matrices

print("Creating matrix for persons matched by their roles...")
roles_matrix = build_matrix(persons, relations_roles, anonymize)

print("Creating matrix for persons matched by their circles...")
circles_matrix = build_matrix(persons, relations_circles, anonymize)

# Writing matrices to CSV
print("Writing roles matrix to ", target_roles, "...")
write_csv(roles_matrix, target_roles)

print("Writing circles matrix to ", target_circles, "...")
write_csv(circles_matrix, target_circles)

print("All done!")
