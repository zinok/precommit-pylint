precommit-pylint
==========

Hook for pylint with configurable score limit.


## Installation

`pip install precommit-pylint`


## Console scripts

```
precommit-pylint --help
usage: precommit-pylint [-h] [--limit LIMIT] [filenames [filenames ...]]

positional arguments:
  filenames

optional arguments:
  -h, --help     show this help message and exit
  --limit LIMIT  Score limit for pylint, defaults to `10`
```

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Hooks available:
- `precommit-pylint` - This hook runs pylint and allows configurable score limit
