# CAFE

## `Cafe_cleaner.jl`

This Julia script filters an input tab-separated value (TSV) file 
containing counts of genes for each species in different gene families. 
The purpose of the script is to prepare the input file for use with the 
program CAFE, which models the evolution of gene families. The script 
takes command line arguments to adjust the filtering criteria. The 
script performs the following steps:

1. Load the necessary Julia packages, including CSV, DataFrames, and ArgParse.

2. Parse the command line arguments, which include the minimum number of non-zero values in a row, the input TSV file name, the output file name, and the maximum difference between the minimum and maximum value in a row.

3. Load the input TSV file into a DataFrame.

4. Remove the "Total" column from the DataFrame.

5. Drop the first column (gene family names) and count the number of non-zero values in each row. Keep only rows where the number of non-zero values is greater than or equal to the minimum specified by the user.

6. Calculate the difference between the maximum and minimum value in each row, and keep only rows where this difference is less than the maximum specified by the user.

7. Add a new first column with the name "(null)" and the value "(null)" in every row.

8. Write the resulting filtered DataFrame to a new TSV file with the specified name.

9. Print the size of the resulting DataFrame to the console.

### Usecase

### Input

### Output

## `cafe_cleaner.py`

*This is the python version of `cafe_cleaner.jl`*

This Python script filters an input tab-separated value (TSV) file containing counts of genes for each species in different gene families. The purpose of the script is to prepare the input file for use with the program CAFE, which models the evolution of gene families. The script takes command line arguments to adjust the filtering criteria. The script performs the following steps:

1. Load the necessary Python packages, including pandas and argparse.

2. Parse the command line arguments, which include the minimum number of non-zero values in a row, the input TSV file name, the output file name, and the maximum difference between the minimum and maximum value in a row.

3. Load the input TSV file into a DataFrame.

4. Remove the "Total" column from the DataFrame.

5. Drop the first column (gene family names) and count the number of non-zero values in each row. Keep only rows where the number of non-zero values is greater than or equal to the minimum specified by the user.

6. Calculate the difference between the maximum and minimum value in each row, and keep only rows where this difference is less than the maximum specified by the user.

7. Add a new first column with the name "(null)" and the value "(null)" in every row.

8. Print the size of the resulting DataFrame to the console.

9. Write the resulting filtered DataFrame to a new TSV file with the specified name.

The main difference between this script and the Julia script is that this script uses pandas library to load and manipulate the data, whereas the Julia script uses DataFrames package. Additionally, the syntax for some operations (e.g., dropping columns) and adding a new column differs between the two scripts.

### Usecase

### Input

### Output

# Cafe/Trees

## `traverse_cafe_tree.py`

#### Usecase

The trees per family produced by cafe come with their own node names and leaf names. The names follow the format "<numerical id\>_count}"(for nodes) and "<supplied leaf name\><numerical id\>_count" (albeit the leaf names take hint from old leaf names, the node names are parsed using cafe's own parsing technique and it is not the same as ggtree's). This means we need a way to supply a list of "<numerical id\>" and in return get the whole id in the cafe generated newicks.

After which we need to find the parents, siblings and children for nodes of interest.

#### Input

Sample operation: `python3 nodewalker.py --list list1.txt --tree OG0000010.tre --output test.tsv `

Here:

- list - List of `<numerical ids\>`, one per line.
- Tree - Tree of interest.
- Output - Name of the of the output file.

#### Output

A tsv file with node, parents, children and siblings listed and the extraneous characters from the node names remvoed. For example:

| node  | parent | children                                                | siblings    |
| ----- | ------ | ------------------------------------------------------- | ----------- |
| <221> | <222>  | Nothoceros_vincentianus<219>,Leiosporoceros_dussii<218> | <221>,<220> |
| <217> | <220>  | <215>,<214>                                             | <217>,<216> |
| <207> | <213>  | <201>,<200>                                             | <207>,<206> |
| <79>  | <106>  | <67>,<66>                                               | <79>,<78>   |
| <206> | <213>  | <199>,<198>                                             | <207>,<206> |
| <205> | <212>  | Isoetes_tegetiformans<197>,<196>                        | <205>,<204> |
| <204> | <212>  | <195>,<194>                                             | <205>,<204> |

## list_significant_families.py

### Dependencies

- `traverse_cafe_tree.py`

### Usecase

Once we have the output from `traverse_cafe_tree.py`, we need to find the gene families that demonstrate significance for all of the nodes in each table from `traverse_cafe_tree.py`. This is what this script is for.

### Input

Sample run command: `python3 list_significant_families.py --table test.tsv --trees Base_asr.tre --output families` 

Params:

- table -> A table with list of nodes (cafe parsed) in each cell.
- Trees -> The `base_asr.tre` from cafe.
- Output -> The base name for the output files (one for the names and one for the counts).

### Output

- {output}.count

A table for the count in each cell.

| node | parent | children | siblings |
| ---- | ------ | -------- | -------- |
| 10   | 1      | 16       | 10       |
| 4    | 4      | 15       | 4        |
| 10   | 13     | 2        | 10       |
| 6    | 7      | 9        | 6        |
| 4    | 13     | 23       | 10       |
| 4    | 2      | 49       | 4        |
| 28   | 2      | 8        | 4        |

- {output}.names

A table for the names in each cell.

| node                                                                                                                                                                                                                                                                                    | parent                                                                                                                            | children                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | siblings                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| OG0000022,OG0000023,OG0000024,OG0000077,OG0000079,OG0000080,OG0000142,OG0000154,OG0000234,OG0000586                                                                                                                                                                                     | <br>                                                                                                                              | OG0000023,OG0000050,OG0000053,OG0000059,OG0000062,OG0000083,OG0000106,OG0000127,OG0000196,OG0000201,OG0000232,OG0000256,OG0000286,OG0000467,OG0000586,OG0001386                                                                                                                                                                                                                                                                                                                                           | OG0000022,OG0000023,OG0000024,OG0000077,OG0000079,OG0000080,OG0000142,OG0000154,OG0000234,OG0000586 |
| OG0000141,OG0000299,OG0000350,OG0000980                                                                                                                                                                                                                                                 | OG0000022,OG0000080,OG0000083,OG0000586                                                                                           | OG0000060,OG0000083,OG0000113,OG0000175,OG0000292,OG0000305,OG0000313,OG0000338,OG0000363,OG0000467,OG0000544,OG0000553,OG0000677,OG0000904,OG0001116                                                                                                                                                                                                                                                                                                                                                     | OG0000141,OG0000299,OG0000350,OG0000980                                                             |
| OG0000053,OG0000101,OG0000109,OG0000123,OG0000161,OG0000232,OG0000260,OG0000306,OG0000312,OG0000636                                                                                                                                                                                     | OG0000028,OG0000037,OG0000058,OG0000075,OG0000098,OG0000141,OG0000179,OG0000282,OG0000298,OG0000312,OG0000427,OG0000895,OG0001185 | OG0000232,OG0000344                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | OG0000053,OG0000101,OG0000109,OG0000123,OG0000161,OG0000232,OG0000260,OG0000306,OG0000312,OG0000636 |
| OG0000129,OG0000287,OG0000373,OG0000405,OG0000866,OG0001153                                                                                                                                                                                                                             | OG0000071,OG0000260,OG0000263,OG0000338,OG0000390,OG0000520,OG0001761                                                             | OG0000059,OG0000119,OG0000140,OG0000308,OG0000312,OG0000348,OG0000556,OG0000653,OG0001386                                                                                                                                                                                                                                                                                                                                                                                                                 | OG0000129,OG0000287,OG0000373,OG0000405,OG0000866,OG0001153                                         |
| OG0000061,OG0000084,OG0000146,OG0001153                                                                                                                                                                                                                                                 | OG0000028,OG0000037,OG0000058,OG0000075,OG0000098,OG0000141,OG0000179,OG0000282,OG0000298,OG0000312,OG0000427,OG0000895,OG0001185 | OG0000028,OG0000047,OG0000061,OG0000064,OG0000086,OG0000095,OG0000101,OG0000129,OG0000146,OG0000149,OG0000152,OG0000166,OG0000183,OG0000187,OG0000255,OG0000305,OG0000376,OG0000382,OG0000416,OG0000472,OG0000502,OG0000653,OG0001238                                                                                                                                                                                                                                                                     | OG0000053,OG0000101,OG0000109,OG0000123,OG0000161,OG0000232,OG0000260,OG0000306,OG0000312,OG0000636 |
| OG0000022,OG0000170,OG0000597,OG0000636                                                                                                                                                                                                                                                 | OG0000083,OG0000586                                                                                                               | OG0000022,OG0000023,OG0000024,OG0000034,OG0000046,OG0000063,OG0000064,OG0000078,OG0000079,OG0000083,OG0000084,OG0000089,OG0000093,OG0000101,OG0000113,OG0000115,OG0000120,OG0000136,OG0000138,OG0000140,OG0000141,OG0000174,OG0000175,OG0000195,OG0000197,OG0000217,OG0000232,OG0000238,OG0000240,OG0000258,OG0000275,OG0000286,OG0000287,OG0000290,OG0000292,OG0000299,OG0000301,OG0000305,OG0000312,OG0000316,OG0000407,OG0000467,OG0000478,OG0000560,OG0000597,OG0000653,OG0000682,OG0000980,OG0001238 | OG0000022,OG0000170,OG0000597,OG0000636                                                             |
| OG0000019,OG0000022,OG0000033,OG0000037,OG0000047,OG0000064,OG0000077,OG0000083,OG0000084,OG0000086,OG0000098,OG0000110,OG0000111,OG0000130,OG0000132,OG0000154,OG0000156,OG0000170,OG0000177,OG0000215,OG0000222,OG0000232,OG0000299,OG0000324,OG0000326,OG0000335,OG0000389,OG0001192 | OG0000083,OG0000586                                                                                                               | OG0000028,OG0000097,OG0000101,OG0000302,OG0000462,OG0000497,OG0000502,OG0000586                                                                                                                                                                                                                                                                                                                                                                                                                           | OG0000022,OG0000170,OG0000597,OG0000636                                                             |

# Cafe/Trees/Visualize

## `cafe_tree.R`

### Usecase

The trees that cafe produces in `Base_asr.tre` have their own convention for labelling the nodes. It makes more sense to visualize these with the node labels supplied in the trees.

### Input

Example: `Colored_tree.R --table Highlight_scheme.tsv --tree OG0000010.tre --plot optparse.pdf`

Where

`Highlight_scheme.tsv` is a delimited table with two rows `Nodes`(for the nodes to be highligted) and `Names` for the nodes' names.

Example table

| Name                     | Node |
| ------------------------ | ---- |
| Outgroup                 | 116  |
| Outgroup                 | 114  |
| Heterosporous Lycophytes | 210  |
| Homosporous Lycophytes   | 216  |
| Heterosporous ferns      | 188  |
| Homosporous ferns        | 172  |
| Angiosperms              | 122  |

`.tre` file is a newick file.

### Output

A plot with highlights for focal nodes. Different clades will have different colors. The labels won't be generated by parsing rather the node labels supplied within will be respected.

## `Highlight_nodes.R`

### Usecase

Highlighting clades can be a useful way to illustrate species trees. This is where this script comes in.

### Input

Example: `Colored_tree.R --table Highlight_scheme.tsv --tree OG0000010.tre --plot optparse.pdf`

Where

`Highlight_scheme.tsv` is a delimited table with two rows `Nodes`(for the nodes to be highligted) and `Names` for the nodes' names.

Example table

| Name                     | Node |
| ------------------------ | ---- |
| Outgroup                 | 116  |
| Outgroup                 | 114  |
| Heterosporous Lycophytes | 210  |
| Homosporous Lycophytes   | 216  |
| Heterosporous ferns      | 188  |
| Homosporous ferns        | 172  |
| Angiosperms              | 122  |

`.tre` file is a newick file.

### Output

A plot with highlights for focal nodes. Different clades will have different colors. The labels will be generated by parsing the tree.

## `colortree.R`

The following R script does the following:

1. Load the necessary libraries: ggtree, phylobase, dplyr, and textshape.
2. Set the names of the newick file and TSV file to be used.
3. Read in the newick tree from the file specified in `newick_file` using the `read.tree()` function from phylobase.
4. Read in the TSV file from the file specified in `tsv_file` using the `read.table()` function from base R.
5. Convert the `tree` object to a `phylo4` object using `as(tree, 'phylo4')`.
6. Define a function `value_to_color()` that maps the values in the `value` column of the TSV file to colors based on whether they are positive, negative, or zero.
7. Add a new column `color` to the TSV file by applying the `value_to_color()` function to the `value` column using `sapply()`.
8. Remove the `node_name` column and set the row names to be the `node_name` column using `column_to_rownames()` from textshape.
9. Create a `phylo4d` object by adding the TSV data to the tree using `phylo4d()`.
10. Plot the tree using `ggtree()` with the `color` column mapped to node colors using the `aes()` function.

## `tip_or_node.pl`

This Perl script takes a file as input, processes its contents, and outputs the result to a new file with a ".typed" extension. The script performs the following steps:

1. Check if a filename was provided as an argument; if not, print an error message and exit.
2. Set the input and output filenames.
3. Open the input file for reading and the output file for writing.
4. Read the input file line by line.
5. For each line, remove the newline character and split the line by tab characters into an array called @fields.
6. Check the first element of the @fields array. If it contains any letters (upper or lowercase), set the variable $type to "species"; otherwise, set it to "other".
7. Print the $type variable followed by the original fields, separated by tab characters, to the output file. Add a newline character at the end of each line.
8. Close the input and output files.
9. Print a message indicating that the output has been written to the output file with a ".typed" extension.

In summary, this script reads data from an input file and outputs the data to a new file with an additional column that indicates whether the first field of each line contains a letter or not (classified as "species" or "Node").

### Usecase

Cafe produces tabulated data that looks like:

| #Taxon_ID                    | Change |
| ---------------------------- | ------ |
| <154>                        | 2039   |
| <210>                        | 1443   |
| <221>                        | 37     |
| Nothoceros_vincentianus<219> | 1925   |
| Timmia_austriaca<203>        | 1421   |
| <149>                        | 535    |
| Physcomitrella_patens<202>   | 2194   |
| <74>                         | 196    |
| Ceratophyllum_demersum<118>  | 601    |

**But** it would be more useful to have this data as:

| Type    | #Taxon_ID                    |      |
| ------- | ---------------------------- | ---- |
| Node    | <154>                        | 2039 |
| Node    | <210>                        | 1443 |
| Node    | <221>                        | 37   |
| species | Nothoceros_vincentianus<219> | 1925 |
| species | Timmia_austriaca<203>        | 1421 |
| Node    | <149>                        | 535  |
| species | Physcomitrella_patens<202>   | 2194 |
| Node    | <74>                         | 196  |
| species | Ceratophyllum_demersum<118>  | 601  |

This is where this script comes in handy.

### Input

Supply the extension of the files and the pattern (default = "ID="). Example `perl tip_or_node.pl {input file name here}`

### Output

The script, given exptected input, should produce a file that has a new first column named `Type` and the file itself should be name `{old name}.type`.

# NGS

## `change_headers_per_assembly.pl`

The Perl code reads all the files in the current directory that have an extension matching the first command line argument. For each file, it reads it line by line, finds and extracts the first word that starts with "ID=", prefixes it with ">", and writes it to a new file with the same name but with the prefix "new_" and the same extension.

This code transforms the input files by adding a ">" symbol before every occurrence of the word that starts with "ID=" and writes the modified content to new files.

Here is an explanation of the code:

1. The first two lines of the code enable strict and warning checks during execution, preventing errors and warnings.

2. Then, the script reads the first command line argument, which is the file extension that we want to process.

3. For each file with the matching extension and that does not start with a '.', the script reads it line by line.

4. The script uses a regular expression to find the first occurrence of a word that starts with "ID=" in each line.

5. When it finds such a word, it prefixes it with ">" and writes the modified line to a new file with the same name and the prefix "new_" and the same extension.

6. If a line does not contain the pattern "ID=", it writes the original line to the output file.

7. Finally, the script closes all the files it opened and completes the directory iteration.

Note that the File::Basename module is used to get the base name of the input file, which is then used to construct the output file name.

### Usecase

Some phytozome assemblies do contain extraneous characters in their headers. They usually have the useful header name just the same but mixed-in with other useless stuff. To account for this we can use regex to select the useful header. This is where this script comes in handy.

### Input

Supply the extension of the files and the pattern (default = "ID="). Example `perl script.pl --extension txt --pattern_word document`

### Output

The script should produce files that have headers with the extraneous strings removed and only has the relavant `>{name here}`.

## `call_datasets.sh`

This is a bash script that downloads the summary data for complete genomes of a list of species from the NCBI datasets using the NCBI datasets command-line interface. The script takes one command-line argument, which is a file containing a list of species names (one per line).

The script uses a `for` loop to iterate over each line in the input file. For each species, it creates a filename by replacing any spaces in the species name with underscores and appending a `.json` extension. Then, it uses the `datasets summary genome taxon` command to get summary information for all complete genomes for that species and saves the output to the corresponding file. The `--assembly-level complete` option ensures that only complete genomes are included in the summary information.

The variable `n` is not used in the script and can be removed. The `IFS=$'\n'` line sets the Internal Field Separator variable to a newline character, which ensures that each line in the input file is processed as a separate item in the `for` loop.

## `download_onekp.R`

This R script downloads peptide sequences from the OneKP (One Thousand Plant Transcriptomes) database for a list of species.

First, the script loads the `onekp` package and retrieves the metadata for all OneKP sequences using the `retrieve_onekp()` function. Then, it reads a file called `list_of_codes.txt` which is assumed to contain a list of species codes (one per line, with no extraneous characters).

The `filter_by_code()` function is used to select only the sequences corresponding to the species codes in the list. Finally, the `download_peptides()` function is used to download the peptide sequences for the selected sequences and save them in the directory `hundred/Onekpdownload`.

## `get_highest_score_from_onekp.py`

This Python script takes two files as input: an original onekp data file and a list of species of interest, and produces a list of codes for the species of interest.

First, the script imports the necessary libraries: os, pandas, and argparse. argparse is used to create command-line interfaces, making it easy for users to provide input to the script. Then, a parser object is created, which describes the arguments that the script can accept. Two arguments are defined: `--o` for the onekp data file location and `--l` for the list of species of interest.

The `main()` function is defined, which is the main body of the script. The function checks if the input files exist and reads the species names from the list of species of interest file. It removes any newline characters from the end of the lines.

If the onekp data file is in Excel format, it is read using `pd.read_excel()`. If it is in TSV format, it is read using `pd.read_csv()` with a tab separator. If neither Excel nor TSV formats are detected, an error message is displayed.

The script then filters the data frame to only include the rows for the species of interest. It groups the data by species and selects the rows with the highest `% BUSCOs (complete+fragmented)` score for each species. The resulting data frame contains the 1KP Index IDs for the species of interest with the highest BUSCO score.

Finally, the script writes the 1KP Index IDs to a text file named "List_of_codes.txt" and displays a message indicating that the output file has been created.

## `parse_datasets_json.jl`

This Julia script is designed to process JSON files produced by NCBI Datasets, and output a TSV file with two columns: Species_name (Name of species) and Counts (Counts of complete genomes in NCBI databases).

The script first sets up the command line arguments using the ArgParse package. It expects the location of the directory containing the JSON files using the `--dir` flag (with the current directory as the default), and the desired output filename using the `--o` flag (with "counts.tsv" as the default).

The script then checks if there are any JSON files in the specified directory and if the output file already exists. If either of these conditions is not met, the script raises an error.

Next, the script opens the output file and writes the header row with the column names "species_name" and "count".

Then, for each JSON file in the directory, the script parses the file and extracts the species name and the count of complete genomes. It then formats the data into a TSV line and writes it to the output file.

Finally, the script closes the output file and the program finishes.

## `synchronize_headers.py`

This Python script synchronizes the headers and sequences of the onekp dataset. It takes four input arguments: `--pep`, `--cds`, `--sync`, and `--miss`, which are the locations of the peptide files, cds files, synced files, and files showing missing sequences, respectively. It also takes two optional arguments: `--pepext` and `--nucext`, which are the extensions of the peptide and cds files, respectively. If these optional arguments are not supplied, the default extensions `faa` and `cds` will be used.

The script first checks whether the supplied location actually exists. Then, it reads in the peptide and cds files and counts the number of headers in each file. After that, it identifies the headers that are missing in the cds files and writes them to a file. It also logs the number of missing sequences for each file.

Finally, it synchronizes the headers and sequences of the peptide and cds files that have the same headers and writes the synchronized files to the `--sync` directory.

---

---

The folders are demarcated accoridng to the language they hold. This repo is for scripts/code and scripts/code only. Actual data files can be easily replicated and as such I have decided to document how to generate data instead of storing it here. 

# Bash

## `Auto_concatanate.sh`

This is a Bash script that concatenates multiple files located in subdirectories of the current directory into a single file, with the extension `.cat`, and stores it in the `~/Desktop/dump` directory.

Here is a step-by-step breakdown of what the script does:

1. The first line `#!/bin/bash` specifies the interpreter that will run the script, in this case, Bash.
2. The second line `mkdir -p ~/Desktop/dump` creates a new directory named `dump` on the user's desktop (`~/Desktop/`), if it does not already exist. The `-p` option creates the directory and any intermediate directories as needed.
3. The `for folder in *` loop iterates over all subdirectories in the current directory.
4. The `for file in $folder/*` loop iterates over all files in each subdirectory.
5. The line `test_name="${folder}.cat"` sets a variable `test_name` to the name of the subdirectory followed by the extension `.cat`. This will be the name of the concatenated file.
6. The line `cat $file/* >> ~/Desktop/dump/$test_name` concatenates all files in the subdirectory (`$file/*`) and appends the result to the end of the concatenated file in the `dump` directory (`~/Desktop/dump/$test_name`).
7. The script ends by printing a confirmation message to the console, stating that all concatenated files are now in the `dump` directory on the user's desktop and have the extension `.cat`.

## `Auto_gdown.sh`

This Bash script downloads files from Google Drive using the `gdown` command. It takes one argument, which is the path to a file containing a list of links to Google Drive files, with each link on a separate line.

Here is a step-by-step breakdown of what the script does:

1. The first line `#!/bin/bash` specifies the interpreter that will run the script, in this case, Bash.
2. The line `IFS=$'\n'` sets the input field separator (IFS) to a newline character. This is done to ensure that spaces in filenames do not cause issues when iterating through the lines in the file.
3. The line `list=$1` sets the variable `list` to the first command-line argument, which should be the path to a file containing a list of links to Google Drive files.
4. The line `lines=$(cat $list)` reads the contents of the file specified by `list` into a variable called `lines`.
5. The line `n=1` initializes a counter variable `n` to 1.
6. The `for line in $lines` loop iterates over each line in the file specified by `list`.
7. The line `gdown $line` downloads the file from the Google Drive link specified by `$line` using the `gdown` command. This assumes that the `gdown` command is installed and configured properly on the system.
8. The loop continues until all lines in the file have been processed.
9. The script ends, and the downloaded files should be available in the current directory.

## `automate_hyphy.sh`

This Bash script processes a set of input files with the extension `.pal` using the HYPHY software package. It assumes that HYPHY is installed and configured properly on the system.

Here is a step-by-step breakdown of what the script does:

1. The first line `#!/bin/bash` specifies the interpreter that will run the script, in this case, Bash.
2. The line `for file in *.pal` starts a loop that iterates over all files in the current directory with the extension `.pal`.
3. The line `base_name="$(basename $file .pal)"` extracts the base filename of the `.pal` file (i.e., the filename without the extension).
4. The line `new_ext=".pal.treefile"` sets a new extension `.pal.treefile` that will be used for the output file.
5. The line `treefile="$base_name$new_ext"` creates a new filename by appending the base filename with the new extension.
6. The line `echo` (echo "1"; echo "6"; echo $file; echo $treefile) | hyphy`` runs the `hyphy` command, passing it a series of input commands through the `echo` command. Specifically, it sets the first input parameter to `1` (for "likelihood-based selection"), the second input parameter to `6` (for "model selection using AIC"), the third input parameter to the current `.pal` file, and the fourth input parameter to the new filename with the `.pal.treefile` extension. The output of the command is printed to the console, which presumably contains information on the results of the analysis.
7. The loop continues until all `.pal` files in the current directory have been processed.
8. The script ends.

## `Auto_taxon.sh`

This Bash script appears to be a script for querying the NCBI taxonomy database using the `esearch`, `efetch`, and `xtract` utilities. The script takes a list of query terms as input and processes each query term in the list.

Here is a step-by-step breakdown of what the script does:

1. The first line `#!/bin/bash` specifies the interpreter that will run the script, in this case, Bash.
2. The line `IFS=$'\n'` sets the input field separator (IFS) to a newline character. This is done to prevent issues with spaces in the query terms.
3. The line `list=$1` assigns the first argument passed to the script as the input file containing a list of query terms.
4. The line `lines=$(cat $list)` reads the contents of the input file into a variable `lines`.
5. The line `n=1` sets a variable `n` to 1, which will be used to number the output for each query term.
6. The `for` loop `for line in $lines` iterates over each query term in the input file.
7. The line `echo "$n.$line"` prints the current query term with a number prefix to the console.
8. The line `esearch -db taxonomy -query "$line"` uses the `esearch` utility to search the NCBI taxonomy database for the current query term.
9. The line `efetch -format native -mode xml` uses the `efetch` utility to retrieve the taxonomy data for the current query term in XML format.
10. The line `xtract -pattern Taxon -block "*/Taxon" -unless Rank -equals "no rank" -tab "\n" -element Rank,ScientificName` uses the `xtract` utility to extract taxonomic information from the XML data. Specifically, it extracts the `Rank` and `ScientificName` elements for each taxonomic unit (excluding those with a rank of "no rank") and outputs them as a tab-separated list with one line per taxonomic unit.
11. The line `echo -e "End of $line\n"` prints a message indicating that the query term has been processed.
12. The line `((n=n+1))` increments the variable `n` by 1, so that the output for each query term is numbered sequentially.
13. The loop continues until all query terms in the input file have been processed.

## `biostar_peptide_download_help_scripts_1.sh`

This Bash script appears to be a script for querying the NCBI protein database using the `esearch`, `esummary`, and `xtract` utilities. The script reads a list of species names from a file `species.txt`, and processes each species name in turn to obtain the accession numbers of protein sequences for that species.

Here is a step-by-step breakdown of what the script does:

1. The first line `#!/bin/bash` specifies the interpreter that will run the script, in this case, Bash.
2. The line `cat species.txt` reads the contents of the file `species.txt` to stdout.
3. The `while` loop `while read SPECIES` reads each line of the file `species.txt` into a variable `SPECIES`.
4. The line `esearch -db protein -query "${SPECIES} [orgn]"` uses the `esearch` utility to search the NCBI protein database for protein sequences from the current species.
   - The `-db protein` option specifies that the protein database should be searched.
   - The `-query "${SPECIES} [orgn]"` option specifies the search query, which consists of the current species name followed by the search term `[orgn]`, which limits the search to records where the species name is mentioned in the organism field.
5. The line `esummary` uses the `esummary` utility to retrieve summary information for the search results.
6. The line `xtract -pattern DocumentSummary -element AssemblyAccession` uses the `xtract` utility to extract the `AssemblyAccession` element from the summary information for each search result, which corresponds to the accession number of the protein sequence.
   - The `-pattern DocumentSummary` option specifies the pattern to match in the XML summary data.
   - The `-element AssemblyAccession` option specifies the element to extract from each matching pattern.
7. The script prints the accession numbers of the protein sequences for the current species to stdout.
8. The loop continues until all species names in the file `species.txt` have been processed.

## `biostar_peptide_download_help_scripts_2.sh`

This Bash script appears to be a script for querying the NCBI Datasets API to obtain information on genomes for a list of species. The script reads a list of species names from a file `species.txt`, and for each species, it queries the API to obtain the scientific name, taxonomy ID, and accession number of all assemblies of the species.

Here is a step-by-step breakdown of what the script does:

1. The first line `#!/bin/bash` specifies the interpreter that will run the script, in this case, Bash.
2. The line `cat species.txt` reads the contents of the file `species.txt` to stdout.
3. The `while` loop `while read SPECIES; do` reads each line of the file `species.txt` into a variable `SPECIES`.
4. The line `datasets summary genome taxon "${SPECIES}" --reference` uses the `datasets` utility to query the NCBI Datasets API for information on all genomes of the current species.
   - The `summary genome` option specifies that the summary information for genomes should be retrieved.
   - The `taxon "${SPECIES}"` option specifies the taxonomy name of the species to be queried.
   - The `--reference` option specifies that only reference genomes should be included in the summary information.
5. The output of the `datasets` command is piped (`|`) to the `jq` utility.
6. The `jq` command `-r` option specifies that the output should be in raw format (without quotes).
7. The `jq` command `'[.assemblies[].assembly | .org.sci_name,.org.tax_id,.assembly_accession] | @tsv'` selects the relevant fields from the JSON output and formats them as a tab-separated list.
   - The `.assemblies[].assembly` selector selects the assembly objects from the summary data.
   - The `|` operator passes the assembly objects to the next selector.
   - The `.org.sci_name` selector selects the scientific name of the organism for each assembly.
   - The `,` operator separates the selectors for the tab-separated output.
   - The `.org.tax_id` selector selects the taxonomy ID of the organism for each assembly.
   - The `,` operator separates the selectors for the tab-separated output.
   - The `.assembly_accession` selector selects the accession number of the assembly for each organism.
   - The `@tsv` operator formats the output as a tab-separated list.
8. The script prints the tab-separated list of scientific name, taxonomy ID, and accession number of all assemblies for the current species to stdout.
9. The loop continues until all species names in the file `species.txt` have been processed.

## `properline.sh`

This Bash script converts a set of FASTA files (files with the `.fa` extension) to a new format, where all sequences are aligned and concatenated into a single line, separated by newline characters.

The script first loops through all `.fa` files in the current directory, and for each file, it:

1. Extracts the basename of the file (i.e., the filename without the `.fa` extension)

2. Appends a new file extension `.afa` to the basename to create a new filename

3. Uses `awk` to read through the FASTA file, and for each sequence:
   
   a. If it's the first sequence in the file, print the sequence header (starting with ">") and sequence data (one or more lines of letters).
   
   b. If it's not the first sequence, print a newline character followed by the sequence header and sequence data, all on one line (i.e., concatenated).

4. Writes the output to a new file with the name created in step 2.

Therefore, the output of this script will be a set of new `.afa` files, each containing all the sequences from the original `.fa` file concatenated together and separated by newline characters.

## `remove_by_extension.sh`

This script takes in command-line arguments with optional flags `-t/--target` and `-e/--ext` to specify the target directory and file extension to look for, respectively.

It then goes through all the files in the target directory that match the specified extension, creates a wildcard string that matches any file with the same basename but any extension, and then removes all such files using `rm`.

In summary, this script recursively deletes files with the same basename and any extension as the specified target files in the specified directory.

## `rmfna.sh`

This bash script removes the directory `FNA` in every subdirectory of the current working directory.

The script iterates over every folder in the current working directory, and for each folder, it attempts to remove the `FNA` directory within it using the `rm` command with the `-r` flag to recursively remove any subdirectories and files within `FNA`. If `FNA` doesn't exist in a folder, the command to remove it will fail silently without any error message.

## `rsync_by_extension.sh`

This bash script copies all files with a certain file extension (`$extension`) from a source directory (`$target`) to a destination directory (`$destination`). It uses the `rsync` command to perform the copy operation.

The script accepts three optional command line arguments:

- `-t` or `--target`: specifies the source directory.
- `-d` or `--destination`: specifies the destination directory.
- `-e` or `--ext`: specifies the file extension to copy.

If any other command line argument is passed, the script will output an error message and exit.

The script first sets the `$target` and `$destination` variables based on the command line arguments and the current working directory. Then it calls `rsync` with the appropriate arguments to copy all files with the specified extension from the source directory to the destination directory while preserving directory structure.

## `seqkit_automation.sh`

This bash script processes all the `.fa` files in the current directory and for each file, it removes duplicate sequences using the `seqkit` tool and outputs the resulting sequences into a new file with the `.afa` extension. The script first defines a `for` loop that iterates through each `.fa` file in the current directory.

Inside the loop, the script extracts the base name of the input file (without the `.fa` extension) using the `basename` command and stores it in the variable `$base_name`. It then appends the `.afa` extension to the base name and saves the resulting string in the variable `$new_file`.

The script then executes the `seqkit rmdup -s` command, where `rmdup` removes duplicate sequences and `-s` sorts the sequences before removal of duplicates. The `< $file` syntax tells the `seqkit` command to read the input from the current `.fa` file, and the `> $new_file` syntax redirects the output to the new `.afa` file.

Overall, the script is useful for preprocessing genomic sequences before downstream analysis.

## `subfolder.sh`

This bash script will split files in the current directory into multiple directories, each containing a maximum of 2500 files (or less if there are fewer than 2500 files remaining). The new directories will be named "folder1", "folder2", and so on.

The script first sets two variables, `dir_size` and `dir_name`, which represent the maximum number of files per directory and the name of the new directories, respectively. Then it calculates the number of new directories needed by dividing the total number of files in the current directory by `dir_size` and rounding up to the nearest integer.

In the loop, the script creates a new directory using `mkdir -p` and the name `"$dir_name$i"`, where `$i` is the loop counter. It then uses `find` to get a list of all files in the current directory, `head` to limit the list to the next `dir_size` files, and `xargs` to move those files to the new directory just created. The process is repeated until all files have been moved to the new directories.

## `sync.sh`

This Bash script takes in three arguments using flags: `--first_directory`, `--second_directory`, and `--third_directory`.

Then, for each file with the extension `.pal.treefile` in the directory specified by the `--first_directory` flag, it extracts the base name of the file (i.e., without the extension), adds `.pal` as a new extension, and constructs two new file names by concatenating the new extension with the base name and appending each to the second and third directories specified by the `--second_directory` and `--third_directory` flags, respectively.

Finally, the script copies the contents of the file located in the first directory and with the file name `$first_pal_name` to both of the newly created files in the second and third directories, whose names are `$second_pal_name` and `$third_pal_name`, respectively.

## `TarSucks.sh`

This Bash script creates a new directory named "extracted" and extracts all files with a .tar.bz2 extension in the current directory to a subdirectory in "extracted" with the same name as the original file (without the extension). It does this using a for loop that iterates over all .tar.bz2 files in the current directory, creates a directory in the "extracted" folder with the same name as the file (without the extension), and then extracts the contents of the file to that directory using the `tar` command. Finally, it prints a message indicating that all files have been extracted and can be found in the "extracted" directory.

## `test.sh`

This script first lists all files in the `long_enough` directory sorted by size (from largest to smallest) and assigns the list to the variable `list` using the `ls` command with options `-rS`. Then, for each file in the list, it extracts the filename without the `.fa` extension and appends `.afa` to it to create a new filename with the `.afa` extension. The script then prints the new filename to the console. However, it doesn't do anything with the new filename, such as creating a new file or renaming the original file.

# Python

## `csv_to_Rdb.py`

This Python script reads a CSV file called "Base_change.tab", and if the file contains more than one column separated by commas, it assumes the file is a CSV file and proceeds to create a Pandas DataFrame. If the CSV file contains only one column, the script prints a message saying that it probably is not a CSV file and then reads the file again, this time using tab-based separation. Then, the script creates a SQLite database named "test_database" and a table called "orthos". The columns in the DataFrame are used to create the table's columns, and the data from the DataFrame is inserted into the "orthos" table using the `to_sql()` method from the Pandas library. If the "orthos" table already exists in the "test_database" database, the script will replace it with the new data by setting the `if_exists` parameter to "replace" in the `to_sql()` method.

## `drop_nones.py`

This Python script is a command-line tool that takes in three input directories containing CDS files with 'None' coded transcripts, peptide files without 'None' coded transcripts, and a destination directory for output files. The script outputs files with only the intersection of headers between the CDS files and peptide files, removing all headers with 'None' transcripts in each file.

The script uses the argparse library to create command-line arguments. There are five arguments:

- "--peps": the path to the directory where the old peptide files with the superset of headers are. By default, it is set to "Default".
- "--cds": the path to the folders where the None-coded CDS files are.
- "--pepext": the extension of the peptide files. By default, it is set to ".pep".
- "--CDSext": the extension of the CDS files. By default, it is set to ".cds".
- "--out": the path to the location where the output files will be delivered.

The script then defines a function called "run" that takes the input directories, processes the files, and outputs them to the destination directory. The function first loops over the CDS files in the "--cds" directory, retains only their basename, and sets the output file path. The function then accesses the peptide files in the "--peps" directory and creates two dictionaries, one for the nucleotide sequences and one for the peptide sequences. The headers with 'None' transcripts are removed from the nucleotide dictionary. The function then loops over the nucleotide dictionary and writes the sequences with matching headers from the peptide dictionary to the output file.

The script then defines the main function that checks if the input and output directories are valid and calls the "run" function if they are. If any of the directories are invalid, the script outputs an error message and quits. Finally, the main function is called.

## `fasta_dicts.py`

This Python script converts all fasta files in a specified directory to pickled dictionaries, where the name of the sequence is the key and the sequence is the value. The fasta file extensions that are read by default are ".fna", ".faa", ".fa", and ".pep". The out files will always have the pickle extension.

The script uses the following packages:

- `pickle`: To create and write pickled objects
- `os`: To access the file system and parse the file paths
- `argparse`: To parse command-line arguments

The script defines an argument parser object to parse the command-line arguments. The command-line arguments that can be supplied are:

- `--loc`: The location of the directory where the fasta files are stored. The default location is the current folder.
- `--ext`: The extension of the files that should be pickled. If not supplied, all files with the default extensions will be pickled.

The `main()` function does the following:

- It first checks the directory specified in the command line or the current directory if no location is specified.
- It then finds all the fasta files in the directory with the specified extensions or all files if no extensions are specified.
- For each fasta file, it reads the file, parses the sequences, creates a dictionary with the sequence name as key and the sequence as the value, and writes the dictionary to a pickled file with the same name as the original file.

## `headers_only.py`

This Python script takes a directory containing fasta files and extracts
 the headers (lines starting with ">") from each file, then writes 
them to separate files with the extension ".hfa" in a specified output 
directory. The input and output directory locations can be specified as 
command-line arguments, and if not provided, the current directory will 
be used as the default input directory and a directory named "Headers" 
will be created in the same directory as the input directory for the 
output files.

## `list_nones.py`

This script searches through all files in the current directory, and for each file that has a '.none' extension, it extracts the headers of the sequences that have a corresponding sequence value of 'None', and writes them to a new file with the same name as the original file but with the '.none' extension.

Here is a breakdown of the code:

1. The script imports the 'os' package to access files in the file system.

2. The main function begins with a for loop that iterates over all files in the current directory using the 'os.listdir()' method.

3. For each file, the code extracts the file name by splitting the file name at the '.' character.

4. The code creates a new file name by appending the '.none' extension to the original file name.

5. The code reads the contents of the current file using the 'with open()' statement and saves each line as a separate string in the 'current_file_lines' list.

6. The code initializes an empty dictionary called 'file'.

7. The code iterates over each line of 'current_file_lines' and checks if the line is a header by checking if it starts with the '>' character.

8. If the line is a header, the code extracts the corresponding sequence value from the next line in 'current_file_lines'.

9. If the sequence value is 'None' (i.e., if it is equal to the string 'None' with no quotes), the header is added to the 'file' dictionary as a key, and the sequence value is added as the corresponding value.

10. The code then writes the header to the 'new_file' using the 'with open()' statement and the 'writer.write()' method.

## `make_cds_mirror.py`

This is a Python script that takes an orthogroup with peptide sequences and generates a corresponding orthogroup with CDS sequences. The script takes command-line arguments using argparse, which allows the user to specify the location of the pickled file with the species identification codes, the location of the CDS fasta dicts in pickle format, the location of the orthogroups, and the output files.

The script loads the species identification codes from the pickled file and iterates over the files in the specified orthogroups directory. For each file, it extracts the headers of the peptide sequences, identifies the species in each header using the most common subscript and dictified CDS fastas with similar headers, and generates a corresponding CDS orthogroup. The script writes the output to files in the specified output directory.

The script defines several functions to carry out the different steps of the process. The `write_to_file` function takes a file name and a dictionary containing the headers and CDS sequences and writes the CDS sequences to a file with the same name in the specified output directory. The `list_to_cds_sequences` function takes a file name and a list of peptide headers, identifies the species in each header using the species identification codes, retrieves the corresponding CDS sequences from the pickle files, and calls the `write_to_file` function to generate the CDS orthogroup. The `get_headers` function takes a file name, reads the peptide headers from the file, and calls the `list_to_cds_sequences` function to generate the CDS orthogroup. The `main` function iterates over the files in the orthogroups directory and calls the `get_headers` function for each file.

## `make_subtrees.py`

This is a Python script that takes in a CSV file with taxonomic information and a separate file with a list of species names to filter, and outputs a new file containing only the rows of the original CSV file that contain the species in the input list. The script uses the Pandas library to read in and manipulate the CSV file and the argparse library to create a command-line interface for specifying input and output files. The script reads in the input and list files specified in the command-line arguments, creates a list of species names from the list file, applies a boolean mask to the CSV file to select only the rows containing the species in the list, and then writes the selected rows to the output file. The script does not check whether the output file already exists, which could cause issues if the file already has content that should not be overwritten.

## `model_genes.py`

This is a Python script that uses the pandas library to manipulate a tab-separated file containing homologous gene families. The script allows the user to filter the families and species they are interested in, and output the results in two different formats: either as separate files for each family and each species, or as a table. The script uses argparse to handle command-line arguments and provides help for each option.

The script defines two functions: `text_output_manager` and `subset`.

`text_output_manager` is a helper function that creates folders for each species and family, reads the input dataframe, and writes a separate file for each family and each species. The function takes two arguments, `species_list` and `df`, which are the list of species and the dataframe containing the homologous gene families, respectively.

`subset` is the main function that reads the command-line arguments, reads the input file, filters the rows and columns based on the specified species and family lists, and calls `text_output_manager` to write the output files. The function uses the pandas `read_csv` function to read the input file and the `isin` method to filter the rows and columns based on the specified lists.

Overall, this script seems to be designed for a specific use case, where the user has a large matrix of homologous gene families and wants to extract a subset of families and species.

## `most_common_substring_in_headers.py`

This Python script takes the path to a folder containing FASTA files as input and parses the headers of those files to find the most common substring in the header. The output is a dictionary where the keys are the names of the FASTA files and the values are the most common substring in the header of each file.

The script uses the following libraries:

- `os`: to navigate the file system
- `difflib.SequenceMatcher`: to compare two strings
- `argparse`: to create CLI elements

The script uses `argparse` to parse the command-line arguments. It expects four optional arguments:

- `--loc`: The path to the folder that holds the FASTA files.
- `--out`: The name of the output file that will hold the output of the script.
- `--ext`: The extension of the files that should be parsed.
- `--Oform`: Whether or not to pickle the output. The default is not to pickle the output.

Once the command-line arguments are parsed, the script navigates to the folder containing the FASTA files and reads in the names of the files with the specified extension. For each file, the script reads in the first 10 lines and extracts the headers. It then compares the headers to find the most common substring and writes the results to a dictionary. If `--Oform` is set to "pickle", the output dictionary is pickled and written to a file.

## `name_dict.py`

This Python script reads an Excel file containing a list of species and their corresponding OneKP Index IDs, filters out the species that are not in a specified list, and creates a dictionary with the OneKP Index ID as the key and the species name as the value. The dictionary is then saved as a pickle file named "codename_realname.pickle".

The script uses argparse to accept two optional arguments: `--big_list` for the path to the Excel file containing the full list of species, and `--small_list` for the path to the file containing the list of species to filter. If these arguments are not provided, the script uses default values of `False`.

Here is a breakdown of the main steps in the script:

1. Import required libraries: `pandas`, `pickle`, and `argparse`.
2. Define the command-line arguments using `argparse`: `--big_list` and `--small_list`.
3. Parse the command-line arguments using `args = parser.parse_args()`.
4. Read the Excel file specified in `args.big_list` into a Pandas dataframe using `pd.read_excel()`.
5. Read the file specified in `args.small_list` into a list using `open().read().splitlines()`.
6. Filter the dataframe to include only the rows corresponding to the species in the list using `df2[df2['Species'].isin(species_list)]`.
7. Create a dictionary with the OneKP Index ID as the key and the species name as the value using a for loop and `df3.itertuples()`.
8. Save the dictionary as a pickle file named "codename_realname.pickle" using `pickle.dump()`.

## `onekp_datatable.py`

This Python script scrapes a website, [Public Release of Thousand Plants (1kP) Assemblies](http://www.onekp.com/public_data.html), for a table of data and converts it into a pandas dataframe. It then saves the dataframe as a tab-separated value (TSV) file named "Onekp_data.tsv" in the current working directory.

The script begins by importing the necessary libraries: requests, lxml, BeautifulSoup, and pandas. It then sets up the headers for the HTTP request and makes the request to the website using requests.get(). The response is stored in a BeautifulSoup object, which is then searched for the table element using find(). The rows of the table are then retrieved using findAll() and stored in the variable "rows".

The script then iterates over each row in "rows", extracting the cell elements and appending them to a new list called "row". If a cell element contains an <a> tag, the script extracts the href attribute and appends it to the "row" list. Otherwise, it extracts the text of the cell element and appends that to the "row" list. The completed "row" list is then appended to a larger list called "l".

Finally, the script converts the "l" list into a pandas dataframe and saves it as a TSV file using df.to_csv().

## `remove_pNs.py`

This Python script processes a directory of FASTA files by removing any nucleotides (represented by the letter 'N') from the sequences, and then writes the new FASTA files to a new file with the same name as the original file but with '.no_pNs.fna' appended to the end.

The script achieves this by iterating over each file in the current working directory using the `os.listdir()` method. It then opens each file using the `with` statement, reads the lines of the file, and stores them in a list called `current_file_lines`.

The script then creates an empty dictionary called `file`, which will be used to store the FASTA header and sequence data for each sequence in the file. It does this by iterating over the `current_file_lines` list using a `for` loop and an `enumerate` function to keep track of the index of each line. If a line starts with the '>' character (which indicates the start of a new sequence), and ends with the text 'p1' (which is presumably a specific identifier that the script author is interested in), the script assumes that the following line contains the nucleotide sequence for that sequence, and adds the header and sequence data to the `file` dictionary.

The script then iterates over the `file` dictionary, concatenates the header and sequence data for each sequence into a single string called `line`, and writes it to a new file with the same name as the original file but with '.no_pNs.fna' appended to the end using the `with` statement and the `writer.write()` method.

The script is executed by calling the `main()` function at the end.

## `select_columns.py`

This Python script is designed to make a subset of a Pandas DataFrame based on columns. It uses the argparse library to accept command-line arguments to specify the names of files and columns. Here is a brief description of what each part of the code does:

- Import the required libraries: `pandas` for data manipulation, and `argparse` for parsing command-line arguments.
- Create an argument parser object named `parser` to accept command-line arguments.
- Define three arguments for the parser: `--name_list`, `--old_file`, and `--new_file`. Each argument is defined with a description, default value, and help message.
- Parse the arguments using `parser.parse_args()`, and assign the resulting object to `args`.
- Define a function called `main()`.
- Inside the `main()` function, open the old file specified by the `--old_file` argument using `pd.read_csv()`.
- Open the file specified by the `--name_list` argument using `open()` and read the lines into a list of column names called `column_names`.
- Iterate over each item in `column_names`, strip the whitespace, and append it to a list of column names called `the_columns`.
- Filter the old DataFrame using `the_columns` using `old_dataframe.filter()`, and assign the resulting DataFrame to `new_dataframe`.
- Save the new DataFrame to a file specified by the `--new_file` argument using `new_dataframe.to_csv()`.

Overall, the script takes three command-line arguments: the name of a file containing a list of column names to keep, the name of the original file to filter, and the name of the new file to create with only the specified columns.

## `SRA_name_manager.py`

This is a Python script that modifies the headers of FASTA files. When you download a file from SRA, it may not always have the exact header that you want it to. This script is there to help with this very specific problem.

The script takes command line arguments, specifically the location of the folder containing the FASTA files to be modified. The `-l` flag is used for this purpose. If this flag is not provided, the program takes the current location as the address of execution.

The script defines several functions.

The `most_common_string()` function detects and returns the most common string in the headers so that they can be replaced. The `fasta_runner()` function opens and writes to the files. The `fastas_in_the_folder()` function generates the list of FASTA files to be modified. Finally, the `params()` function is where the majority of the action will take place, as it parses the command-line arguments and calls the other functions.

The modified headers are created by replacing spaces with underscores and appending the name of the file (without the `.fasta` extension) with a '>' sign in front of it. The modified headers are written to a new file, with the same name as the original file, except for the addition of the `.header_changed` suffix.

Note: the script uses the `difflib` module to find the most common substring in the headers throughout the FASTA file.

## `sync_peps_nuc.py`

This Python script reads all files in the current working directory, reads each file line by line, and writes a new file with the same name as the original file, but with a suffix of ".clean.fna". It does this by parsing each file and extracting the DNA sequence from each FASTA formatted file.

It accomplishes this by first iterating through each file in the directory using `os.listdir()`. For each file, it opens the file and reads its contents into a list of lines. Then, it creates a new dictionary called `file` to hold the header and sequence for each FASTA sequence in the file.

The script then iterates through the list of lines, looking for lines that start with the ">" character, which indicates the start of a FASTA header. When it finds a header, it extracts the sequence for that header from the next line, adds it to the `file` dictionary, and continues iterating through the lines. If the sequence for a header is "None", it skips that header and moves on to the next.

Finally, the script writes a new file with the name of the original file and the suffix ".clean.fna". It does this by iterating through the `file` dictionary and concatenating each header and sequence into a single string, which it then writes to the new file using the `write()` method of a file object opened in append mode (`'a'`).

## `uncode_names.py`

This Python script is a command-line tool that takes a pickled dictionary, a folder containing files with codes as file names, and a new folder location. The script renames the files in the old folder with the respective values in the dictionary and copies them to the new folder.

The script uses the `argparse` module to create a parser object that parses the command-line arguments. The script takes four optional arguments:

- `--pickle`: The location of the pickled dictionary with codes as keys and full names as values. Default value is 'Default'.
- `--old`: The location of the old files with codes as file names. The argument is mandatory and needs to be the full path in Unix format.
- `--new`: The location of the new folder where the renamed files will be pasted. The argument is mandatory and needs to be the full path in Unix format.
- `--ext`: The extension of the files to be processed. Default value is 'fa'.

The `main()` function reads the pickled dictionary, gets a list of the file names in the old folder, and iterates over the dictionary keys. If the key is in the list of file names, it renames the file with the corresponding value from the dictionary and copies it to the new folder. If a file with the same name already exists in the new folder, the script appends a number to the file name to avoid overwriting it.

The script uses the `shutil` module to copy and rename files and the `os` module to get the list of files in the old folder.

If the pickled dictionary cannot be opened or read, the script prints an error message.

## `use_dict_to_replace_strings.py`

This Python script is a command-line tool that takes in a file, a dictionary, and an output file name as arguments and replaces certain strings in the input file with new strings guided by the dictionary.

It uses the `argparse` library to parse command-line arguments and `pickle` to open the pickled dictionary. The command-line arguments are specified in the code with their corresponding descriptions and defaults.

The script opens the input file and reads its contents. It also opens the dictionary file and loads its contents into a dictionary. It then iterates through each line of the input file and replaces any string that matches a key in the dictionary with the corresponding value. Finally, it writes the modified lines to the output file.

# R

## `annotree.R`

This R script reads in a tab-separated file (`counts.tsv`) that contains species names and corresponding numbers. It then reads in a Newick file (`species_tree.newick`) containing a phylogenetic tree.

The script uses the `add_labels` function to add labels and numbers to the tree based on the species names and numbers read in from the `counts.tsv` file. The `add_labels` function also returns any missing numbers for labels and writes them to a log file if there are any.

After modifying the tree object to include labels and numbers, the script visualizes the tree using `ggtree` and saves it as a PDF (`species_tree_with_numbers.pdf`). The resulting tree has tip labels that include both species names and corresponding numbers, and node labels that include corresponding numbers. The visualization includes both tip labels and node labels, with the latter nudged slightly to avoid overlapping with the tree branches.

## `test_all_trees.R`

This R script uses the packages tidyverse, argparse, ggtree, TreeTools, and glue to perform the following task:

The purpose of this script is to take one or more phylogenetic trees and create a table indicating whether each tree is ultrametric, binary, and rooted or not. The script takes command-line input using argparse to allow the user to specify the location of the trees and the file extension of the trees to be processed. If no file extension is specified, the script will process all files with the ".tree" extension.

The script then reads each tree file, tests if each tree is ultrametric, binary, and rooted using the functions is.ultrametric(), is.binary(), and is.rooted() from the ggtree and TreeTools packages. It stores the results of the tests in vectors, and then creates a data frame from the vectors. The resulting data frame has four columns: Tree_name, Ultrametricity, Binaryness, and Rootedness. The script then writes the data frame to a CSV file named "test_binary_ultra_rooted.csv" in the same directory as the script.

## `Visualize_tree.R`

This R script uses the packages tidyverse and ggtree to perform the following task:

The script reads a phylogenetic tree from a file named "SpeciesTree_rooted.txt" located at the specified path "/home/rijan/Desktop/backup/push_to_hpc/". It then creates a ggtree object from the phylogenetic tree using the ggtree() function from the ggtree package. The branch length of the tree is set to 'none', which means that the branches will not be drawn. The theme_tree2() function is used to apply a pre-defined theme to the tree, and the geom_tiplab() function is used to add labels to the tips of the tree. The align argument of geom_tiplab() is set to TRUE to align the labels, and the linesize argument is set to 0.5 to adjust the spacing between the labels. The xlim() function is used to set the x-axis limits of the plot to 0 and 25.

The resulting plot is then saved as a PDF file named "test_2.pdf" using the ggsave() function from the ggtree package. The width and height of the PDF file are set to 60 and 80 cm, respectively, and the limitsize argument is set to FALSE to allow the plot to extend beyond the specified width and height if necessary.
