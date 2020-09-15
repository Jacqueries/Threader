"""
This script contains a program that calculates the low level matrices
for double dynamic programming, using previously written codes

Usage:
    
    python3 gen_low_level.py

or

    from gen_low_level import *


In Distance matrix, replace the distances with the associated column of the DOPE file


"""

__authors__ = ("Apollinaire Roubert", "Ilyas Granguillaume")
__contact__ = ("apo.roubert@gmail.com", "ilyas.tuteur@gmail.com")
__version__ = "1.0.0"
__date__ = "2020/09/15"

from prog_dynam import *
from distIntraTemplate import *
import parsePDB as pP
from readTarget import *
import copy

def generate_low(mat_col, query, dope_file):
    template_length = len(mat_col.iloc[0, :])
    mat_names = {}
    for i,res in enumerate(query): #Fixing res in pos
        for pos in range(template_length):
            mat_name = res + str(pos)
            tmp_score = placeholder(res, i, pos, query, template_length, dope_file, mat_col)
            tmp_mat = prog_dynam_matrix(list(range(template_length)), query)
            print(tmp_mat.lines, tmp_mat.columns)
            tmp_mat.create_content()
            tmp_mat.fill_up(tmp_score, [pos+1, i+1])
            tmp_mat.show()
            tmp_mat.optimal_path()
            mat_names[mat_name] = tmp_mat.output
    return mat_names


def placeholder(res, i, pos, query, template_length, dope_file, mat_col):
    query_copy = copy.deepcopy(query)
    del query_copy[i]
    output = {'gap':0}
    with open(dope_file, "r") as filin:    
        lines = filin.readlines()
        for line in lines:
            tmp = line.split()
            if tmp[0] != res:
                pass
            for j in range(template_length):
                if j == pos:
                    output[tmp[2]+str(j)] = 0
                    continue
                output[tmp[2]+str(j)] = float(tmp[mat_col.iloc[pos,j]]) * (-1)
    return output

if __name__ == '__main__':
    template = pP.read_coord_PDB(sys.argv[1])
    mat_col = create_DistMat(template)
    print(mat_col)
    query = readTargSeq(sys.argv[2])
    generate_low(mat_col, query, sys.argv[3])
    print("toto")
