#Fantasy Game inventory Practice Project, pg 119
import pprint
stuff ={
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12
    }
inv = {
    "gold coin": 42,
    "rope": 1
    }

dragonLoot= [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby',
    'torch',
    'arrow'
    ]
shitty_balls= [
    'nutsack',
    'ball breath',
    'fire hydrant',
    'pork chop',
    'pork chop',
    'gold coin'
    ]


"**************************************************"
#code styled more directly on book material. It performs the first Project function on pg 119

def displayInventory(inventory):#function takes the parameter inventory, which is a dictionary
    print ("Inventory".center(20, "-"))
    pprint.pprint (inventory, width = 10)
    total = 0
    for key, value in inventory.items():
        print ("{0} {1}".format(value, key))
        total += inventory.get(key)#get() used instead of value. both work
    print ("Total number of items: {0}".format(total))
    
#displayInventory(inv)
#Code performs the second project on pg 120. uses the displayInventory function in the function call below

def addToInventory( inventory, addedItems):#parameters are the dicitonary 'inventory', and the list 'addedItems'k
    for item in addedItems:        
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory

displayInventory(addToInventory(stuff, dragonLoot))

"************************************************************"

#displayInventory combines the above functions into one function call. addedItems and their amount are sent to inventory, and then the inventory is printed
def displayInventory(inventory, addedItems):
    print ("Inventory: \n")

    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    for key, value in inventory.items():
        print ("{0} {1}".format(value, key))
    print ("Total number of items: {0}".format(sum(inventory.values())))

#displayInventory(stuff, dragonLoot)