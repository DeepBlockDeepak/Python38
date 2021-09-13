#counts number of occurrences of a letter in a string
message= "It was a bright cold day in April, and the clocks were striking thirteen."
import pprint #for pretty printing the 'count' list with pprint() method
count ={}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
print ("=======", end = "\n" *2)
message_text = pprint.pformat(count)
print (message_text)
