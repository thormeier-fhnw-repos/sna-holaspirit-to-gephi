#!/bin/bash

print ":: ============================="
print ":: Holaspirit to Gephi toolchain"
print ":: ============================="
print "::"
./holaspirit-to-gephi.py --anonymize --source-file=data/raw/export_holaspirit.csv --target-file=data/gephi-ready/relations.csv
./holaspirit-roles-gephi-attributes.py --source-file=data/raw/export_holaspirit.csv --target-file=data/gephi-ready/attributes.csv
./attach-attributes.py --attributes-file=data/gephi-ready/attributes.csv --expartners-file=data/raw/expartners.csv --zebra-file=data/raw/export_zebra.csv
./anonymize-attributes.py --attributes-file=data/gephi-ready/attributes.csv --person-file=anonymize_map.csv

rm anonymize_map.csv
