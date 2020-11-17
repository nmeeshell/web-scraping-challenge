{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "!which chromedriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    executable_path= {'executable_path': './chromedriver'}\n",
    "    return browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_info={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_news():\n",
    "    try:\n",
    "        browser=init_browser()\n",
    "        \n",
    "        url = \"https://mars.nasa.gov/news/\"\n",
    "        browser.visit(url)\n",
    "        \n",
    "        html = browser.html\n",
    "        soup = bs(html, \"html.parser\")\n",
    "        \n",
    "        news_title = soup.find('li',class_= 'slide')\n",
    "        news_title2 = news_title.find('div', class_='content_title').text\n",
    "        news_p = news_title.find('div', class_='article_teaser_body').text\n",
    "        \n",
    "        mars_info['news_title2']= news_title2\n",
    "        mars_info['news_p'] = news_p\n",
    "        \n",
    "        return mars_info\n",
    "    \n",
    "    finally:\n",
    "        browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_image():\n",
    "    try:\n",
    "        browser=init_browser()\n",
    "        \n",
    "        url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "        browser.visit(url)\n",
    "        \n",
    "        html = browser.html\n",
    "        soup = bs(html, \"html.parser\")\n",
    "        \n",
    "        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]\n",
    "        main_url = 'https://www.jpl.nasa.gov'\n",
    "        featured_image_url = main_url + featured_image_url\n",
    "        \n",
    "        mars_info['featured_image_url'] = featured_image_url\n",
    "        \n",
    "        return mars_info\n",
    "    \n",
    "    finally:\n",
    "        browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_facts():\n",
    "    mars_url = \"https://space-facts.com/mars/\"\n",
    "    mars_facts = pd.read_html(mars_url)\n",
    "    \n",
    "    mars_df = mars_facts[2]\n",
    "    mars_df.columns = ['Description','Value']\n",
    "    mars_df.set_index('Description', inplace=True)\n",
    "    data = mars_df.to_html()\n",
    "    \n",
    "    mars_info['mars_facts'] = data\n",
    "    \n",
    "    return mars_info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape_mars_hemispheres():\n",
    "    try:\n",
    "        browser=init_browser()\n",
    "        hemispheres_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "        browser.visit(hemispheres_url)\n",
    "        \n",
    "        html = browser.html\n",
    "        soup = bs(html, \"html.parser\")\n",
    "        items = soup.find_all('div', class_='item')\n",
    "        \n",
    "        hemisphere_image_urls = []\n",
    "        hemispheres_main_url = 'https://astrogeology.usgs.gov'\n",
    "        \n",
    "        for i in items:\n",
    "            title = i.find('h3').text\n",
    "            partial_img_url = i.find('a', class_='itemLink product-item')['href']\n",
    "            browser.visit(hemispheres_main_url + partial_img_url) \n",
    "            partial_img_html = browser.html \n",
    "            soup = bs(partial_img_html, \"html.parser\")\n",
    "            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']\n",
    "            hemisphere_image_urls.append({\"title\" : title, \"img_url\" : img_url})\n",
    "            \n",
    "        mars_info['hemisphere_image_urls'] =  hemisphere_image_urls\n",
    "        \n",
    "        return mars_info\n",
    "    \n",
    "    finally:\n",
    "        \n",
    "        browser.quit()"
   ]
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
