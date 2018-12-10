# Usage from command line: python3 <first input sam> <name to write unique reads of sam1 to>
# <second input sam> <sam2 unique reads>
# Note that the usage of this script is to pull out uniquely aligned reads between two samfiles.
# Requirement: Input samfiles are sorted by read namd
# To ensure all the reads are aligned, you should use 'samtools view <bowtie_sam> -o <outfile> -F 4'
#  to filter out unaligned reads prior to running this script

import sys
import os


def main():
    unique_one = open(sys.argv[2], 'w')
    unique_two = open(sys.argv[4], 'w')
    prev_10 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    counter = 0  # Use counter with mod 10 to place into list in ordered fashion
    with open(sys.argv[1]) as one_sam:
        with open(sys.argv[3]) as two_sam:
            line1 = one_sam.readline()
            line2 = two_sam.readline()
            while line1 and line2:
                line1_mod, line2_mod = line1.strip().split('\t'), line2.strip().split('\t')
                line1_mod, line2_mod = line1_mod[0], line2_mod[0]
                line1_mod, line2_mod = line1_mod.split('.'), line2_mod.split('.')
                line1_mod, line2_mod = line1_mod[1], line2_mod[1]
                if line1_mod > line2_mod:
                    if line2_mod not in prev_10:
                        unique_two.write(line2)
                    line2 = two_sam.readline()
                elif line2_mod > line1_mod:
                    if line1_mod not in prev_10:
                        unique_one.write(line1)
                    line1 = one_sam.readline()
                elif line2_mod == line1_mod:
                    prev_10[counter % 10] = line2_mod
                    line1 = one_sam.readline()
                    line2 = two_sam.readline()
                    counter += 1


if __name__ == "__main__":
    main()
