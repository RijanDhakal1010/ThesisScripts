import pandas as pd # we will need pandas to make a dataframe
import csv # we might need this to work with the csv files 
import sqlite3 # this we will need to make a dataframe
#import sys # might need this in the future to make the script interactive

def main():

	df = pd.read_csv('Base_change.tab', header =0)

	if len(df.columns) == 1:
		print('Using comma-based separation gave only one column. This is probably not a csv file, so we will use a tab based separation instead.')
		df = pd.read_csv('Base_change.tab',sep ='\t', header =0)

	list_of_columns = df.columns.values.tolist()

	literal_names = str()

	for i in list_of_columns:
		literal_names += f'{str(i)}{","}'
	
	literal_names = literal_names[:-1] # hacky fix for the lingering comma

	literal_command = f'{"CREATE TABLE IF NOT EXISTS orthos ("}{literal_names}{")"}'

	conn = sqlite3.connect('test_database')
	c = conn.cursor()
	
	c.execute(literal_command)
	conn.commit()

	df.to_sql('orthos', conn, if_exists='replace', index = False)

main()