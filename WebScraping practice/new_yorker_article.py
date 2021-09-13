
import os, requests, bs4



url = "https://www.newyorker.com/magazine/2021/05/24/burnout-modern-affliction-or-human-condition"


#download the webpage
res = requests.get(url)

#check validity
res.raise_for_status()

#obtain the html of the page
soup = bs4.BeautifulSoup(res.text, features='html.parser')

article_text0 = soup.select(".has-dropcap")

article_text = soup.select(".paywall")

#need to .get the article_text('src') 
#then .get that url?

print(len(article_text0))

print(len(article_text))

with open('burnout.txt', 'w') as article_file:
    
    for item in article_text0:
        article_file.write(str(item))

    for item in article_text:
        article_file.write(str(item))

