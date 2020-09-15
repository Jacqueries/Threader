"""
This script contains a program that calculates the high level matrix
for double dynamic programming, using previously written codes

Usage:
    
    python3 high_level.py pdb_file.pdb seq_file.fasta dope_file.par


NOTICE : CHANGE THE GAP PENALTIES, THE DIFFERENCES ARE MAJOR



"""

__authors__ = ("Apollinaire Roubert", "Ilyas Granguillaume")
__contact__ = ("apo.roubert@gmail.com", "ilyas.tuteur@gmail.com")
__version__ = "1.0.0"
__date__ = "2020/09/15"

from gen_low_level import *

def high_level(low_scores, query, template_length):
    """Generate the high level matrice 
    Args :
        -low_scores: Dict containing final scores for each fixed position
	-query: sequence to thread
	-template_length: number of position   
    """
    h_mat = prog_dynam_matrix(list(range(template_length)), query)
    h_mat.create_content()
    h_mat.fill_high(low_scores)
    h_mat.show()
    h_mat.optimal_path()

if __name__ == '__main__':
    if len(sys.argv)>1 and sys.argv[1]=='help':
        print(__doc__)
    else:
    	template = pP.read_coord_PDB(sys.argv[1])
        mat_col = create_DistMat(template)
        query = readTargSeq(sys.argv[2])
        mat_score = generate_low(mat_col, query, sys.argv[3])
        high_level(mat_score, query, len(template))
        
