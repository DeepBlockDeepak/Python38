# function will take user input in the form of time of day , HH:MM:SS, and return the angle between
#the minute and hour hand on the corresponding analog clock

import re #import regEx module for handling acceptable user inputs

def clock_hands():

    while True:#while loop allows an incorrect input to trigger a do-over. Correct inputs will be stored and break out of the While Loop
        try:
            userTime = input("Insert a time in the HH:MM:SS format to compute angle between minute and hour hands (Blank to exit): ")#userTime will pass into the search() method
            userTimeRegex= re.compile(r'\d\d:\d\d:\d\d') #we pass the desired pattern HH:MM:SS (digits with : delimiters), and store the resulting Regular Expression object to userTimeRegex
            mo= userTimeRegex.search(userTime) #here we call search() on userTimeRegex and pass search() the string we want to search for a match. The result gets stored in 'mo', the Match Object
            userTime = (mo.group())
            #userTime has been reassigned the str Object that matches the HH:MM:SS user input. This will be used for the second part of clock_hands(), which will calculate the angle
            
        except AttributeError:#Attribute Error is raised because the Regex methods are applied to incorrect inputs, rather than ValueErrors
            
            if not userTime:#blank inputs to userTime will break process and end function
                break
            print ("Incorrect format. Try again.")
            continue #typos allow a do over to process
    
        hours = float(userTime[:2])#list slice the userTime input and make into floating point integer
        minutes = float(userTime[3:5])
        seconds = float(userTime[6:])#assigned variables for each digit value. No condition testing needed due to use of Regular Expression pattern matching

        seconds_to_min = 360/60 * (seconds) #converts seconds degree value
        minutes_angle = seconds_to_min/60 + 360/60*minutes #converts the 'seconds_to_min' to a fractional minute value, and adds the (6 deg/min * 'minutes') value contributed from the minutes value
        hours_angle= minutes_angle/360*30 + 360/12*hours# converts the minute angle to a fractional hour value, then multiples by 30 deg/hour value. 360/12=30 deg per hour, which is multiplied by the hour value. Added together, the total angle of the hour hand is computed.

        angle = abs(hours_angle - minutes_angle) #hours_angle - minutes_angle can be negative, and the acute angle between hands is needed.
                                                    #

        if angle > 180: #this condition is for the obtuse angle, not the acute angle we're looking for
            print ('{:.2f}'.format(360 - angle))#using 360 finds the complimentary angle to the obtuse angle we found. Will by definition be less than 180 degrees
        else:
            print ('{:.2f}'.format(angle))#formatting the floating point integer to two decimal places

clock_hands()
