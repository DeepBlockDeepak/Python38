#build_bst takes a list as argument, and makes a BST with nodes designated by median indeces of the argument lists.
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  middle_idx = len(my_list)//2
  middle_value = my_list[middle_idx]
  '''
  print ("Middle index: {0}".format(str(middle_idx)),("Middle value: {0}".format(middle_value)))
  '''

  tree_node = {'data': middle_value}  
 
  tree_node['left_child']= build_bst(my_list[:middle_idx])
  tree_node['right_child'] = build_bst(my_list[middle_idx + 1:])
  
  
  return tree_node
# For testing
sorted_list = [0,99,1,2,3,4]
binary_search_tree = build_bst(sorted_list)
print (binary_search_tree)
print (len(binary_search_tree))



"""
def parse(response):
  filename = "my_tree.txt" 
  with open(filename, 'w') as f:
    f.write(str(response))
parse(binary_search_tree)
"""


