import shutil, re, os
#convert American date formats to European. Ex: March 5, 2009 == 03/05/2009; or 3/5/09 ---> 05/03/2009; 05/3/2009
#American: first slot ranges from 01-12 or 1,2,3-12. Second slot ranges from 01-31, or 1-31

#dateRegex function returns the Regex object for pattern matching the American date format
def dateRegex():

    dateRegex = re.compile(r"""
        (.*?)
        ([1-9]|0[1-9]|1[0-2])               #month - allows 03 or 3 for March format
        (-|\\|.)                            #separator1  - the character between day, month, and year
        ([1-9] |1[0-9]| 2[0-9]|3[0-1])      #day - allows any day of a month and nothing else
        (-|\\|.)                            # separator2                          
        (\d{1,4})                           #year - any number up to but not including 10^4 an be written
        (.*?)$


        """, re.VERBOSE)

    #returns Regex object for checking file names later on
    return dateRegex

def filename_checker():
    AmdateRegex = dateRegex()

    AmericanFilePath = str(input("Enter the filepath you would like to assess for textfile American Date -> European Date conversions: "))

    for filename in os.listdir(AmericanFilePath):
        mo = AmdateRegex.search(filename)

        if mo == None:
            continue
        
        first_name = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        last_name = mo.group(7)
        

        AmericanFile = os.path.abspath(filename)
        EuroFile = first_name + day + "-" + month + "-" + year + last_name

        print ("Renaming {} to \n{}\n".format(AmericanFile, EuroFile))


        shutil.move(
            os.path.join(AmericanFilePath, filename),
            os.path.join(AmericanFilePath, EuroFile)
            )

filename_checker()