precommit-pylint
==========

Hook for pylint with configurable score limit.


## Notice

The hook is shipped not as a python package as for python packages pre-commit runs them in 
virtualenv, which does not really work for pylint well.

## Console scripts

```
precommit-pylint.py --help
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
