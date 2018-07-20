from splinter import Browser
from bs4 import BeautifulSoup
import re
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data={}

    ##NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    soup = soupify(browser,url)

    mars_data['news_title'] = soup.find('div', class_='content_title').find('a').text
    mars_data['news_p'] = soup.find('div', class_='article_teaser_body').text

    ##JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    soup = soupify(browser,url)

    mars_data['featured_image_url'] = "https://www.jpl.nasa.gov" + soup.find('article', class_='carousel_item')['style'].split("'")[1]

    ##Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    soup = soupify(browser,url)

    mars_data['mars_weather'] = soup.find(text = re.compile("Sol"))

    ##Mars Facts
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)

    df = tables[0]
    df.columns = ['Fact','Measurements']
    mars_data['df_table']=df.to_html(index=False)

    ##Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    soup = soupify(browser,url)

    urls = soup.findAll('div', class_ ='description')

    hemisphere_image_urls = []

    for url in urls:
        next_page = 'https://astrogeology.usgs.gov'+ url.a['href']
        
        soup = soupify(browser,next_page)
        
        #looks for original picture
        web_list = soup.findAll('li')
        #switched to full-size sample jpg instead of original since .tif files don't display 
        for obj in web_list:
            if ((obj.a.text) and obj.a.text == 'Sample'):  
                link = obj.a['href']
        
        title = soup.find('title').text.split('|')[0][:-1]
        
        hemisphere_image_urls.append( {'title':title,'img_url':link})

    mars_data['hemisphere'] = hemisphere_image_urls

    browser.quit()

    return mars_data



def soupify(browser,url):
    browser.visit(url)
    html = browser.html
    return BeautifulSoup(html, 'html.parser')