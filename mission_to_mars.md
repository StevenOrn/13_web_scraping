

```python
from splinter import Browser
from bs4 import BeautifulSoup
import re
import pandas as pd
```


```python
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
```


```python
url = 'https://mars.nasa.gov/news/'
```


```python
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
```

NASA Mars News


Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.


```python
news_title = soup.find('div', class_='content_title').find('a').text
news_p = soup.find('div', class_='article_teaser_body').text
```


```python
print(news_title,news_p)
```

    NASA Mars Mission Adds Southern California Dates Looking for summer fun? Southern California families have their choice of the beach, movies, museums -- and even NASA's next mission to Mars.


JPL Mars Space Images - Featured Image


Visit the url for JPL Featured Space Image here.
Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
Make sure to find the image url to the full size .jpg image.
Make sure to save a complete url string for this image.


```python
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
```


```python
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
```


```python
soup.find('article', class_='carousel_item')['style']
```




    "background-image: url('/spaceimages/images/wallpaper/PIA18897-1920x1200.jpg');"




```python
featured_image_url = "https://www.jpl.nasa.gov" + soup.find('article', class_='carousel_item')['style'].split("'")[1]
```


```python
featured_image_url
```




    'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA18897-1920x1200.jpg'



Mars Weather


Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.


```python
url = 'https://twitter.com/marswxreport?lang=en'
```


```python
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
```


```python
mars_weather = soup.find(text = re.compile("Sol"))
```


```python
mars_weather
```




    'Sol 2108 (2018-07-12), Sunny, high -24C/-11F, low -65C/-84F, pressure at 8.06 hPa, daylight 05:19-17:27'



Mars Facts


Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
Use Pandas to convert the data to a HTML table string.


```python
url = 'http://space-facts.com/mars/'
```


```python
tables = pd.read_html(url)
```


```python
tables[0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Equatorial Diameter:</td>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Polar Diameter:</td>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mass:</td>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Moons:</td>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Orbit Distance:</td>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Orbit Period:</td>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Surface Temperature:</td>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>7</th>
      <td>First Record:</td>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Recorded By:</td>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = tables[0]
df.columns = ['Fact','Measurements']
df.to_html(index=False)
```




    '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th>Fact</th>\n      <th>Measurements</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <td>Mass:</td>\n      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n    </tr>\n    <tr>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.52 AU)</td>\n    </tr>\n    <tr>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <td>Surface Temperature:</td>\n      <td>-153 to 20 °C</td>\n    </tr>\n    <tr>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'



Mars Hemispheres


Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


```python
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
```


```python
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
```


```python
urls = soup.findAll('div', class_ ='description')
```


```python
urls[1].a['href']
```




    '/search/map/Mars/Viking/schiaparelli_enhanced'




```python
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
```


```python
web_list = soup.findAll('li')
```


```python
web_list[-3]
```




    <li><a href="http://astrogeology.usgs.gov/tools/map-a-planet-2">Map a Planet 2</a></li>




```python
for obj in web_list:
    if (obj.a.text == 'Original'):
        print(obj.a['href'])
```


```python
soup.find('title').text.split('|')[0][:-1]
```




    'Astropedia Search Results'




```python
hemisphere_image_urls = []
for url in urls:
    next_page = 'https://astrogeology.usgs.gov'+ url.a['href']
    
    browser.visit(next_page)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    #looks for original picture
    web_list = soup.findAll('li')
    for obj in web_list:
        if ((obj.a.text) and obj.a.text == 'Original'):
            link = obj.a['href']
    
    title = soup.find('title').text.split('|')[0][:-1]
    
    hemisphere_image_urls.append( {'title':title,'img_url':link})
```


```python
hemisphere_image_urls
```




    [{'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif',
      'title': 'Cerberus Hemisphere Enhanced'},
     {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif',
      'title': 'Schiaparelli Hemisphere Enhanced'},
     {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif',
      'title': 'Syrtis Major Hemisphere Enhanced'},
     {'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif',
      'title': 'Valles Marineris Hemisphere Enhanced'}]




```python
browser.quit()
```
