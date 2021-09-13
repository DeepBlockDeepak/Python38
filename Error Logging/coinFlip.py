import random


def monte_trials():
    trials = int(input("How many trials would you like to run?"))

    over_half_counter = 0
    for trial in range(trials):
        heads_count = coin_flipper()
        if heads_count > 500:
            over_half_counter += 1

    print("Heads(random.randint() value of 1)"
        " came up over half the time in {}% of trials".format((over_half_counter/trials)*100))

def coin_flipper():
    heads = 0
    for i in range(1000):
        if random.randint(0, 1) == 1:
            heads += 1
            
    return heads
monte_trials()

