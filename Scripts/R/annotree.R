# Load required libraries
library(ape)
library(ggtree)

# Read the TSV file with species and node names and numbers
# Make sure the TSV file has headers: "name", and "number"
data <- read.table("counts.tsv", header = TRUE, sep = "\t", fill = TRUE, colClasses = "character")

# Read the Newick file
newick_file <- "species_tree.newick"
tree <- read.tree(newick_file)

# Add labels and numbers to the tree
add_labels <- function(tree, data) {
  missing_numbers <- c()
  
  for (i in 1:nrow(data)) {
    label_name <- data$name[i]
    label_number <- data$number[i]
    if (label_name %in% tree$tip.label) {
      tip_index <- match(label_name, tree$tip.label)
      tree$tip.label[tip_index] <- paste(label_name, label_number, sep = ":")
    } else if (label_name %in% tree$node.label) {
      node_index <- match(label_name, tree$node.label)
      tree$node.label[node_index] <- paste(label_name, label_number, sep = ":")
    } else {
      missing_numbers <- c(missing_numbers, label_name)
    }
  }
  
  return(list(tree = tree, missing_numbers = missing_numbers))
}

# Modify the tree object to include labels and numbers
result <- add_labels(tree, data)
tree <- result$tree
missing_numbers <- result$missing_numbers

# Write missing labels to a log file
if (length(missing_numbers) > 0) {
  writeLines(c("Missing numbers for the following labels:", missing_numbers), "missing_labels.log")
}

# Convert factors to characters
tree$tip.label <- as.character(tree$tip.label)
tree$node.label <- as.character(tree$node.label)

# Visualize the tree
p <- ggtree(tree, layout = "rectangular") +
  geom_tiplab(size = 3) +
  geom_nodelab(size = 3, na.rm = TRUE, nudge_x = 0.008) +
  theme_tree2() +
  theme(legend.position = "none")

# Save the tree as a PDF
ggsave("species_tree_with_numbers.pdf", p, width = 20, height = 20, dpi = 300)
