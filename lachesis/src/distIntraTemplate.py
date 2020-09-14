import sys
import parsePDB as pP
import pandas as pd
import numpy as np
import math

def dist_pos(pos1,pos2):
    """
        Compute distance between 2 position
        Args:
            + pos1 : xyz
            + pos2 : xyz
        Return euclidian distance
    """
    return( math.sqrt( (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2) )

def create_DistMat(pos):
    
    npos = 10 #len(pos)
    df = pd.DataFrame(np.zeros( (npos,npos) ) )
    for i in range(npos):
        for j in range(npos):
            df.iloc[i,j] = dist_pos(pos[i],pos[j])	
    print(df)

if __name__ == "__main__":
    pdbFile = sys.argv[1]

    create_DistMat(pP.read_coord_PDB(pdbFile))

