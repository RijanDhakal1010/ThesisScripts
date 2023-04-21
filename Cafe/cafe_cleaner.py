import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Process orthofinder data for cafe.')

parser.add_argument('--min', type=int, default=2,
                    help='How many minimum non-zero values in a row. Default is 2.')
parser.add_argument('--tsv', type=str, required=True,
                    help='What is the name of the tsv file.')
parser.add_argument('--o', type=str, default='counts.tsv',
                    help='What is the name of the output file.')
parser.add_argument('--diff', type=int, default=68,
                    help='What difference between the minimum and the maximum value do you want to filter for? Default 68')

args = parser.parse_args()

df = pd.read_csv(args.tsv, sep='\t')

df = df.drop(columns=['Total'])

# In the dataframe, the first column is a non-integer value (names of families). Use `df.iloc[:, 1:]` to drop that.
# For each row count the number of non-zero values and drop if the number of non-zero values is too small 
# (the gene family is useless if it only has genes from two species in it in a group of 112 species).
df1 = df[df.iloc[:, 1:].apply(lambda row: (row != 0).sum(), axis=1) > args.min]

df2 = df1[df1.iloc[:, 1:].apply(lambda row: row.max() - row.min(), axis=1) < args.diff]

# Add a column named 'null' to the first column and set every value to '(null)'
df2.insert(0, 'Desc', '(null)')

print("The size of the dataframe this has created is", df2.shape)

df2.to_csv(args.o, sep='\t', index=False)


