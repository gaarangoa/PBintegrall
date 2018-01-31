
files=`ls /data/patric/plasmids/`

for file in $files;
do
    echo $file >> log.plasmids
    integron_finder --local_max --cpu 20 --func_annot --outdir /data/patric/integrons/plasmid/$file /data/patric/plasmids/$file
done