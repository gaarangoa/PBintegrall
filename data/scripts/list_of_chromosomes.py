# This scripts traverses a file from the PATRIC database and splits the files into chromosome sequences and plasmids.
# /data/patric/genomes/1133852.3

import sys

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

fi=sys.argv[1] # fasta file with sequences
diri = sys.argv[2] # input directory
diro=sys.argv[3] # output directory


pfile = open(diro+'/plasmids.txt', 'w')
cfile = open(diro+'/chromosomes.txt', 'w')

for ix,record in enumerate(SeqIO.parse(diri+"/"+fi+"/"+fi+".fna", "fasta")):
    gid = record.description
    seq = record.seq

    if "plasmid" in gid:
        gtype="plasmids"
        pfile.write(gtype+'/'+fi+"_"+str(ix)+'.fasta\n')
        print(gtype+'\t'+fi+"_"+str(ix)+'.fasta')
    else:
        gtype="chromosomes"
        cfile.write(gtype+'/'+fi+"_"+str(ix)+'.fasta\n')
        print(gtype+'\t'+fi+"_"+str(ix)+'.fasta')


