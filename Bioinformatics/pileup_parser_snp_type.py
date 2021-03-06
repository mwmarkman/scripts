# Matthew Markman, September 2018
# Takes a samtools style .pileup file and outputs statistics for every
# base within a short reference (in this case flu).
# Designed with scIAV (see PNAS paper) in mind, as calling SNPs or indels
# traditionally only displays variations that are seen across most reads.
# Designed to be run on a single .pileup file.

import csv
import os.path

path = "/Users/MacProMatt/Desktop/Langlois_Project_009/pileup_results/9-3.mpileup"  # Switch file path here
name_of_file = 'Sample9-3_snptype.csv'  # Change output file name here

print("Variation data for the file: " + path)
file_to_parse = open(path, 'r')

save_location = '/Users/MacProMatt/Desktop/Langlois_Project_009/pileup_results'

file = os.path.join(save_location, name_of_file)


with open(file, 'w') as write_file:
    chrom_count = {'M1': 0, 'NA': 0, 'NP': 0, 'NS1': 0, 'PA': 0, 'PB1': 0, 'PB2': 0, 'NEP': 0, 'M2': 0}
    file_writer = csv.writer(write_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['chr', 'pos', 'con', 'cov', 'SNPs', 'indels', 'freq', 'ts', 'tv '])
    for line in file_to_parse:
        f = line.strip().split('\t')
        execute = False
        chromosome, position, consensus, coverage, aln_type = f[0], f[1], f[2], f[3], f[4]
        if chromosome in chrom_count:
            chrom_count[chromosome] += 1
            execute = True
        if execute:
            snps = aln_type.count('a') + aln_type.count('t') + aln_type.count('c') + aln_type.count(
                'g') + aln_type.count('A') + aln_type.count(
                'T') + aln_type.count('C') + aln_type.count('G')
            if consensus == 'A' or consensus == 'a':
                ts = aln_type.count('T') + aln_type.count('t')
                tv = aln_type.count('C') + aln_type.count('c') + aln_type.count('G') + aln_type.count('g')
            elif consensus == 'T' or consensus == 't':
                ts = aln_type.count('A') + aln_type.count('a')
                tv = aln_type.count('C') + aln_type.count('c') + aln_type.count('G') + aln_type.count('g')
            elif consensus == 'G' or consensus == 'g':
                ts = aln_type.count('c') + aln_type.count('C')
                tv = aln_type.count('T') + aln_type.count('t') + aln_type.count('a') + aln_type.count('A')
            elif consensus == 'C' or consensus == 'c':
                ts = aln_type.count('g') + aln_type.count('G')
                tv = aln_type.count('T') + aln_type.count('t') + aln_type.count('a') + aln_type.count('A')
            else:
                ts = 0
                tv = 0
            indels1 = aln_type.count('+1') + aln_type.count('-1')
            indels2 = aln_type.count('+2') + aln_type.count('-2')
            indels3 = aln_type.count('+3') + aln_type.count('-3')
            indels4 = aln_type.count('+4') + aln_type.count('-4')
            indels5 = aln_type.count('+5') + aln_type.count('-5')
            indels6 = aln_type.count('+6') + aln_type.count('-6')
            indels7 = aln_type.count('+7') + aln_type.count('-7')
            indels8 = aln_type.count('+8') + aln_type.count('-8')
            indels9 = aln_type.count('+9') + aln_type.count('-9')
            indels10 = aln_type.count('+10') + aln_type.count('-10')
            indels = indels1+indels2+indels3+indels4+indels5+indels6+indels7+indels8+indels9+indels10
            indels_weight = indels1+(indels2*2)+(indels3*3)+(indels4*4)+(indels5*5)+(indels6*6)+(indels7*7)+(indels8*8)+(indels9*9)+(indels10*10)
            snps = snps - indels_weight
            total = snps + indels
            if int(coverage) != 0:
                print("EXECUTE")
                print(total)
                print(int(coverage))
                mod = float(total/(int(coverage)))
                print(mod)
            else:
               mod = 0
            file_writer.writerow([chromosome, position, consensus, coverage, snps, indels, mod, ts, tv])