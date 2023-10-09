#!/usr/bin/env python3

import argparse
import contextlib
import io
import os
import re

from pylint.lint import Run as pylint_run

_IGNORE_REGEXP = re.compile(
    r'Ignoring entire file \(file-ignored\)'
)


def _check_ignore(pylint_output):
    """Check the python file whether ignored
    If the file is ignored returns True,
    returns False otherwise
    """
    for line in pylint_output.splitlines():
        match = re.search(_IGNORE_REGEXP, line)
        if match:
            return True

    return False


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
    if os.path.basename(filename) == '__init__.py' and os.stat(filename).st_size == 0:
        print(f'Skipping pylint on {filename} (empty __init__.py..\tSKIPPED')
        return True

    # Start pylint
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        with contextlib.redirect_stderr(buffer):
            linter = pylint_run([filename], exit=False).linter

    out = buffer.getvalue()

    # pylint don't score files without statements
    score_missing = 0.0 if getattr(linter.stats, 'statement', False) else 10.0

    # Verify the score
    score = getattr(linter.stats, 'global_note', score_missing)
    ignored = _check_ignore(out)
    file_passed = ignored or score >= float(limit)

    # Add some output
    print('Running pylint on {}.. {:.2f}/10.00\t{}{}'.format(
        filename, score,
        'PASSED' if file_passed else 'FAILED',
        '\tIGNORED' if ignored else ''
    ))

    if output and score < 10:
        print("{0}\n{1}{0}\n".format("=" * 80, out))

    return file_passed


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
