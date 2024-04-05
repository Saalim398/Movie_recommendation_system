#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# In[6]:


os.chdir('E:\\users\\downloads')
movies_data = pd.read_csv('movies.csv')
movies_data.head()


# In[7]:


display (movies_data.shape)


# In[9]:


selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)


# In[10]:


display (movies_data.info())


# In[11]:


display (movies_data.isna().sum())


# In[12]:


display (movies_data[selected_features].head())


# In[13]:


display (movies_data[selected_features].isna().sum())


# In[14]:


for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
display (movies_data.head())


# In[15]:


combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
display (combined_features)


# In[16]:


vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
display (feature_vectors.shape)
print (feature_vectors)


# In[17]:


similarity = cosine_similarity(feature_vectors)
print  (similarity )


# In[18]:


display(similarity.shape)


# In[19]:


movie_name = input(' Enter your favourite movie name : ')


# In[20]:


list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)


# In[21]:


len(list_of_all_titles)


# In[22]:



find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)


# In[23]:


close_match = find_close_match[0]
print(close_match)


# In[24]:


index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)


# In[25]:


similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)


# In[26]:


len(similarity_score)


# In[27]:


sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 
print(sorted_similar_movies)


# In[28]:


print('Movies suggested for you : \n')
i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1


# In[29]:


movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True) 

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1


# In[ ]:




