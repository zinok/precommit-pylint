precommit-pylint
==========

Hook for pylint with configurable score limit.


## Installation

`pip install precommit-pylint`


## Console scripts

```
precommit-pylint --help
usage: reorder-python-imports [-h] [--diff-only] [--add-import ADD_IMPORT]
                              [--remove-import REMOVE_IMPORT]
                              [--application-directories APPLICATION_DIRECTORIES]
                              [filenames [filenames ...]]

positional arguments:
  filenames

optional arguments:
  -h, --help            show this help message and exit
  --diff-only           Show unified diff instead of applying reordering.
  --add-import ADD_IMPORT
                        Import to add to each file. Can be specified multiple
                        times.
  --remove-import REMOVE_IMPORT
                        Import to remove from each file. Can be specified
                        multiple times.
  --application-directories APPLICATION_DIRECTORIES
                        Colon separated directories that are considered top-
                        level application directories. Defaults to `.`
```

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Hooks available:
- `precommit-pylint` - This hook runs pylint and allows configurable score limit

