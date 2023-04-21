# the following libraries are need for this script to work
import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd

# The following three lines will make the code able to access the file on the internet. The following three lines currently work but I am not sure if the setup is sustainable. It is a patchwork of patchworks that may or may not keep working.

headers_1 = {'Accept-Encoding': 'identity', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'} # this is need to save us from being hit with captcha
connection_one = requests.get('http://www.onekp.com/public_data.html', headers = headers_1) # this is the website
soup_object = BeautifulSoup(connection_one.content,features="lxml") # this create a soup object that we will parse

table = soup_object.find('table') # The table that I am working with has only one so I am using find but you can use findAll to find tables.

rows = table.findAll(lambda tag: tag.name=='tr') # This converts each row in my table into a row that can be parsed. I understand 'tr' to mean table row in html but not sure. 

l =[] # this is the list that we will make a dataframe out of.

for tr in rows: # here we are going through the loopable 'rows' object that we made a second ago
    td = tr.find_all('td') # This goes through the individual rows in the tr objects and makes the members of the rows loopable.
    row = [] # this is to hold each new row items and emptied out each time for a new row to come in.
    for tr in td: # we made an object td that has all the items in each row, but those are html lines and not the information we need or at least it has more information than we really need.
        #ref= tr.find_all('a',href=True)
        try: # using the try method in python makes it much easier to handle error. Errors such as empty cells, which ironaically I have not handled here but plan to do in the future.
            ref = tr.find('a',href=True) # this takes the individual item in thw row and makes it possible to go through the elements of the item, parsing HTML is wild stuff!
            i = ref['href'] # href stand for the hyperlink refernce which is what I need. Otherwise you will only get the text with 'tr.text'. Some of my columns have hypterlinks, some of my columns have just text and I need to work around that. 
            row.append(i) # append it to the 'row' object that we made above
        except: # some of the rows are text only so the ones that are rejected are sent below to have their text extracted
            i = tr.text # extracts text
            row.append(i) # appends item
    l.append(row) # append the row
df = pd.DataFrame(l) # makes a dataframe

df.to_csv('Onekp_data.tsv',sep='\t', index=False) # this one makes a dataframe in the current directory.