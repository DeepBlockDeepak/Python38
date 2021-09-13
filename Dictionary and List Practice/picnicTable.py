#printPicnic takes in a dictionary of items and centers a title over two columns
#the left column, the items, will be left justified, followed by asterisks
#the right column will be right-justified, preceded be emtpy spaces



def printPicnic(itemsDict,leftWidth,rightWidth):
    print ("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))

    for k, v in itemsDict.items():
		print (k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, ' '))


itemsDict = {
	"keys": 1,
	"oranges": 2,
	"pens": 55554
}
    
printPicnic(itemsDict, 10, 6)
