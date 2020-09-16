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
    """
        Create and return the distance matrix between positions
        Args:
            -pos: coordinates of all CA position in template
    """
    npos = len(pos)
    df = pd.DataFrame(np.zeros( (npos,npos) ) )
    for i in range(npos):
        for j in range(npos):
            df.iloc[i,j] = dist_pos(pos[i],pos[j])
    return create_colmat(df)

def which_col(dist, steps):
    """
        Return a column position in dopefile associated with the correct distance
        Args:
            -dist : the distance between 2 position
	    -steps : number of columns in dopefile
    """
    if dist < 0.25:
        return 0
    for i in range(len(steps)):
        if dist >= steps[i] and dist < steps[i]+0.5:
            return i 
    return 29

def create_colmat(df):
    """
        Create and return the column matrix that associate positions with dopefile columns
        Args:
            -df: matrix of distance
    """
    steps = []
    cpos = len(df.iloc[0,:])
    cdf = pd.DataFrame(np.zeros( (cpos,cpos) ), dtype=int )
    for i in range(30):
        steps.append(0.25 + i*0.5) 
    for i in range(cpos):
        for j in range(cpos):
            cdf.iloc[i,j] = which_col(df.iloc[i,j], steps)
    return cdf

if __name__ == "__main__":
    pdbFile = sys.argv[1]

    create_DistMat(pP.read_coord_PDB(pdbFile))

