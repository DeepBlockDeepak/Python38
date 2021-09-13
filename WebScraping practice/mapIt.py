import sys, pyperclip, webbrowser

if len(sys.argv) <= 1:
    address = pyperclip.paste()
    #address should be a string who's items are separated by spaces
    address = "+".join(address.split(" "))
    print(address)


else:

    address = "+".join(sys.argv[1:]) #for the Google Map URL


url = "www.google.com/maps/search/" + address
webbrowser.open(url)
