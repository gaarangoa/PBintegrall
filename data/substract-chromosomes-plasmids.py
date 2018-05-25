# This scripts traverses a file from the PATRIC database and splits the files into chromosome sequences and plasmids.
# /data/patric/genomes/1133852.3 

import sys

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

def mkdir(directory):
    try:
        os.stat(directory)
    except:
        os.mkdir(directory) 

fi=sys.argv[1] # fasta file with sequences
diri = sys.argv[2] # input directory
diro=sys.argv[3] # output directory

mkdir(diro+"/plasmids/")
mkdir(diro+"/chromosomes/")

for ix,record in enumerate(SeqIO.parse(diri+"/"+fi+"/"+fi+".fna", "fasta")):
    gid = record.description 
    seq = record.seq

    if "plasmid" in gid: 
        gtype="plasmids"
    else:
        gtype="chromosomes"
    
    nrecord = SeqRecord(record.seq, id=record.id, name='', description=record.description)
    SeqIO.write([nrecord], open(diro+"/"+gtype+'/'+fi+"_"+str(ix)+'.fasta', 'w'), 'fasta')


