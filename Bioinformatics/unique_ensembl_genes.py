# script to split out a sam or sam type alignment by whether the spot a read mapped to
# is characterized with an ensembl ID or not
import sys

ensembl_out_file = open(sys.argv[2], 'w')
unchr_out_file = open(sys.argv[3], 'w')

with open(sys.argv[1]) as reads:
    line = reads.readline()
    while line:
        split_line = line.strip().split('\t')
        if line[2].startswith("ENSM"):
            ensembl_out_file.write(line)
        else:
            unchr_out_file.write(line)
        line = reads.readline()
