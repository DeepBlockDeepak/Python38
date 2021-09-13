#! python3

class Student():
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade) 
	
  def get_average(self):
    print(sum(self.grades)/ (float(len(self.grades))))
      
      
class Grade(): 
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
    
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)
pieter_grade = Grade(100)
pieter_grade2 = Grade(70)
pieter.add_grade(pieter_grade.score)
print (type(pieter_grade.score))
pieter.add_grade(pieter_grade2.score)
print (pieter.grades)


#WHY DOESN'T THIS WORK???
    