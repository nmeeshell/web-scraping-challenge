{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'splinter'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-f93e1212c03a>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Declare Dependencies\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mbs4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBeautifulSoup\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0msplinter\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mBrowser\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrequests\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'splinter'"
     ]
    }
   ],
   "source": [
    "# Declare Dependencies \n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path':'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit Nasa news url through splinter module\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object\n",
    "html = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "\n",
    "# Retrieve the latest element that contains news title and news_paragraph\n",
    "news_title = soup.find('div', class_='content_title').find('a').text\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "# Display scrapped data \n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit Mars Space Images through splinter module\n",
    "image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(image_url_featured)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object \n",
    "html_image = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html_image, 'html.parser')\n",
    "\n",
    "# Retrieve background-image url from style tag \n",
    "featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]\n",
    "\n",
    "# Website Url \n",
    "main_url = 'https://www.jpl.nasa.gov'\n",
    "\n",
    "# Concatenate website url with scrapped route\n",
    "featured_image_url = main_url + featured_image_url\n",
    "\n",
    "# Display full link to featured image\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit Mars Weather Twitter through splinter module\n",
    "weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(weather_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object \n",
    "html_weather = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html_weather, 'html.parser')\n",
    "\n",
    "# Find all elements that contain tweets\n",
    "latest_tweets = soup.find_all('div', class_='js-tweet-text-container')\n",
    "\n",
    "# Retrieve all elements that contain news title in the specified range\n",
    "# Look for entries that display weather related words to exclude non weather related tweets \n",
    "for tweet in latest_tweets: \n",
    "    weather_tweet = tweet.find('p').text\n",
    "    if 'Sol' and 'pressure' in weather_tweet:\n",
    "        print(weather_tweet)\n",
    "        break\n",
    "    else: \n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit Mars facts url \n",
    "facts_url = 'http://space-facts.com/mars/'\n",
    "\n",
    "# Use Panda's `read_html` to parse the url\n",
    "mars_facts = pd.read_html(facts_url)\n",
    "\n",
    "# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`\n",
    "mars_df = mars_facts[0]\n",
    "\n",
    "# Assign the columns `['Description', 'Value']`\n",
    "mars_df.columns = ['Description','Value']\n",
    "\n",
    "# Set the index to the `Description` column without row indexing\n",
    "mars_df.set_index('Description', inplace=True)\n",
    "\n",
    "# Save html code to folder Assets\n",
    "mars_df.to_html()\n",
    "\n",
    "data = mars_df.to_dict(orient='records')  # Here's our added param..\n",
    "\n",
    "# Display mars_df\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit hemispheres website through splinter module \n",
    "hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(hemispheres_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object\n",
    "html_hemispheres = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html_hemispheres, 'html.parser')\n",
    "\n",
    "# Retreive all items that contain mars hemispheres information\n",
    "items = soup.find_all('div', class_='item')\n",
    "\n",
    "# Create empty list for hemisphere urls \n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# Store the main_ul \n",
    "hemispheres_main_url = 'https://astrogeology.usgs.gov'\n",
    "\n",
    "# Loop through the items previously stored\n",
    "for i in items: \n",
    "    # Store title\n",
    "    title = i.find('h3').text\n",
    "    \n",
    "    # Store link that leads to full image website\n",
    "    partial_img_url = i.find('a', class_='itemLink product-item')['href']\n",
    "    \n",
    "    # Visit the link that contains the full image website \n",
    "    browser.visit(hemispheres_main_url + partial_img_url)\n",
    "    \n",
    "    # HTML Object of individual hemisphere information website \n",
    "    partial_img_html = browser.html\n",
    "    \n",
    "    # Parse HTML with Beautiful Soup for every individual hemisphere information website \n",
    "    soup = BeautifulSoup( partial_img_html, 'html.parser')\n",
    "    \n",
    "    # Retrieve full image source \n",
    "    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']\n",
    "    \n",
    "    # Append the retreived information into a list of dictionaries \n",
    "    hemisphere_image_urls.append({\"title\" : title, \"img_url\" : img_url})\n",
    "    \n",
    "\n",
    "# Display hemisphere_image_urls\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
