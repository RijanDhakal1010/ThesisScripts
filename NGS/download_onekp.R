# The goal of this script is to :
	# 1. Take a file with one code name per line as the input for the species to download from the onekp database
		# a. Download and install the onekp package if need be
	# 2. And download the files accoridingly
		# a. Ask for address before installing
		# b. If address not given then use an arbritary one

## The script is currently unvetted for defensive programming.



library(onekp)

# the following code is taken from the official onekp vignette from this point in time [https://web.archive.org/web/20201029141224/https://docs.ropensci.org/onekp/]. Things might have changed

onekp <- retrieve_onekp()

lines <- readLines("list_of_codes.txt") # please make sure that this file holds assembly file/ species name code in this format : one per line, with no extraneous characters.

seqs <- filter_by_code(onekp, lines)
download_peptides(seqs, 'hundred/Onekpdownload') # you may or may not need to make sure that the folders already exist.
