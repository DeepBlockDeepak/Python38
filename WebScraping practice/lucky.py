#! python3
# lucky.py - Opens several google search results

import requests, sys, webbrowser, bs4

print("Googling...")    #downloading the page, showing a waiting screen

#downloading the webpage of a google search result from the user's search items
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]))

#check validity of the webpage download
try:
    res.raise_for_status()

except Exception as exc:
    print("There was a problem: {}".format(exc))


soup = bs4.BeautifulSoup(res.text,"html.parser")#, features="html.parser"

#'.r a' is supposed to obtain the search links
linkElems = soup.select('.g a')

#only obtain at most 5 of the search links
numOpen = min(5, len(linkElems))


for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
    #print(linkElems[i].get('href').getText())

