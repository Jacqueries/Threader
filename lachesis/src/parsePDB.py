import sys
import re
def read_coord_PDB(nomfichier):
    """
    	Read pdb template file and retreive Calphas coordinates.
    Args : PDB filename
    Output : dictionnary with position : list of coordinates
    """
    position=[]
    mdl = 0
    with open(nomfichier,'r') as file:
        for line in file:
            if line.startswith('MODEL'):
                mdl = mdl + 1
                if mdl >= 2:
                    return(position)  
            if re.search("^ATOM",line) and line[13:15] == "CA":
                x = float(line[32:38])
                y = float(line[40:46])
                z = float(line[48:54])
                position.append([x,y,z])

    return(position)

if __name__ == "__main__":
    pdbFile = sys.argv[1]
    pos = read_coord_PDB(pdbFile)

