# Matthew Markman, September 2018
# Takes a samtools style .pileup file and outputs statistics for every
# base within a short reference (in this case flu).
# Designed with scIAV (see PNAS paper) in mind, as calling SNPs or indels
# traditionally only displays variations that are seen across most reads.
# Designed to be run on a single .pileup file.

import csv
import os.path

path = "/Users/MacProMatt/Desktop/mpileup.shen/Sample5-2-.rmdup.bam.mpileup"  # Switch file path here
name_of_file = 'Sample5-2.csv' # Change output file name here

print("Variation data for the file: " + path)
file_to_parse = open(path, 'r')

save_location = '/Users/MacProMatt/Desktop/mpileup.shen/csv'

file = os.path.join(save_location, name_of_file)

with open(file, 'w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    cm1, cna, cnp, cns1, cpa, cpb1, cpb2, cnep, cm2 = (1, 1, 1, 1, 1, 1, 1, 1, 1)
    file_writer.writerow(['chr', 'pos', 'con', 'cov', 'SNPs', 'indels'])
    for line in file_to_parse:
        execute = False
        chromosome = ''
        position = -1
        mod = -1
        line = line.replace('\t', '@')
        if line.startswith("M1"):
            chromosome = "M1"
            position = cm1
            execute = True
            cm1 += 1
        elif line.startswith("NA"):
            chromosome = "NA"
            position = cna
            execute = True
            cna += 1
        elif line.startswith("NP"):
            chromosome = "NP"
            position = cnp
            execute = True
            cnp += 1
        elif line.startswith("NS1"):
            chromosome = "NS1"
            position = cns1
            execute = True
            cns1 += 1
        elif line.startswith("PA"):
            chromosome = "PA"
            position = cpa
            execute = True
            cpa += 1
        elif line.startswith("PB1"):
            chromosome = "PB1"
            position = cpb1
            execute = True
            cpb1 += 1
        elif line.startswith("PB2"):
            chromosome = "PB2"
            position = cpb2
            execute = True
            cpb2 += 1
        elif line.startswith("NEP"):
            chromosome = "NEP"
            position = cnep
            execute = True
            cnep += 1
        elif line.startswith("M2"):
            chromosome = "M2"
            position = cm2
            execute = True
            cm2 += 1
        elif line.startswith("HA"):
            pass
        else:
            print("****************")
            print("FAILED TEST CASE")
            print("****************")
        if execute:
            line = line.replace((chromosome + '@' + str(position) + "@"), '')
            consensus = line[0]
            line = line[2:]
            coverage = line.split('@')[0]
            if int(coverage) < 10:
                line = line[2:]
            elif int(coverage) < 100:
                line = line[3:]
            elif int(coverage) < 1000:
                line = line[4:]
            else:
                print("****************")
                print("FAILED TEST CASE")
                print("****************")
            line = line.split('@')[0]
            indels1 = line.count('+1') + line.count('-1')
            indels2 = line.count('+2') + line.count('-2')
            indels3 = line.count('+3') + line.count('-3')
            indels4 = line.count('+4') + line.count('-4')
            indels5 = line.count('+5') + line.count('-5')
            indels6 = line.count('+6') + line.count('-6')
            indels7 = line.count('+7') + line.count('-7')
            indels8 = line.count('+8') + line.count('-8')
            indels9 = line.count('+9') + line.count('-9')
            indels10 = line.count('+10') + line.count('-10')
            indels = indels1+indels2+indels3+indels4+indels5+indels6+indels7+indels8+indels9+indels10
            indels_weight = indels1+(indels2*2)+(indels3*3)+(indels4*4)+(indels5*5)+(indels6*6)+(indels7*7)+(indels8*8)+(indels9*9)+(indels10*10)
            snps = line.count('a') + line.count('t') + line.count('c') + line.count('g') + line.count('A') + line.count('T') + line.count('C') + line.count('G')
            snps = snps - indels_weight
            total = snps + indels
            if int(coverage) != 0:
                mod = total/(int(coverage))
            else:
                mod = 0
            file_writer.writerow([chromosome, position, consensus, coverage, snps, indels, mod])
            print(line)
            print(snps)
            print(indels)

