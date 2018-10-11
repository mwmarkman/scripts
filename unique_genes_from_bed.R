setwd("/Users/MacProMatt/Desktop/")
bed = read.table("BALB_snp_genes_strict.bed", sep = "")
bed = data.frame(lapply(bed, as.character), stringsAsFactors = FALSE)

length_bed = length(bed$V1)

V4_list = 1:length_bed
V4_list_copy = 1:length_bed

for (i in V4_list){
  element = bed[i,"V4"]
  element = strsplit(element, "[.]")
  element = element[[1]][1]
  V4_list_copy[i] = element
}

bed$V4 = V4_list_copy

unique_genes = unique(bed$V4)
print(length(unique_genes))

