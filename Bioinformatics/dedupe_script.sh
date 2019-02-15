#!/bin/bash

#Input 1 for SE reads, 2 for paired end reads in place one after the script name
#If using paired end reads, input 2 is the length of the reads
#For example, for a paired read sequence with 125 bp reads you should call the script with
#sh dedupe_script.sh 2 125

#Requires bbmap and FLASH (Flash only needed for paired end reads)
export PATH=$PATH:/Users/MacProMatt/Desktop/programs/bbmap
export PATH=$PATH:/Users/MacProMatt/Desktop/programs/FLASH-1.2.11
export PATH=$PATH:/Users/MacProMatt/Desktop/programs/fastx_toolkit

cd /Users/MacProMatt/Desktop/Langlois_Project_002

if [ ! -d "deduped" ]; then
  mkdir deduped
fi

if [[ $1 == 1 ]]; then
  for i in *.fastq; do
    clumpify.sh in=${i} out=deduped/${i}.deduped.fastq dedupe
    rm -rf ${i}
  done
#elif [[ $1 == 2 ]]; then
#   echo $2
#   echo $1

  #4) For this specific data, we also need to trim adapter
  #1) use FLASH to concatenate reads
  #2) use bbmerge to merge reads + concatenate
  #3) use clumpify to remove dupes

#  bbmerge.sh in=reads.fq outa=adapters.fa
#  echo "Correct output"
else
  echo "Not a valid input"
fi
