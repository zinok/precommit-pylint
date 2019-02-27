#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import re
import sys
import decimal
import subprocess

_SCORE_REGEXP = re.compile(
    r'^Your\ code\ has\ been\ rated\ at\ (\-?[0-9\.]+)/10')

_IGNORE_REGEXP = re.compile(
    r'Ignoring entire file \(file\-ignored\)'
)

def _parse_score(pylint_output):
    """Parse the score out of pylint's output as a float
    If the score is not found, return 10.0
    """
    for line in pylint_output.splitlines():
        match = re.match(_SCORE_REGEXP, _futurize_str(line))
        if match:
            return float(match.group(1))
    return 10.0

def _check_ignore(pylint_output):
    """Check the python file whether ignored
    If the file is ignored returns True,
    returns False otherwise
    """
    for line in pylint_output.splitlines():
        match = re.search(_IGNORE_REGEXP, _futurize_str(line))
        if match:
            return True

    return False

def _futurize_str(obj):
    if isinstance(obj, bytes):
        obj = obj.decode('utf-8')
    return obj

def check_file(limit, filename, output=False):
    """Check single file

    :type limit: float
    :param limit: Minimum score to pass the commit
    :type filename: str
    :param filename: Path to the file to check
    :type output: bool
    :param output: Show pylint output
    """

    # Check if file to skip
    if os.path.basename(filename) == '__init__.py':
        if os.stat(filename).st_size == 0:
            print(
                'Skipping pylint on {} (empty __init__.py..'
                '\tSKIPPED'.format(filename))
            return True

    # Start pylint
    sys.stdout.write('Running pylint on {}..\t'.format(filename))

    try:
        command = ['pylint', filename]
        proc = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        out, _ = proc.communicate()
    except OSError:
        print("\nAn error occurred. Is pylint installed?")
        return False

    # Verify the score
    score = _parse_score(out)
    ignored = _check_ignore(out)
    if ignored or score >= float(limit):
        status = 'PASSED'
    else:
        status = 'FAILED'

    # Add some output
    print('{:.2}/10.00\t{}{}'.format(
        decimal.Decimal(score),
        status,
        ignored and '\tIGNORED' or ''))

    if output and score < 10:
        print("="*80)
        print(out)
        print("="*80)
        print("")

    # If failed
    if status == 'FAILED':
        return False

    return True

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument(
        '--limit', type=float, default=10,
        help=(
            'Score limit for pylint, defaults to `%(default)s`'
        ),
    )
    parser.add_argument(
        '--output', action='store_true',
        help=(
            'Show pylint output, defaults to `%(default)s`'
        ),
    )
    args = parser.parse_args(argv)

    # check files
    for filename in args.filenames:
        if not check_file(args.limit, filename, args.output):
            return 1

    return 0


if __name__ == '__main__':
    exit(main())
