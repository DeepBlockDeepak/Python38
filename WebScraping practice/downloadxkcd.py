#! python3
# downloadxkcd.py - Downloads every single xkcd comic

import requests, os, bs4

"""
Failed URLs Log:
    2197 - had a scroll bar and multiple images with one
    2067 - had a sophisticated zoom feature with hyperlinks
    1663 - had an interactable script in the image
    1608 - has an interactable arcade thingy
    1525 - interactable
    1416 - awesome infinite zoom interaction
    1350 - interactable
""" 
url = "http://xkcd.com/1349"

os.makedirs('xkcd_comics', exist_ok = True)

while not url.endswith("#"):

    print("Downloading the page {}...".format(url))

    res = requests.get(url)

    #check validity of the webpage download
    try:
        res.raise_for_status()

    except Exception as exc:
        print("There was a problem: {}".format(exc))


    soup = bs4.BeautifulSoup(res.text)


    #Find url of the comic image
    comicElem = soup.select('#comic img')

    
    if comicElem == []:
        print("Could not find comic image.")

    else:
        comicURL = 'http:' + comicElem[0].get('src')
        
        #Download the image.
        print("Downloading image {}...".format(comicURL))

        res = requests.get(comicURL)

        #check validity of the webpage download
        try:
            res.raise_for_status()

        except Exception as exc:
            print("There was a problem: {}".format(exc))
        
        #save the image to ./xkcd
        with open(os.path.join('xkcd_comics', os.path.basename(comicURL)), 'wb') as imageFile:

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)

        
    #move to the "Prev" button's URL
    prevLink = soup.select('a[rel="prev"]')[0]

    url = "http://xkcd.com" + prevLink.get('href')
    
    
print("Done")




