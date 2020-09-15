import sys
import re
def read_coord_PDB(nomfichier):
    """
    Read pdb template file and retreive Calphas coordinates.
    Args : PDB filename
    Output : dictionnary with position : list of coordinates
    """
    position=[]
    with open(nomfichier,'r') as file:
        for line in file:
            if re.search("^ATOM",line):
                x = float(line[32:38])
                y = float(line[40:46])
                z = float(line[48:54])
                position.append([x,y,z])
    return(position)

if __name__ == "__main__":
    pdbFile = sys.argv[1]
    pos = read_coord_PDB(pdbFile)
    print(len(pos))