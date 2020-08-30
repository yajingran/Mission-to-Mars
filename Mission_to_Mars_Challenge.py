#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[28]:


# Mac Users
# Path to chromedriver
#!which chromedriver
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path, headless=False)


# In[29]:


# Windows users (initiate splinter)
executable_path = {'executable_path': 'chromedriver'} #(go back one directory where the chrome driver is located, in class folder)
browser = Browser('chrome', **executable_path, headless=False)


# In[30]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
# telling our browser to wait one second before searching for components
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[31]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[32]:


slide_elem.find("div", class_='content_title')


# In[33]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[34]:


# Use the parent element to find the paragraph text 
# the output is the summary of te first article since we used find.()
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[35]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[36]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[37]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[38]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[39]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[40]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# ### Mars Facts

# In[41]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[42]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[43]:


df.to_html()


# ### Mars Weather

# In[44]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[45]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[46]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[47]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[48]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links = browser.find_by_css('a.product-item h3')
for item in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css('a.product-item h3')[item].click()
    hemisphere['title'] = browser.find_by_css('h2.title').text
    sample_element = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_element['href']
    
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()


# In[49]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[50]:


# 5. Quit the browser
browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




