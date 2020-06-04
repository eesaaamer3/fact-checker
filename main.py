import urllib 
import requests 
from bs4 import BeautifulSoup
import tkinter as tk

## CODE FOR BACKEND PYTHON SCRIPT

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


### CODE FOR FRONT END WINDOW

main_window = tk.Tk()

# Frames 
main_frame = tk.Frame()
title_frame = tk.Frame()

answer_frame = tk.Frame()
rewind_frame = tk.Frame()

def info_submission():
    info = input.get()
    input.delete(0, tk.END)
    main_frame.pack_forget()
    title_frame.pack_forget()
    initial_contact(info)

def rewind():
    answer_frame.pack_forget()
    rewind_frame.pack_forget()

    intro_window()

# Components for intro window
title = tk.Label(master = title_frame, text = "Fact Checker by Eesa Aamer", justify="center")
greeting = tk.Label(master = main_frame, text="Enter your fact: ", width = 12, height = 2, justify="left")
submission = tk.Button(master = main_frame, text="Submit", command = info_submission, width = 7)
input = tk.Entry(master = main_frame, width = 50)

# Components for answer window
rewind_time = tk.Button(
    master = rewind_frame, 
    text = "Click here to enter another fact!", 
    command = rewind,
    height = 3
    )

# Function that develops the answer window
def answer_window(x):
    print(x)
    # declares components
    answer = tk.Label(master=answer_frame, text=x, height=5)
    # develops the frames
    answer_frame.pack()
    rewind_frame.pack()
    # develops the components in the frame
    answer.grid(row=0, column=0)
    rewind_time.grid(row=1, column=0)


# Function that develops the intro window
def intro_window():
    # develops frames
    title_frame.pack()
    main_frame.pack()
    # creates components 
    title.grid(row=0, column=1)
    greeting.grid(row=1,column=1)
    input.grid(row=1,column=2)
    submission.grid(row=1, column=3)



intro_window()
# Main loop that keeps window open
main_window.mainloop()

