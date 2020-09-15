"""
This script contains a program that calculates the low level matrices
for double dynamic programming, using previously written codes

Usage:
    
    python3 gen_low_level.py pdb_file.pdb seq_file.fasta dope_file.par

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
        """Generate all low level matrices
    Args :
	-query: sequence to thread
	-dope_file: self expl
	-mat_col: matrix that link distance and column in dope file
    Return dictionnary in the form of key : AA_n°_position and value : alignment final score
    """
    template_length = len(mat_col.iloc[0, :])
    mat_names = {'gap' : -2}
    for i,res in enumerate(query): #Fixing res in pos
        for pos in range(template_length):
            mat_name = res + "_" + str(pos)   #name of the low_level matrix
            tmp_score = gen_low_score(res, i, pos, query, template_length, dope_file, mat_col) #get the score matrix of the low-level matrix
            tmp_mat = prog_dynam_matrix(list(range(template_length)), query)
            tmp_mat.create_content()
            tmp_mat.fill_up(tmp_score, [pos+1, i+1])
            tmp_mat.show()
            tmp_mat.optimal_path()
            mat_names[mat_name] = tmp_mat.output
    return mat_names


def gen_low_score(res, i, pos, query, template_length, dope_file, mat_col):
    """Position - residue pairing associated with corresponding dope score
    Args :
        -res: fixed res
	-i: position of res in [query]
	-pos: position in template 
	-query: sequence to thread
	-template_length: number of position 
	-dope_file: self expl
	-mat_col: matrix that link distance and column in dope file
    Return dictionnary in the form of key : AA_n°_position and value : dope score
	for an AA in a fixed position  
    """
    query_copy = copy.deepcopy(query)
    del query_copy[i] # unused
    output = {'gap':-2} # command line
    with open(dope_file, "r") as filin:    
        lines = filin.readlines()
        for line in lines: # retreive all possible pairings with 20 aas 
            tmp = line.split()
            if tmp[0] == res[0:3]:
                for j in range(template_length):
                    output[tmp[2]+ "_" +str(j)] = float(tmp[mat_col.iloc[pos,j] + 4]) * (-1) #inverse the DOPE potentials
    return output

if __name__ == '__main__':
    if len(sys.argv)>1 and sys.argv[1]=='help':
        print(__doc__)
    else:
    	template = pP.read_coord_PDB(sys.argv[1])
    	mat_col = create_DistMat(template)
    	print(mat_col)
    	query = readTargSeq(sys.argv[2])
    	generate_low(mat_col, query, sys.argv[3])
    
