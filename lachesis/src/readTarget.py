import sys
from Bio import SeqIO



def readTargSeq(seq):
    """
    	Read query and translate from one letter to 3 letter code
    Args : fasta filename
    Output : ordered list of aas 
    """
    tlCode = {"A": ["ALA",0], "R":["ARG",0], "N":["ASN",0], "D":["ASP",0], "C":["CYS",0], "E":["GLU",0], "Q":["GLN",0], "G":["GLY",0], "H":["HIS",0], "I":["ILE",0], "L":["LEU",0], "K":["LYS",0], "M":["MET",0], "F":["PHE",0], "P":["PRO",0], "S":["SER",0], "T":["THR",0], "W":["TRP",0], "Y":["TYR",0], "V":["VAL",0]}
    for record in SeqIO.parse(seq, "fasta"):
        pass
    nseq = str(record.seq)
    seqT = []	
    for letter in nseq:
        if letter == 'X':
            continue
        tlCode[letter][1] += 1
      
        seqT.append(tlCode[letter][0] + "_" + str(tlCode[letter][1])) # to identify repeating residues
    return(seqT)


if __name__ == "__main__":
    seq = sys.argv[1]
    readTargSeq(seq)
