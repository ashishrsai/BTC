#!/bin/bash
# Basic while loop
#!/bin/bash
# Basic while loop
for i in $(seq 7.01 0.10 7.91);
do echo $i;
for j in $(seq 0.01 0.01 0.50);
do echo $j;
echo $a
a=$j
b=0.51
CPU_USAGE=$( bc <<< "$b-$a" )
tail -n 3 /home/ashish/Desktop/FinalData/minute7/blockTime$i$j.txt | head -n1 >> ashishrsai$i.txt
done
done
