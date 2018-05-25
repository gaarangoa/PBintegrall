# list all genomes:
# $1 genomes directory
# $2 input directory
# $3 output directory

dix=$1
dox=$2

list=`ls $dix` # input the directory where all the genomes are

for g in $list;
do
    # echo $g
    # python substract-chromosomes-plasmids.py $g $dix $dox
    python list_of_chromosomes.py $g $dix /data/patric/integrons/
done

