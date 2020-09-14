"""
This script contains a function that directly codes for dynamic programming, and is meant to be imported into another script for use. In the event that it is called as a main, an example of how it works is outputted.

Usage:
    
    import prog_dynam.py

or

    python3 prog_dynam.py
"""

__authors__ = ("Apollinaire Roubert")
__contact__ = ("apo.roubert@gmail.com")
__version__ = "1.0.0"
__date__ = "2020/09/14"

import numpy as np
import pandas as pd


class prog_dynam_matrix:
    lines = ''      #contains row names for display
    columns = ''    #contains column names for display
    lin = 0         #number of rows in the data set including a blank first row
    col = 0         #same as last line but for columns
    output = 0      #the final score of the optimal alignment
    content = 0     #the entire matrix
    
    def __init__(self, data1, data2):
        self.lines = ['_'] + data1
        self.columns = ['_'] + data2
        self.lin = len(self.lines)
        self.col = len(self.columns)
    
    def create_content(self): #method that initialises the matrix
        self.content = np.zeros((self.lin, self.col), dtype = int)
        
    def fill_up(self, score_mat):   #method that fills the matrix up
        gaps = score_mat['gap']
        for i in range(1, self.lin):
            for j in range(1, self.col):
                self.content[i, j] += max(score_mat[self.lines[i] + self.columns[j]]
                                        + self.content[i-1, j-1], 
                                        self.content[i-1, j] + gaps, 
                                        self.content[i, j-1] + gaps)
                if i == (self.lin-1) and j == (self.col-1):
                    self.output = self.content[i,j]
    
    def optimal_path(self): #method that returns 1 POSSIBLE optimal path
        tmp = [self.lin-1, self.col-1]
        ver = [tmp[0]]
        hor = [tmp[1]]
        while tmp != [0, 0] :
            diag = self.content[tmp[0]-1, tmp[1]-1]
            up = self.content[tmp[0]-1, tmp[1]]
            left = self.content[tmp[0], tmp[1]-1]
            prev = []
            if max(diag, up, left) == diag:
                tmp = [tmp[0]-1, tmp[1]-1]
            elif max(diag, up, left) == up:
                tmp = [tmp[0]-1, tmp[1]]
            else:
                tmp = [tmp[0], tmp[1]-1]
            ver.append(tmp[0])
            hor.append(tmp[1])
        alignment = [[],[]]
        prev_ver = 0
        prev_hor = 0
        for i in ver:
            if prev_ver == i:
                alignment[0].append('-')
            else:
                alignment[0].append(self.lines[i])
            prev_ver = i
        for i in hor:
            if prev_hor == i:
                alignment[1].append('-')
            else:
                alignment[1].append(self.columns[i])
            prev_hor = i
        print(''.join(alignment[0]) + '\n' + ''.join(alignment[1]))

    def show(self): #method that displays the matrix with its contents
        print(pd.DataFrame(self.content, columns = self.columns, index = self.lines))


if __name__ == "__main__":
    data_series1 = ['A','A','A','A','T','T','T','T','G','C','C','C','C','C','C',
                    'C','C','C','C','C']
    data_series2 = ['T','T','T','T','C','C','C','C','C','C','C','C','C','C','C',
                    'C']
    score_mat = {'gap':-1,'AT':2,'AA':4,'AG':1,'AC':1,
                    'TA':2,'TT':4,'TG':1,'TC':0,
                    'GG':6,'GA':1,'GC':5,'GT':1,
                    'CA':1,'CC':5,'CT':0,'CG':5}
    example1 = prog_dynam_matrix(data_series1, data_series2)
    example1.create_content()
    example1.fill_up(score_mat)
    print("\nExample:\n")
    print("\nData set 1 :{}\nData set 2 :{}\nScore matrix :{}\n".format(data_series1,
            data_series2, score_mat))
    print("\nOptimal alignment has a score of {}\n".format(example1.output))
    example1.show()
    example1.optimal_path()