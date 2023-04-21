# the goal of this script is to take a list of nodes and produce a table that lists their siblings, parents and children.

from ete3 import Tree # handles the tree data
from ete3.parser import newick
# using argparse setup flags: newick tree file, name for output file
import argparse
import pandas as pd
import re
import os

parser = argparse.ArgumentParser(description="The goal of this script is to take a list of nodes and produce a table that lists their siblings, parents and children.")

input_group = parser.add_argument_group('Input file arguments')

input_group.add_argument('--list',nargs='?', const='bar',default='Default', help= "List of focal nodes, one per line in text format.")

input_group.add_argument('--tree',nargs='?', const='bar',default='Default', help= "The newick tree file.")

parser.add_argument('--output',nargs='?', const='bar',default='Default', help= "Name for the output file.")

args = parser.parse_args()

# make sure that the input files exist
for action in parser._action_groups:
    if action.title == 'Input file arguments':
        for arg in action._group_actions:
            arg_value = getattr(args,arg.dest)
            if os.path.exists(arg_value):
                continue
            else:
                print(f"Cannot open '{arg_value}', please make sure it exits or the path is supplied correctly.")
                exit()

# open list and read the contents into a list, remove the traling whitespaces
with open(args.list) as f:
    list_of_nodes = [f"<{line.rstrip()}>" for line in f]

# open the tree file and read the contents into a tree object. Catch error for the regular way of opening trees and switch to format 1 if the error is there
try:
    tree = Tree(args.tree)
except newick.NewickError:
    tree = Tree(args.tree, format=1)

all_nodes = []

for i in tree.traverse("postorder"):
    if not i.is_leaf():
        all_nodes.append(i.name)

matches = [s for s in all_nodes if any(sub in s for sub in list_of_nodes)]

# Create a df with the columns: node, parent, children, siblings
df = pd.DataFrame(columns=['node','parent','children','siblings'])

# iterate through the list of nodes and add them to the dataframe as items in the idex  column (noe).For every item in the list_of_nodes find parent, children, siblings and add them to the corresponding columns in the df. If multiple children, siblings add them to the same unit delimited by commas
for i,node in enumerate(matches):
    node = tree.search_nodes(name=node)[0]
    # the regex is in place to remove the extraneous characters
    node_name = re.search(r'.*?>', node.name)[0]
    parent = re.search(r'.*?>', node.up.name)[0]
    children = ",".join([re.search(r'.*?>', i.name)[0] for i in node.children])
    siblings = ",".join([re.search(r'.*?>', i.name)[0]  for i in node.up.children])
    df.loc[i] = [node_name,parent,children, siblings]

# save the df to a tsv file
df.to_csv(args.output,sep='\t', index=False)
