rm(list=ls())

#Volcano plot

jf_dat = read.csv('/Users/MacProMatt/Desktop/JF180 D34 T4.50kvsN4.50k_all.csv')

plot(jf_dat$logFC, -log10(jf_dat$PValue), pch=20, main="Volcano plot", xlab = "log2 Fold Change", ylab = '-log10 P Value', ylim = c(0,50), col = "grey")

high = subset(jf_dat, logFC > 2)
points(high$logFC, -log10(high$PValue), pch = 20, col = "blue")
low = subset(jf_dat, logFC < -2)
points(low$logFC, -log10(low$PValue), pch = 20, col = 'blue')

#with(subset(jf_dat, logFC > 2 ), points(logFC, -log10(PValue), pch=20, col="red"))
#with(subset(jf_dat, logFC < -2 ), points(logFC, -log10(PValue), pch=20, col="red"))
abline(h = -log10(0.05), col = 'red', lty = 3)
