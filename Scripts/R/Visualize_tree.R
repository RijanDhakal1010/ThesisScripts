library(tidyverse)
library(ggtree)

# the path to the tree files is

tree <- read.tree("/home/rijan/Desktop/backup/push_to_hpc/SpeciesTree_rooted.txt")
ggtree(tree,branch.length = 'none') + theme_tree2()+geom_tiplab(align=TRUE, linesize=.5)+ xlim(0,25)
ggsave("test_2.pdf", width = 60, height = 80, units = "cm", limitsize = FALSE)

