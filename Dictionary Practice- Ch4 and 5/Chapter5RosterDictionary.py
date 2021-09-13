#adding names to a dictionary roster
from pprint import pprint
roster = {
    "Bob":"Dylan",
    "Carrie" : "Grant",
    "Smokey" : "Robinson"
    }


def roster_dictionary(roster):
    while True:
        
        name = str(input("What name are you looking for? (Blank to quit)"))

        if name == "":# USE  if roster.get(name)== None:
            pprint (roster)
            return roster
            
        elif name in roster:
            print ("{0}'s last name is {1}.".format(name, roster[name]))
            new_name = str(input("If you would like to change {0}'s last name, enter it. (Blank to quit)".format(name)))
            if new_name == "":
                pprint(roster)
                continue #possibly USE break here
            else:
                roster[name] = new_name
                continue

        else:            
            last_name = str(input("What is {0}'s last name?".format(name)))#experiment with not using break here
            
            roster[name]= last_name

            pprint(roster)
            continue
roster_dictionary(roster)

'''
f= open('checkthisout.txt', 'w')
f.write(repr(roster))
f.close()

'''
    

