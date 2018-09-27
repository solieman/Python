
# coding: utf-8

# Import the required libraries

# In[1]:


import requests
import nltk
from bs4 import BeautifulSoup


# Load the target web page

# In[2]:


page = requests.get("URL")


# In[3]:


page.status_code


# In[4]:


soup = BeautifulSoup(page.content, 'html.parser')


# In[5]:


# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out


# In[6]:


# get text
text = soup.get_text()


# In[7]:


# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())


# In[8]:


# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))


# In[9]:


# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)


# In[10]:


tokens = nltk.word_tokenize(text)


# In[11]:


import os.path
f_name = soup.title.text + '.tab'
f_path = os.path.join('/local/path/', f_name)
f = open(f_path, "w+")
f.write(text)


# In[12]:


word_features = ["Activity","Mindfulness","Nutrition","Sleep","Transformation"]


# In[13]:


def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


# In[14]:


print((find_features(tokens)))

