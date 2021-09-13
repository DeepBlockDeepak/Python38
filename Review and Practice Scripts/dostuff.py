import pprint
names, grades, notes = [],[],[]
print(names,grades,notes)


for i in (range(10)):
    names.append("name" + str(i + 1))
    grades.append("grade" + str(i+1))
    notes.append("stuff" + str(i+1))

empty = {}

for na,gr, no in zip(names,grades,notes):
    empty[na]= {"Grade": gr, "Notes": no}

empty["Gerald"]= {}


empty["Gerald"]["Grade"]= 60006
empty["Gerald"]["Notes"]= "he was a good lad today that Lad Gerlad"


pprint.pprint(empty)

print (empty["Gerald"])