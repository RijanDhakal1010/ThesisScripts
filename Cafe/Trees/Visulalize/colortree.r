library(ggtree)
library(phylobase)
library(dplyr)
library(textshape)

newick_file <- "newick_file.nwk"

tsv_file <- "table.tsv"

# Read the newick tree
tree <- read.tree(newick_file)

# Read the TSV file
tsv_data <- read.table(tsv_file, header=TRUE, sep="\t")

treeobj = as(tree,'phylo4')

# Function to convert values into colors
value_to_color <- function(x) {
  if (x > 0) {
    return('green')
  } else if (x < 0) {
    return('red')
  } else {
    return('yellow')
  }
}

# Replace the 'value' column with the 'color' column
tsv_data$color <- sapply(tsv_data$value, value_to_color)
tsv_data <- tsv_data[, c("node_name", "color")]

tsv_data <- tsv_data %>% column_to_rownames( loc = 1)

# Create separate tibbles for nodes and tips
#node_tibble <- tsv_data %>% filter(type == "node") %>% select(node_name,color)
#tip_tibble <- tsv_data %>% filter(type == "tip") %>% select(node_name, color)

treeobj = phylo4d(treeobj,all.data = tsv_data)

ggtree(treeobj, aes(color=I(color)))
