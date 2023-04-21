library(tidyverse)
library(argparse)
library(ggtree)
library(TreeTools)
library(glue)

# You need the following code to set up command-line input

parser <- ArgumentParser(description = 'The purpose of this script is to take one tree or a list of trees and then print a table to file that says where the said tree/s are ultramteric, binary and rooted or not. Please mind the flags you are supposed to supply to the script, anything you supply will be used otherwise the defaults will be supplied to the flags.')

parser$add_argument('--l', default =".",help="You should pass the location of your trees to this flag. The default is the folder that the script sits in.")

parser$add_argument('--e',default='None',help="If your trees have a specific extension then pass them here without the period. Otherwise all the files in the locaiton will be processed. Please note that the script can only take one extension at the time right now.")

args<- parser$parse_args() # this creates a list of the commandline args


ext_str <- args$e
alt_pattern <- glue('([^\\s]+(\\.(?i)({ext_str}))$)')

if( args$e == 'None'){
	pattern = "Null"
} else{
	pattern = alt_pattern
}	
list_of_files <- list.files(path=".", pattern = "([^\\s]+(\\.(?i)(tree))$)", all.files= FALSE, full.names=FALSE)


# We need the following vectors to create 
Tree_name <- c()

Ultrametricity <- c()

Binaryness <- c()

Rootedness <- c()

# this is where we will test the files to see if they are actually ultrametric
for(i in list_of_files){
  
  current_tree <- read.tree(i)
  test_ultra <- is.ultrametric(current_tree)
  test_binary <- is.binary(current_tree)
  test_rooted <- is.rooted(current_tree)
  
  Ultrametricity <- append(Ultrametricity,test_ultra)
  Tree_name <- append(Tree_name,i)
  Binaryness <- append(Binaryness,test_binary)
  Rootedness <- append(Rootedness,test_rooted)
}

df <- data.frame(Tree_name,Ultrametricity,Binaryness,Rootedness)

write.csv(df,"test_binary_ultra_rooted.csv", row.names = FALSE)
