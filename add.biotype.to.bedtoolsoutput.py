import sys

#infile = open(sys.argv[1],'r') #isoform.exon.mapping.table.txt
infile = open('isoform.exon.mapping.table.txt','r')
infile2 = open('BALB_exons_over_var.bed','r')
outfile = open('BALB_exons_over_var_with_biotype.bed','w')

gdict = {}
for line in infile:
	f = line.strip().split('\t')
	#print(f)
	gid  = f[0]
	eid = f[2]
	biotype = f[5]
	nid = eid+':'+gid
	if nid in gdict:
		gdict[nid].append(biotype)
	elif nid not in gdict:
		gdict[nid] = []
		gdict[nid].append(biotype)

#print(gdict)



for gid in gdict:
	blist = gdict[gid]
	blist = list(set(blist))
	gdict[gid] = blist

#print(gdict)

for line in infile2:
	f = line.strip().split('\t')
	nid = f[3]
	if nid in gdict:
		blist=gdict[nid]
		if len(blist) == 1:
			biotype = blist[0]
			outfile.write(line.strip()+'\t'+biotype+'\n')
		elif len(blist) > 1:
			for biotype in blist:
				outfile.write(line.strip()+'\t'+biotype+'\n')
	else:
		print(line)





