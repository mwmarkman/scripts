import sys
class GCD4034():
	#Reads a file with all the sequences, FASTA format, skips the new line characters
	def readFile(self):
		inFile = open(sys.argv[1], "r")
		line2 = ""
		line2 = line2 + inFile.readline()
		line2 = line2.rstrip('\n')
		for line in inFile:
			line2 += line.rstrip('\n')
		self.findATG(line2)

	#runs the file
	def main(self):
		self.readFile()

	#finds the start codon
	def findATG(self,X):
		code = ""
		letters = ""
		stop = 0
		number = 0
		for i in range(len(X) - 2):
			#Start codon checker
			#Case to enter the loop of 3s after start codon
			if X[i] == "A" and X[i+1] == "T" and X[i+2] == "G":
				number = number+1
				code = code + "Theoretical Protein #: " + str(number) + "\n"
				code = code + "Met "
				letters = letters + "M"
				#next base after START codon's sequence
				j = i+3
				finish = False
				#finds the stop codons
				while (finish == False and j < len(X)-2):
					#enter into codon finder

					#Stop codon checker 1
					if X[j] == "T" and X[j+1] == "G" and X[j+2] == "A":
						stop = j
						code = code + "Stop"
						letters = letters + " Stop"
						code = code + '\n' + letters
						code = code + '\n' +'{Start position: ' + str(i)
						code = code + '\t' + 'Stop position: ' + str(stop) + '\t'
						pro_length = (stop+1 - i)/3
						code = code + 'Protein Length: ' + str(pro_length) + ' amino acids}' +'\n' + '\n' 
						letters = ""
						finish = True

					#Stop codon checker 2
					elif X[j] == "T" and X[j+1] == "A" and X[j+2] == "A":	
						stop = j
						code = code + "Stop"
						letters = letters + " Stop"
						code = code + '\n' + letters
						code = code + '\n' +'{Start position: ' + str(i)
						code = code + '\t' + 'Stop position: ' + str(stop) + '\t'
						pro_length = (stop+1 - i)/3
						code = code + 'Protein Length: ' + str(pro_length) + ' amino acids}' +'\n' + '\n' 
						letters = ""
						finish = True

					#Stop codon checker 3
					elif X[j] == "T" and X[j+1] == "A" and X[j+2] == "G":	
						stop = j
						code = code + "Stop"
						letters = letters + " Stop"
						code = code + '\n' + letters
						code = code + '\n' +'{Start position: ' + str(i)
						code = code + '\t' + 'Stop position: ' + str(stop) + '\t'
						pro_length = (stop+1 - i)/3
						code = code + 'Protein Length: ' + str(pro_length) + ' amino acids}' +'\n' + '\n' 
						letters = ""
						finish = True

					else:
						#finds the rest of the codons
						if X[j] == "A" and X[j+1] == "T" and X[j+2] == "G":	
							code = code + "Met "
							letters = letters + "M"
						elif X[j] == "T" and X[j+1] == "T" and X[j+2] == "T":	
							code = code + "Phe1 "
							letters = letters + "F"
						elif X[j] == "T" and X[j+1] == "T" and X[j+2] == "C":	
							code = code + "Phe2 "
							letters = letters + "F"
						elif X[j] == "T" and X[j+1] == "T" and X[j+2] == "A":	
							code = code + "Leu "
							letters = letters + "L"
						elif X[j] == "T" and X[j+1] == "T" and X[j+2] == "G":	
							code = code + "Leu "
							letters = letters + "L"
						elif X[j] == "T" and X[j+1] == "C" and X[j+2] == "T":	
							code = code + "Ser "
							letters = letters + "S"
						elif X[j] == "T" and X[j+1] == "C" and X[j+2] == "C":	
							code = code + "Ser "
							letters = letters + "S"
						elif X[j] == "T" and X[j+1] == "C" and X[j+2] == "A":	
							code = code+ "Ser "
							letters = letters + "S"
						elif X[j] == "T" and X[j+1] == "C" and X[j+2] == "G":	
							code = code+ "Ser "
							letters = letters + "S"
						elif X[j] == "T" and X[j+1] == "A" and X[j+2] == "T":	
							code = code+ "Tyr "
							letters = letters + "Y"
						elif X[j] == "T" and X[j+1] == "A" and X[j+2] == "C":	
							code = code+ "Tyr "
							letters = letters + "Y"
						elif X[j] == "T" and X[j+1] == "G" and X[j+2] == "T":	
							code = code+ "Cys "
							letters = letters + "C"
						elif X[j] == "T" and X[j+1] == "G" and X[j+2] == "C":	
							code = code+ "Cys "
							letters = letters + "C"
						elif X[j] == "T" and X[j+1] == "G" and X[j+2] == "G":	
							code = code+ "Trp "
							letters = letters + "W"
						elif X[j] == "C" and X[j+1] == "T" and X[j+2] == "T":	
							code = code+ "Leu "
							letters = letters + "L"
						elif X[j] == "C" and X[j+1] == "T" and X[j+2] == "C":	
							code = code+ "Leu "
							letters = letters + "L"
						elif X[j] == "C" and X[j+1] == "T" and X[j+2] == "A":	
							code = code+ "Leu "
							letters = letters + "L"
						elif X[j] == "C" and X[j+1] == "T" and X[j+2] == "G":	
							code = code+ "Leu "
							letters = letters + "L"
						elif X[j] == "C" and X[j+1] == "C" and X[j+2] == "T":	
							code = code+ "Pro "
							letters = letters + "P"
						elif X[j] == "C" and X[j+1] == "C" and X[j+2] == "C":	
							code = code+ "Pro "
							letters = letters + "P"
						elif X[j] == "C" and X[j+1] == "C" and X[j+2] == "A":	
							code = code+ "Pro "
							letters = letters + "P"
						elif X[j] == "C" and X[j+1] == "C" and X[j+2] == "G":	
							code = code+ "Pro "
							letters = letters + "P"
						elif X[j] == "C" and X[j+1] == "A" and X[j+2] == "T":	
							code = code+ "His "
							letters = letters + "H"
						elif X[j] == "C" and X[j+1] == "A" and X[j+2] == "C":	
							code = code+ "His "
							letters = letters + "H"
						elif X[j] == "C" and X[j+1] == "A" and X[j+2] == "A":	
							code = code+ "Gln "
							letters = letters + "Q"
						elif X[j] == "C" and X[j+1] == "A" and X[j+2] == "G":	
							code = code+ "Gln "
							letters = letters + "Q"
						elif X[j] == "C" and X[j+1] == "G" and X[j+2] == "T":	
							code = code+ "Arg "
							letters = letters + "R"
						elif X[j] == "C" and X[j+1] == "G" and X[j+2] == "C":	
							code = code+ "Arg "
							letters = letters + "R"
						elif X[j] == "C" and X[j+1] == "G" and X[j+2] == "A":	
							code = code+ "Arg "
							letters = letters + "R"
						elif X[j] == "C" and X[j+1] == "G" and X[j+2] == "G":	
							code = code+ "Arg "
							letters = letters + "R"
						elif X[j] == "A" and X[j+1] == "T" and X[j+2] == "T":	
							code = code+ "Ile "
							letters = letters + "I"
						elif X[j] == "A" and X[j+1] == "T" and X[j+2] == "C":	
							code = code+ "Ile "
							letters = letters + "I"
						elif X[j] == "A" and X[j+1] == "T" and X[j+2] == "A":	
							code = code+ "Ile "
							letters = letters + "I"
						elif X[j] == "A" and X[j+1] == "C" and X[j+2] == "T":	
							code = code+ "Thr "
							letters = letters + "T"
						elif X[j] == "A" and X[j+1] == "C" and X[j+2] == "C":	
							code = code+ "Thr "
							letters = letters + "T"
						elif X[j] == "A" and X[j+1] == "C" and X[j+2] == "A":	
							code = code+ "Thr "
							letters = letters + "T"
						elif X[j] == "A" and X[j+1] == "C" and X[j+2] == "G":	
							code = code+ "Thr "
							letters = letters + "T"
						elif X[j] == "A" and X[j+1] == "A" and X[j+2] == "T":	
							code = code+ "Asn "
							letters = letters + "N"
						elif X[j] == "A" and X[j+1] == "A" and X[j+2] == "C":	
							code = code+ "Asn "
							letters = letters + "N"
						elif X[j] == "A" and X[j+1] == "A" and X[j+2] == "A":	
							code = code+ "Lys "
							letters = letters + "K"
						elif X[j] == "A" and X[j+1] == "A" and X[j+2] == "G":	
							code = code+ "Lys "
							letters = letters + "K"
						elif X[j] == "A" and X[j+1] == "G" and X[j+2] == "T":	
							code = code+ "Ser "
							letters = letters + "S"
						elif X[j] == "A" and X[j+1] == "G" and X[j+2] == "C":	
							code = code+ "Ser "
							letters = letters + "S"
						elif X[j] == "A" and X[j+1] == "G" and X[j+2] == "A":	
							code = code+ "Arg "
							letters = letters + "R"
						elif X[j] == "A" and X[j+1] == "G" and X[j+2] == "G":	
							code = code+ "Arg "
							letters = letters + "R"
						elif X[j] == "G" and X[j+1] == "T" and X[j+2] == "T":	
							code = code+ "Val "
							letters = letters + "V"
						elif X[j] == "G" and X[j+1] == "T" and X[j+2] == "C":	
							code = code+ "Val "
							letters = letters + "V"
						elif X[j] == "G" and X[j+1] == "T" and X[j+2] == "A":	
							code = code+ "Val "
							letters = letters + "V"
						elif X[j] == "G" and X[j+1] == "T" and X[j+2] == "G":	
							code = code+ "Val "
							letters = letters + "V"
						elif X[j] == "G" and X[j+1] == "C" and X[j+2] == "T":	
							code = code+ "Ala "
							letters = letters + "A"
						elif X[j] == "G" and X[j+1] == "C" and X[j+2] == "C":	
							code = code+ "Ala "
							letters = letters + "A"
						elif X[j] == "G" and X[j+1] == "C" and X[j+2] == "A":	
							code = code+ "Ala "
							letters = letters + "A"
						elif X[j] == "G" and X[j+1] == "C" and X[j+2] == "G":	
							code = code+ "Ala "
							letters = letters + "A"
						elif X[j] == "G" and X[j+1] == "A" and X[j+2] == "T":	
							code = code+ "Asp "
							letters = letters + "D"
						elif X[j] == "G" and X[j+1] == "A" and X[j+2] == "C":	
							code = code+ "Asp "
							letters = letters + "D"
						elif X[j] == "G" and X[j+1] == "A" and X[j+2] == "A":	
							code = code+ "Glu "
							letters = letters + "E"
						elif X[j] == "G" and X[j+1] == "A" and X[j+2] == "G":	
							code = code+ "Glu "
							letters = letters + "E"
						elif X[j] == "G" and X[j+1] == "G" and X[j+2] == "T":	
							code = code+ "Gly "
							letters = letters + "G"
						elif X[j] == "G" and X[j+1] == "G" and X[j+2] == "C":	
							code = code+ "Gly "
							letters = letters + "G"
						elif X[j] == "G" and X[j+1] == "G" and X[j+2] == "A":	
							code = code+ "Gly "
							letters = letters + "G"
						elif X[j] == "G" and X[j+1] == "G" and X[j+2] == "G":	
							code = code+ "Gly "
							letters = letters + "G"
						j = j+3

		self.writeFile(code) #sends the string of proteins letters to the output text file method
		#writes to output file 
	def writeFile(self,A): 
		 outFile = open("output.txt", "w")
		 outFile.write(A)
		 outFile.close()
        print "output.txt created!"

ex = GCD4034()
y = ex.main()

