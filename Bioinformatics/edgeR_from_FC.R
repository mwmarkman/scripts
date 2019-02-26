library(edgeR)

#Note: Classically you would expect to normalize for gene length, but we are only concerned with the differnces between samples. Gene length is expected to have the same effect on read counts across samples. 

#Note: We should go back and make sure of these results, weirdly the library size for sample6-3 is 1/3 the other library sizes

#Read in featureCounts input and modify it for use with edgeR
fc <- read.table('/Users/MacProMatt/Desktop/mouse/sorted/features_count_all/total_file.count', header = T)
row.names(fc) <- fc$Geneid
fc_min <- subset(fc, select = -c(Geneid,Chr,Start,End,Strand,Length))
group <- c(0,1,2,3,4,5,3,4,5,3,4,5)
dge <- DGEList(counts = fc_min, group = group)

#Filter out genes that are lowly expressed
keep <- rowSums(cpm(dge)>1) >= 2
dge <- dge[keep, , keep.lib.sizes=FALSE]

#adjust for RNA composition levels
dge <- calcNormFactors(dge)

#Estimate the dispersion within the samples
dge <- estimateDisp(dge)

#Output to a csv file (this one is for low versus high)
et <- exactTest(dge, pair=c("4","5"))
csv_out <- topTags(et, n=Inf)
write.csv(csv_out, file = '/Users/MacProMatt/Desktop/Low_versus_high.csv')
