#Chap6PracticeProjectInverse.py performs same idea as chap5practiceproject...
#BUT it prints stacks according to the same index of each internal list

table_data = [['apples', 'oranges', 'cherries', 'banana'],
			['Vercingetorix','Bob','Carol', 'David'],
			['dogs', 'cats', 'moose', 'Epidexipteryx']
]

def get_col_widths(table):#first, obtain values of largest lengths in columns
	print ('\n')
	col_widths= []#col_widths contains elements equal to the longest length word in each column of table_data 
	

	for s in range(len(table[0])): #assess table_data according to the items of the inner lists([apples,...,banana] --> [0,...,3])
		max_length = 0 #placeholder; max_length will be 4 elements in length
		
		for f in range(len(table)): #[f] is the index for the outer lists
			if len(table[f][s]) > max_length:
				max_length = len(table[f][s]) #updates max_length to largest length within the first column
		col_widths.append(max_length) #col_widths now is updated. This will occur a total of 4 times because there are 4 "columns" in table_data
	return col_widths

def print_table(table):
	col_widths = get_col_widths(table)#import the previously obtained col_widths, used for left/right-justifying 

	for f in range(len(table)) : #looping through each [f] index first so that inner loop can access each item within each table[f]
		for s in range(len(table[0])):#[s] is the second index used to access the inner list's elements
			print (table[f][s].ljust(col_widths[s]), end = ' '*3) #ljust() organizes each column based on the max widths found in col_widths 
		print ()
print_table(table_data)
