from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd

!which chromedriver

def init_browser():
    executable_path= {'executable_path': './chromedriver'}
    return browser = Browser('chrome', **executable_path)

mars_info={}

def scrape_mars_news():
    try:
        browser=init_browser()
        
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        news_title = soup.find('li',class_= 'slide')
        news_title2 = news_title.find('div', class_='content_title').text
        news_p = soup.find('div', class_='article_teaser_body').text
        
        mars_info['news_title2']= news_title2
        mars_info['news_p'] = news_p
        
        return mars_info
    
    finally:
        browser.quit()

def scrape_mars_image():
    try:
        browser=init_browser()
        
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        main_url = 'https://www.jpl.nasa.gov'
        featured_image_url = main_url + featured_image_url
        
        featured_image_url

        mars_info['featured_image_url'] = featured_image_url
        
        return mars_info
    
    finally:
        browser.quit()

 def scrape_mars_facts():
    mars_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(mars_url)
    
    mars_df = mars_facts[2]
    mars_df.columns = ['Description','Value']
    mars_df.set_index('Description', inplace=True)
    data = mars_df.to_html()
    
    mars_info['mars_facts'] = data
    
    return mars_info

def scrape_mars_hemispheres():
    try:
        browser=init_browser()
        hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemispheres_url)
        
        html = browser.html
        soup = bs(html, "html.parser")
        items = soup.find_all('div', class_='item')
        
        hemisphere_image_urls = []
        hemispheres_main_url = 'https://astrogeology.usgs.gov'
        
        for i in items:
            title = i.find('h3').text
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            browser.visit(hemispheres_main_url + partial_img_url) 
            partial_img_html = browser.html 
            soup = bs(partial_img_html, 'html.parser')
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
            
        mars_info['hemisphere_image_urls'] =  hemisphere_image_urls
        
        return mars_info
    
    finally:
        
        browser.quit()