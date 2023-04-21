import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="This script is designed to take two files: 1. The original onekp file and 2. The list of species from onekp that one is interested in. This script will then produce the list of codes for the species of interest.")


parser.add_argument('--o',nargs='?',const='bar',help="The location to the onekp data file. It can handle both TSV or excel files.")

parser.add_argument('--l',nargs='?', const='bar', help="The location to the list of speices of interest. Text file with one species per line.")

args = parser.parse_args()

def main():

    if os.path.exists(args.o):
        pass
    else:
        print("Cannot open the onekp file. Please correct path.")

    if os.path.exists(args.l):
        pass
    else:
        print("Cannot open the list of species file. Please correct path.")

    with open(args.l, "r") as species_list_file:
        species_names = species_list_file.readlines()

    species_names = [item.rstrip() for item in species_names]

    if args.o.endswith(".xlsx"):
        df = pd.read_excel(args.o)
    elif args.o.endswith(".tsv"):
        df = pd.read_csv(args.o, sep = "\t")
    else:
        print("Please supply the original onekp file as either an excel(.xlsx) or tsv (.tsv) file.")
    # df2 makes data processing easier
    df2 = df[df['Species'].isin(species_names)]

    # df3 maeks processing the column of choice a little easier.
    df3 = df2.merge(df2.groupby('Species')["% BUSCOs (complete+fragmented)"].apply(lambda x: x[x==x.max()]).reset_index())

    with open('List_of_codes.txt', 'w') as f:
        for x in df3['1KP Index ID']:
            f.write("%s\n" % x)

    print("The code writes to the output file to get rid of older data.\n")
main()
