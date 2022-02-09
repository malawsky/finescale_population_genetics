### set OUTPUT to final directory you wish to use
### run code from within directory that contains IBIS output 

OUTPUT=/filepath/to/output/directory

for file in *.seg
do
  cat "$file" |awk '{print $1"~"$2,$9}' | awk '{ if ($2 >= 5) print $0 }' | awk '
  NR == 1 { print; next }
  { a[$1] += $2 }
  END {
    for (i in a) {
      printf "%-15s\t%s\n", i, a[i];
    }
  }
' >> $OUTPUT/sumIBD_chr${file}.txt 
done

cat $OUTPUT/sumIBD_chr*.txt | awk '
  NR == 1 { print; next }
  { a[$1] += $2 }
  END {
    for (i in a) {
      printf "%-15s\t%s\n", i, a[i];
    }
  }
' > $OUTPUT/sumIBD_all_chr.txt 

cat sumIBD_all_chr.txt | sed -r 's/~/\t/g' | awk '{print $1,$2,$3}' > sumIBD_all_chr_final.txt


