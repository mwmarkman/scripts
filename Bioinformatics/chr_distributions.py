# goal is to find the distribution of "SNPS" over the length of all 8 of the IAV chromosomes
# input one: file path to the location of the csv files to process

import sys
import os


def main():
    for i in os.listdir(sys.argv[1]):
        with open(sys.argv[2]) as out_file:
            for i in ['M1', 'NA', 'NP', 'NS1', 'PA', 'PB1', 'PB2', 'NEP', 'M2']:
                counter = 1



#    out_file = open(sys.argv[2], 'w')
#    with open(sys.argv[1]) as out_file:
#        for i in ['M1', 'NA', 'NP', 'NS1', 'PA', 'PB1', 'PB2', 'NEP', 'M2']:
#            line = in_file.readline()



if __name__ == "__main__":
    main()