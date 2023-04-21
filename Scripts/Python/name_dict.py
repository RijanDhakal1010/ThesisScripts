#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import pickle
import argparse


# In[ ]:


parser = argparse.ArgumentParser(description="This will need a pickled dict or a dict in one format or another. The dict's key-value pair should have the onekp alphabetical code as the keys and the respective names of the species as the value pairs.The script should be supplied with some params in the form of sysargv.")


# In[ ]:


parser.add_argument('--big_list', nargs='?', const="bar", default=False, help="This is the path to the file that holds the onekp database in excel format.")
parser.add_argument('--small_list', nargs='?', const="bar", default=False, help ="This is the list of species we are interested in.")
args = parser.parse_args()


# In[73]:


#open the onekp excel file with pandas
species_dataframe = pd.read_excel(args.big_list)


# In[74]:


location_of_list = args.small_list


# In[75]:


#df2 takes the only columns that we need
df2 = species_dataframe[['1KP Index ID','Species']]


# In[76]:


# this takes the path to the file that has the list and converts it into a list
species_list= open(location_of_list,'r').read().splitlines()


# In[77]:


#df3 only has the species we care about
df3 = df2[df2['Species'].isin(species_list)] 


# In[82]:


test_dict={}
for i in df3.itertuples():
    if test_dict.get(i[1]) == None:
        test_dict[i[1]] = i[2]
    else:
        test_dict[i[1]].append(i[2])


# In[ ]:


with open('codename_realname.pickle', 'wb') as handle:
    pickle.dump(test_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

