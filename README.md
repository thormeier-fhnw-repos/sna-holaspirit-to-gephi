# Holaspirit to Gephi converter

This Python script takes a CSV Export of the members/roles list of Holaspirit and transforms it into a Gephi-friendly 
CSV format.

## Data model

This script creates two one-mode networks with bi-directional edges and people as nodes. There's two different kinds 
edges: Same role and same circle.

## Usage

First, download the MS Excel export from the "Members" part of your Holaspirit instance. The first sheet, "Members" now 
has to be exported to CSV. This will be the data source. As delimiters, Commas (`,`) are used, the quote char is double 
quotes (`"`).

There's two mandatory parameters, the `--source-file` parameter determines which file to load the data from, the 
`--target-roles-file` and `--target-circles-file` parameters determine which file the new data will be written into.

```bash
./holaspirit-to-python.py --source-file=file-to-load.csv --target-roles-file=file-to-write-roles-replationship.csv --target-circles-file=file-to-write-circles-replationship.csv
```

After the script finished execution,

## Anonymize the data

If you want the data to be anonymous, i.e. for presentations or school work, you can provide the `--anonymize` flag:

```bash
./holaspirit-to-python.py --source-file=file-to-load.csv --target-roles-file=file-to-write-roles-replationship.csv --target-circles-file=file-to-write-circles-replationship.csv --anonymize
``` 

All people names will then be replaced by a number that is incremented. The number is determined by first encounter,
i.e. the first person name the script encounters will be `1`, the second `2`and so on.
