
"""
https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv
"""

import requests, time, pyperclip


def grab_met():

    #os.chdir(r'C:\Python38\Scripts\python38_practice\Chapter11\')
    user_url = pyperclip.paste()

    start = time.perf_counter()

    res = requests.get(user_url)

    try:
        res.raise_for_status()
    except Exception as exc:
        print("There was a problem: %s" % exc)
    
    
    with open("met_content.txt", 'wb') as metFile:
        for chunk in res.iter_content(100000):
            metFile.write(chunk)

    end = time.perf_counter()

    print("Total time to run script = {}".format(end - start))

grab_met()

