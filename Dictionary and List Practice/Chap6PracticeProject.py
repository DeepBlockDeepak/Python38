#Table Printer
#get_col_width() will obtain a list where each element is equal to the length of the largest word in each tableData list element
# print_table() will then print the input list of lists, TableData, into a table structure, where each row is printed vertically,
#  left-justified according to the table obtained from get_col_width()


table_data = [['apples', 'oranges', 'cherries', 'banana'],
			['Vercingetorix','Bob','Carol', 'David'],
			['dogs', 'cats', 'moose', 'Epidexipteryx']]

def get_col_width(table):
	print ('\n')
	#widths_list will find the largest length of the items in the lists. 
	#this is necessary because the largest length will need to be used for right-justifying
	widths_list = []
	for row in table:
		max_length = 0
		for item in row:
			if len(item) > max_length:
				max_length = len(item)
		widths_list.append(max_length)
	return (widths_list)
		

def print_table(table):
	widths_list = get_col_width(table)
	#s stands for "Second", as in the Second index needed to select the particular elements in the inner-most lists of table
	for s in range(len(table[0])): 
		for f in range(len(table)):#f stands for "First", because it's the first index of access. We hold [s] constant, in the outer loop, for each cycle of the rows accessed by index [f].
			print (table[f][s].ljust(widths_list[f]), end = ' '*3)
		print ()

print_table(table_data)
