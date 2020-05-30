#!/usr/bin/env python
# coding: utf-8

# ### Required Imports for Web Scraping And Converting To DataFrame

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bs4
from bs4 import BeautifulSoup
import requests


# ### Load the content using reuqests module convert it to html readable

# In[2]:


page = requests.get("https://www.imdb.com/search/title/?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012")
contents = page.content


# ### Create a Static Html file of the same to use later and store it

# In[3]:


print(type(contents))
with open('IMDB_Movies_HTML_Page.html','ab') as fb:
    fb.write(contents)


# ### Parse content using BeautifulSoup4's html.parse

# In[4]:


soup = BeautifulSoup(contents,"html.parser")


# ### Clean the data by removing unneccessary html tags and create dictionary to store data

# In[ ]:


### Data_Clean_Soup=soup.find_all("div","lister-item mode-advanced")
Dict_Of_IMDB_Data = { 'Movie_Name' : [0,],'Duration_Minute':[0,],'Genre':[0,],'Rating':[0,],"Text":[0,],'Directores':[0,],'Stars_Heroes':[0,],'User_Votes':[0,],'Gross_In_Million':[0,]}
Dict_Of_IMDB_Data


# ### Use find_all or find to get required data from the parser

# In[6]:


#Data_Clean_Soup[0].find_all('a')[1].string                                  Movie Name
#Data_Clean_Soup[0].find_all('a')[13].string                                 Director
#Data_Clean_Soup[0].find_all('a')[14:]                                       all the heroes who worked in movie
#Data_Clean_Soup[0].find("span","runtime").string[:-4]                       duration
#Data_Clean_Soup[0].find("span","genre").string.strip('\n ')                 genre
#Data_Clean_Soup[0].find("span","value").string                              Rating
#Data_Clean_Soup[0].find_all('p')[1].string.strip('\n ')                     Text
#Data_Clean_Soup[0].find_all('span')[-4].string                              Vote
#Data_Clean_Soup[0].find_all('span')[-1].string[:-1]                         gross
#{ 'Movie_Name' : [],'Duration_Minute':[],'genre':[],'rating':[],"Text":[],'Directores':[],'Stars_Heroes':[],'User_Votes':[],'Gross_In_Million':[]}


# ### Convert Data to the List to Save in Dictionary

# In[7]:


Movie=[]
Genre=[]
Rating=[]
Text=[]
Directores=[]
User_Vote=[]
Gross=[]
Duration=[]
Stars=[]
get=[]
try:
    for i in range(len(Data_Clean_Soup)):
        get=i
        Movie.append(Data_Clean_Soup[i].find_all('a')[1].string)
        Genre.append(Data_Clean_Soup[i].find("span","genre").string.strip())
        Duration.append(Data_Clean_Soup[i].find("span","runtime").string[:-4])
        Rating.append(Data_Clean_Soup[i].find("span","value").string)
        Text.append(Data_Clean_Soup[i].find_all('p')[1].find(text=True).strip())
        Directores.append(Data_Clean_Soup[i].find_all('a')[13].string)
        User_Vote.append(Data_Clean_Soup[i].find_all('span')[-4].string)
        Gross.append(Data_Clean_Soup[i].find_all('span')[-1].string[:-1])
        list_actor =[]
        total_list = Data_Clean_Soup[i].find_all('a')[14:]
        for i in total_list:
            list_actor.append(i.string)
        Stars.append(','.join(list_actor))
except:
    print("Get Error on Line with Data index : ",get)
        


# ### Add data to the Dictionary

# In[8]:


Dict_Of_IMDB_Data['Movie_Name']=Movie
Dict_Of_IMDB_Data['Genre'] = Genre
Dict_Of_IMDB_Data['Duration_Minute'] =Duration
Dict_Of_IMDB_Data['Rating'] = Rating
Dict_Of_IMDB_Data['Text'] = Text
Dict_Of_IMDB_Data['Directores'] = Directores
Dict_Of_IMDB_Data['User_Votes'] = User_Vote
Dict_Of_IMDB_Data['Gross_In_Million'] = Gross
Dict_Of_IMDB_Data['Stars_Heroes']= Stars


# ### Create DataFrame Using Pandas 

# In[9]:


IMDB_Movie_Data = pd.DataFrame(Dict_Of_IMDB_Data)
IMDB_Movie_Data


# ### Now Save the DataFrame as a CSV file to use it later on Data Visualization
# #### we have out csv file to perform the analysis. so, we can able to use it visualize and understand the data and their relations
# ##### Now we can able to use this data to create NLP Model or Machine learning for predictions

# In[12]:


IMDB_Movie_Data.to_csv("IMDB_MOVIES.csv")

