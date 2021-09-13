#total_bought.py is practice for looping through dictionaries with the .get() method
#It will attempt to print each Guest's name, followed by the same kind of picnic item
#Also attempts to print each person followed by every item

all_guests = {
    'Alice': {'apples':5,'pretzels': 12,
    },
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups':3, 'apple pies': 1}

}

def picnic(guest_list):
    for name, value in guest_list.items(): #each 'key' is the name, and each 'value' is the dictionary associated
        for k, v in value.items():#the first loop is holding 'Alice' and her item dict constant. Now this loop will cycle through her items and their values
            print (name + " : " + k + " " + str(value.get(k,0)))
picnic(all_guests)
