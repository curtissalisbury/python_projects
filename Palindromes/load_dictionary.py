"""Loads a text file as a list
Arguments:
    - text file name (and directory path, if needed)
Exceptions:
    - IOError if filename not found
Returns:
    - A list of words in a text file in lower case

Requires:
    - import sys
"""

import sys


def load(file):
    """OPen a text file and return a list of lowercase strings"""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'{e} \n Error opening {file}. Terminating Program',
              file=sys.stderr)
        sys.exit(1)
