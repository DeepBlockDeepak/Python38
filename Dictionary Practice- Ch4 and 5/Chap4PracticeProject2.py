#Character Picture Grid problem on pg 103
first= ["."]*6
second = [".","0", "0"]+["."]*3
third= ["0"]*4 + ["."]*2
fourth = ["0"]*5 + ["."]
fifth= ["."] + ["0"]*5
sixth = ["0"]*5 + ["."]
seventh = ["0"]*4 + ["."]*2
eighth = [".","0", "0"]+["."]*3
ninth= ["."]*6

grid = [
    first,
    second,
    third,
    fourth,
    fifth,
    sixth,
    seventh,
    eighth,
    ninth
    ]

for element in grid:
    print ("  ".join(element))
print ('\n')
print ("*"*10)
print ('\n')
    

def pic_grid(grid):
    for col in range(len(grid[0])):
        for i in range(len(grid)):
            print (grid[i][col], end = ' ')
        print()

pic_grid(grid)

print ('\n')
print ("--------------------------------")
print ('\n')

for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print()
        



