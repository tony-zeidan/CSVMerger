# CSVMerger

CSVMerger is a simple package that contains functions for the merging of csv files.
This package also includes a console script that can be used.


Note: This package relies on Pandas, and the majority of its functions are wrappers for functions in the Pandas distribution.

## Command Line Usage
Once installed properly, the user can start the console script.

```bash
csv-merger <input directory of csv files> <output path> [options]
```
For help with the script run:
```bash
csv-merger --help
```

## Functions Usage
The user can also import the package and use its functions.

```python
from csvmerger.merger import merge_csvs_from_directory

merge_csvs_from_directory("<input directory of csv files>", "<output path>")
```

## Installation
A user must install this package manually (through pip).
First, clone the repository.

Next, navigate to the folder containing the `setup.py` file.

Finally, run:
```bash
python setup.py install
```


## License
No license.