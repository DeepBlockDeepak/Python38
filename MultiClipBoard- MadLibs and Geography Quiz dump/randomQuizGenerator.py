#!Python3
#creates 35 unique quizzes each of which has 50 multiple-choice questions in random order
#writes the quizzes to 35 text files and creates 35 answer keys which are writtent 35 text files


#import os for os.path type methods; import random for the random.shuffle() method
import os
import random

#######################TODO: finish the fucking comments you asshole ######################
capitals= {'Alabama': 'Montgomery',
 'Alaska': 'Juneau',
 'Arizona': 'Phoenix',
 'Arkansas': 'Little Rock',
 'California': 'Sacramento',
 'Colorado': 'Denver',
 'Connecticut': 'Hartford',
 'Delaware': 'Dover',
 'Florida': 'Tallahassee',
 'Georgia': 'Atlanta',
 'Hawaii': 'Honolulu',
 'Idaho': 'Boise',
 'Illinois': 'Springfield',
 'Indiana': 'Indianapolis',
 'Iowa': 'Des Moines',
 'Kansas': 'Topeka',
 'Kentucky': 'Frankfort',
 'Louisiana': 'Baton Rouge',
 'Maine': 'Augusta',
 'Maryland': 'Annapolis',
 'Massachusetts': 'Boston',
 'Michigan': 'Lansing',
 'Minnesota': 'Saint Paul',
 'Mississippi': 'Jackson',
 'Missouri': 'Jefferson City',
 'Montana': 'Helena',
 'Nebraska': 'Lincoln',
 'Nevada': 'Carson City',
 'New Hampshire': 'Concord',
 'New Jersey': 'Trenton',
 'New Mexico': 'Santa Fe',
 'New York': 'Albany',
 'North Carolina': 'Raleigh',
 'North Dakota': 'Bismarck',
 'Ohio': 'Columbus',
 'Oklahoma': 'Oklahoma City',
 'Oregon': 'Salem',
 'Pennsylvania': 'Harrisburg',
 'Rhode Island': 'Providence',
 'South Carolina': 'Columbia',
 'South Dakota': 'Pierre',
 'Tennessee': 'Nashville',
 'Texas': 'Austin',
 'Utah': 'Salt Lake City',
 'Vermont': 'Montpelier',
 'Virginia': 'Richmond',
 'Washington': 'Olympia',
 'West Virginia': 'Charleston',
 'Wisconsin': 'Madison',
 'Wyoming': 'Cheyenne'}
#dirname is the directory where the files will be located.
dirname= "C:\\Python38\\Scripts\\python38_practice\\ChapterProjects\\chapter8_madlibs"

#loop 35 times for each student, creating a new quiz and answer key each time
for quizNum in range(35):
    #File object 'qn' is created
    qn = open(os.path.join(dirname, "capitalsquiz{0}.txt".format(str(quizNum + 1))), 'w')#open a quiz with appropriate name, for each student
    qn.write("Name:\n\nDate:\n\nPeriod:\n\n")

    qn.write((" "*20)+ "State Capitals Quiz (Form {0})".format(quizNum +1))
    qn.write('\n'*2)

    answerKeyFile = open(os.path.join(dirname, "capitalsquiz_answers{0}.txt".format(str(quizNum +1))),'w')#open an answer key, with same name index as its associated quiz

    # a list 'states' is created and shuffled. This will be cycled over in the quiz creator
    states = list(capitals.keys())
    random.shuffle(states)

    #now do a loop of size 50, once for each state/capital pair in the capitals dictionary
    for questionNum in range(50):
        #in each loop, a new capital city is chosen. That capital city is then removed_
        #from a list of all the capital cities.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers= list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)] #correctAnswer is deleted so that only incorrect values are leftover
        wrongAnswers = random.sample(wrongAnswers, 3)#sample 3 random wrongAnswers from the list of wrongAnswers
        
        answerOptions = wrongAnswers + ([correctAnswer]) #correct answer must be in a list, due adding iterable string to a list
        
        random.shuffle(answerOptions)#answerOptions must be shuffled so that the correctAnswer isn't always the last option listed

        qn.write("\n{0}What is the capital of {1}?".format(str(questionNum +1) + ".)  " ,states[questionNum]))

        for letter, answer in zip('abcd'.upper(), answerOptions):
            qn.write("\n" + letter + ".  " + answer)
        qn.write("\n")

        #answerKeyFile.write("\nQuestion {} : {} \n".format(str(questionNum +1),correctAnswer ))
        answerKeyFile.write("\nQuestion {} : {}). {} \n".format(str(questionNum +1), 'ABCD'[answerOptions.index(correctAnswer)], correctAnswer))
qn.close()
answerKeyFile.close()

