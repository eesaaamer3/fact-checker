import urllib 
import requests 
from bs4 import BeautifulSoup

# desktop user-agent so urllib returns results from desktop version 
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}

def initial_contact(query):
    #query = input("Enter in your fact: ")
    query = query.replace(" ", "+")
    url = 'https://google.com/search?q="{}"'.format(query)
    html_retrivel(url)

def html_retrivel(u):
    resp = requests.get(u, headers=headers)

    if resp.status_code == 200:
        html_parser(BeautifulSoup(resp.content, "html.parser"))
    else:
        print("ERROR: There was an issue while searching. Please try again")

def html_parser(soup): 
    results = []
    for elements in soup.find_all('div', class_='r'):
        links = elements.find_all('a')
        if links:
            link = links[0]['href']
            title = elements.find('h3').text
            item = {
                "title": title,
            }
            results.append(item)
    fact_check(len(results))


def fact_check(r):
    if r <= 5:
        answer_window("Fact is very likely to be FALSE. Do not trust.")
    elif r > 5 and r < 10:
        answer_window("Fact may contain FALSE information. Please conduct further research.")
    elif r >= 10:
        answer_window("Fact is TRUE.")
