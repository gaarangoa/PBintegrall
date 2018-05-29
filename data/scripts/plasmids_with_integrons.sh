files=`awk '{print $2}' plasmids.list.txt`
cd ./plasmid/

for file in $files;
do
    fx=`echo $file | awk '{gsub(".fasta","",$0); print }'`
    cat $file | awk -v File=$file '{if($_~/# No Integron found/){print File"\t"0}else{print File"\t"1}}'
done

cd ..