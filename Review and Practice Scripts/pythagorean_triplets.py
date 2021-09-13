#!python3
import timeit

def version3(limit):
    for x in range(1,limit):
        for y in range(x+1, limit):
            z = y + 1

            while z**2 < x**2 + y**2:
                z +=1
            
            if z**2 == x**2 + y**2 and z<= limit:
                pass
                #print("{} = {}^2 + {}^2".format(z,x,y))
                #print("-"*50)

            


def version4(limit):
    for x in range(1, limit):
        y = x + 1
        z = y + 1

        while z <= limit:

            while z**2 < x**2 + y **2:
                z += 1
            
            if z**2 == x**2 + y**2 and z <= limit:
                pass
                #print("{} = {}^2 + {}^2".format(z,x,y))
                #print("-"*50)
            y = y + 1

def timer_3(num_of_trials):
    total_time = 0
    #total_number_of_trials = num_of_trials

    for i in range(num_of_trials):
        start = timeit.default_timer()
        version3(limit)
        stop = timeit.default_timer()

        total_time += (stop - start)

        #num_of_trials -= 1


    average_time = total_time / num_of_trials
    return average_time
    #print("\n***The version_3 run was {}***\n".format(stop - start))

def timer_4(num_of_trials):
    total_time = 0

    for i in range(num_of_trials):
        start = timeit.default_timer()
        version4(limit)
        stop = timeit.default_timer()
        total_time += (stop - start)
        
    
    average_time = total_time / num_of_trials
    return average_time

    #print("\n***The Version_4 run was {}***\n".format(stop - start))

limit = 2000
num_of_trials = 20
start = timeit.default_timer()

version4(limit)

stop = timeit.default_timer()

print("Time = " + str(stop - start))

"""print(
    "Version 4 is {} times faster than Version 3".format(
        round(timer_3(num_of_trials)/timer_4(num_of_trials), 2)
    )
)
"""