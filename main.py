import urllib 
import requests 
import bs4 as BeautifulSoup

query = input("Enter in your fact: ")
query = query.replace(" ", "+")
URL = "https://google.com/search?q={}".format(query)

