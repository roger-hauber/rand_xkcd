'''Scrape a random xkcd cartoon from the web and save it
 into img folder'''

 #BeautifulSoup and requests are required
import requests
from bs4 import BeautifulSoup

## get html for a random comic
url = "https://c.xkcd.com/random/comic/"

rand_html = requests.get(url).content

 #pass rand_html to BeautifulSoup
rand_soup = BeautifulSoup(rand_html, "html.parser")

#first find the div id= "comic", then find the img
rand_div = rand_soup.find("div", id = "comic")

#get the img tag from the div
rand_img_tag = rand_div.find("img")["src"]

img_data = requests.get("https:" + rand_img_tag).content


#open file as write and binary and then write to the file
with open("img/random.png", "wb") as img:
    img.write(img_data)
