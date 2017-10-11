# This scripts traverses a file from the PATRIC database and splits the files into chromosome sequences and plasmids.

import sys

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

def mkdir(directory)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory) 

fi=sys.argv[1] # fasta file with sequences
dirc=sys.argv[2] #

mkdir(dirc+"/genomes/")
mkdir(dirc+"/chromosomes/")

for ix,record in enumerate(SeqIO.parse(fi, "fasta")):
    gid = record.id 
    seq = record.seq

    if "plasmid" in gid: 
        gtype="plasmids"
    else:
        gtype="chromosomes"
    
    nrecord = SeqRecord(record.seq, id=gid, name='', description=record.description)
    SeqIO.write([nrecord], open(dirc+'/'+gtype+'/'+str(ix)+'.fasta', 'w'), 'fasta')


