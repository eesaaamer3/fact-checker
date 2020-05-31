import urllib 
import requests 
import bs4 as BeautifulSoup

# desktop user-agent so urllib returns results from desktop version 
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

query = input("Enter in your fact: ")
query = query.replace(" ", "+")
url = "https://google.com/search?q={}".format(query)

headers = {"user-agent" : USER_AGENT}
resp = requests.get(url, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
else:
    print("ERROR: There was an issue while searching. Please try again")

