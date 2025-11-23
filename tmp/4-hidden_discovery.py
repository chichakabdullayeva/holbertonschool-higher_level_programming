#!/usr/bin/python3
"""Print all names defined in hidden_4.pyc (excluding names starting with __)."""

import marshal
import sys

def main():
    pyc_file = "/tmp/hidden_4.pyc"

    with open(pyc_file, "rb") as f:
        f.read(16)  # skip the header of the pyc file (magic number, timestamp, etc.)
        code_obj = marshal.load(f)

    # Retrieve all names defined in the code object
    names = [name for name in code_obj.co_names if not name.startswith("__")]
    
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()
