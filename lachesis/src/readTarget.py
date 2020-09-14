import sys
from Bio import SeqIO



def readTargSeq(seq):
    tlCode = {"A": "ALA", "R":"ARG", "N":"ASN", "D":"ASP", "C":"CYS", "E":"GLU", "Q":"GLN", "G":"GLY", "H":"HIS", "I":"ILE", "L":"LEU", "K":"LYS", "M":"MET", "F":"PHE", "P":"PRO", "S":"SER", "T":"THR", "W":"TRP", "Y":"TYR", "V":"VAL"}

    for record in SeqIO.parse(seq, "fasta"):
        pass
    nseq = str(record.seq)
    seqT = []	
    for letter in nseq:
        seqT.append(tlCode[letter])
    return(seqT)


if __name__ == "__main__":
    seq = sys.argv[1]
    readTargSeq(seq)
