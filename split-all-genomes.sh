# list all genomes:

list=`ls $1` # input the directory where all the genomes are

for g in $list;
do 
    python substract-chromosomes-plasmids.py $g $2 $3
done

