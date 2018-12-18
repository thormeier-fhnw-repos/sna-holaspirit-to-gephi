# Holaspirit to Gephi converter

This python app takes a CSV export of the members/roles list of Holaspirit and transforms it into a Gephi-friendly
CSV format. **Requires Python >= 3**

## holaspirit-to-gephi.py

### Data model

This app creates a one-mode network with bi-directional edges and people as nodes. A relation bewteen two 
nodes can either be

 * same role
 * same circle

#### How the network is generated

First, the application creates two matrices:

 1. A matrix with weighted relations for same **roles**
 2. A matrix with weighted relations for same **circles**

These two matrices are then combined: Another empty matrix is created (all weights **0**) and the values of the other 
two matrices are added.

#### Weights

The weight of the edges is determined as follows:

 * **0**: No relation, i.e. no edge present
 * **+ 0.5**: Same role, that is not Lead Link or Rep Link.
 * **+ 1.0**: Same role, both nodes are either Lead links or Rep Links or any combination (Lead and Rep Links tend to 
 communicate more often through higher circles and are therefore of more influence)
 * **+ 1.0**: Same circle (People working together closely)
 * **+ 1.5**: Lead and Rep Link of same circle (Lead Link assigns roles within circle, Rep Link represents circle in 
 upper circle)

#### Calculation examples

* Alice and Bob are both Developers, but in different circles: **0.5**
* Alice and Bob are both UX specialist and Developer, but in different circles: **0.5 * 2 roles = 1.0**
* Alice is Developer, Bob is UX specialist, they are in the same circle: **1.0**
* Alice and Bob are both Developers in the same circle: **1.0 (circle) + 0.5 (same roles) = 1.5**
* Alice is Lead Link, Bob is Rep Link, they are in different circles: **1.0**
* Alice is Lead Link, Bon is Rep Link, they are in the same circle: **1.0 (same circle) + 1.5 (Lead and Rep  Link of same circle) = 2.5**
* Alice and Bob are Lead and Rep Link of three different circles: **2.5 * 3 circles = 7.5**
* Alice is Rep Link, Bob is UX specialist, they are in the same circle: **From A to B: 1.5, from B to A: 1.0**

#### Edge/node attributes

This application does not add attributes for nodes or edges.

### Usage

As per `--help`:

```
usage: holaspirit-to-python.py [-h] [--anonymize] --source-file SOURCE_FILE
                               --target-file TARGET_RELATIONS

Convert an export of roles and circles of Holaspirit to Gephi CSV

optional arguments:
  -h, --help            show this help message and exit
  --anonymize           Determines if the names of people should be anonymized

required named arguments:
  --source-file SOURCE_FILE
                        Source file: The Holaspirit CSV export
  --target-file TARGET_RELATIONS
                        Target file for relations
```

#### Source and target

The source file can be specified via `--source-file` parameter. The file needs to be in CSV format, i.e. a direct export 
from Holaspirit (which is .xlsx) converted to CSV.

The target file (i.e. the CSV being generated) can be specified via `--target-file` parameter. This target file will 
contain a matrix with values. Values **> 0** mean that there's a weighted relation, values **== 0** mean that there's 
no relation.

#### Anonymizing the data

In some use cases, it may be necessary to anonymize the data. If an anonymization is necessary, it can be achieved by 
passing the `--anonymize` flag. This will also create a file `anonymize_map.csv` which contains the clear text names and 
their respective anonymized tokens. A token will look like such: `Person #123` whereas `123` is the index of 
encountering.


#### Usage example

To load an export from the file `../export.csv` and write it into `../network.csv`, anonymized, execute the following 
command:

```bash
./holaspirit-to-gephi.py --source-file=../export.csv --target-file=../network.csv --anonymize
```

## holaspirit-roles-gephi-attributes.py

Creates a CSV file of names mapped to a list of rows.

### Usage

```
usage: holaspirit-roles-gephi-attributes.py [-h] --source-file SOURCE_FILE
                                            --target-file TARGET_ATTRIBUTES

Convert an export of roles and circles of Holaspirit to Gephi attributes CSV

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  --source-file SOURCE_FILE
                        Source file: The Holaspirit CSV export
  --target-file TARGET_ATTRIBUTES
                        Target file for attributes

```

## attach-attributes.py

Attaches further attributes (if ex partner and start date of person) to the attributes CSV file 
created with `holaspirit-roles-gephi-attributes.py`

### Usage

```
usage: attach-attributes.py [-h] --attributes-file ATTRS --expartners-file
                            EXPARTNERS --zebra-file ZEBRA

Attaches further attributes to a given attributes CSV

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  --attributes-file ATTRS
                        Attributes, a given file with attributes for Gephi
  --expartners-file EXPARTNERS
                        File containing a list of names that used to be
                        partners
  --zebra-file ZEBRA    File containing an export of Zebra
```

## anonymize-attributes.py

Anonymizes all attributes: Replaces names in an attributes CSV file with a given map of names to tokens.

### Usage

```
usage: anonymize-attributes.py [-h] --attributes-file ATTRS --person-file
                               PERSONS

Anonymizes a given attributes CSV

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  --attributes-file ATTRS
                        Attributes, a given file with attributes for Gephi
  --person-file PERSONS
                        Personss, a list of persons and their anonymized
                        tokens
```

## Glueing things together: toolchain.sh

Executes all commands consectuively. The following files need to be present:

 * data/raw/export.csv (Holaspirit export CSV)
 * data/raw/expartners.csv (List of names that used to be partners)
 * data/raw/startdates.csv (List of names and their startdates)
 
The following files will be created:

 * data/gephi-ready/relations.csv
 * data/gephi-ready/attributes.csv

The complete toolchain can be executed via `./toolchain.sh`

## Disclaimer

This application serves educational purpose only and is developed by Nelson Abplanalp and Pascal Thormeier.

It is distributed under the MIT license.
