"""
This script contains a program that calculates the low level matrices
for double dynamic programming, using previously written codes

Usage:
    
    python3 gen_low_level.py

or

    from gen_low_level import *

"""

__authors__ = ("Apollinaire Roubert")
__contact__ = ("apo.roubert@gmail.com")
__version__ = "1.0.0"
__date__ = "2020/09/14"

from prog_dynam import *
from distIntraTemplate import *
from readTarget import *



if __name__ == '__main__':
    template = pP.read_coord_PDB(sys.argv[1])
    dist_mat = create_DistMat(template)
    print(dist_mat)
    print(template)
