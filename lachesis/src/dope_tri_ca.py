"""
This script will scour a DOPE potential file, find all lines that deal with only Alpha carbon interactions for both residues, extract them, then write a new .par file with only those lines.

Takes as argument a DOPE potential file under the .par format
Returns a .par file named "dope_ca_only.par" with only the CA-CA lines

Usage:

    python3 dope_tri_ca.py argument1

"""

__authors__ = ("Apollinaire Roubert")
__contact__ = ("apo.roubert@gmail.com")
__version__ = "1.0.0"
__date__ = "2020/09/12"

import sys

def extract_lines(dope_file):
    """
    function that extracts lines with "CA" in the DOPE.par file
    arguments:
        dope_file.par (a dope file)
    """
    dope_ca_only = []
    with open(dope_file, "r") as filin:
        lines = filin.readlines()
        for line in lines:
            if line.split()[1] == "CA" and line.split()[3] == "CA":
                dope_ca_only.append(line)
    return dope_ca_only

def write_new_dope(new_dope_lines):
    """
    function that writes a new dope.par file
    argument:
        file_lines (a list of letters)
    """
    with open("dope_ca_only.par", "w") as filout:
        for line in new_dope_lines:
            filout.write(line)

if __name__ == "__main__":
    new_dope_lines = extract_lines(sys.argv[1])
    write_new_dope(new_dope_lines)
