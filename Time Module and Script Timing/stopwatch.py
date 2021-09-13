#!python3

# stopwatch.py - A simple stopwatch program
import time

print(
    "Press ENTER to being. Afterwards, press ENTER to 'click' the stopwatch. "
    "Press CTRL-C to quit."
    )

input()

print("Started.")

startTime = time.time()

lastTime = startTime

lapNum = 1

while True:

    input()

    newTime = time.time()


    print(
        "Lap {}: {} "
        "....... Total time elapsed: {}".format(
            lapNum, round(newTime - lastTime, 2), round(newTime - startTime, 2)
        )
    )

    lapNum += 1
    lastTime = newTime



