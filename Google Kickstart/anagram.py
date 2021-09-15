"""
Problem
Let S be a string containing only letters of the English alphabet. An anagram of S is any string that contains exactly the same letters as S (with the same number of occurrences for each letter), but in a different order. For example, the word kick has anagrams such as kcik and ckki.

Now, let S[i] be the i-th letter in S. We say that an anagram of S, A, is shuffled if and only if for all i, S[i]≠A[i]. So, for instance, kcik is not a shuffled anagram of kick as the first and fourth letters of both of them are the same. However, ckki would be considered a shuffled anagram of kick, as would ikkc.

Given an arbitrary string S, your task is to output any one shuffled anagram of S, or else print IMPOSSIBLE if this cannot be done.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line, a string of English letters.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a shuffled anagram of the string for that test case, or IMPOSSIBLE if no shuffled anagram exists for that string.

Limits
Memory limit: 1 GB.
1≤T≤100.
All input letters are lowercase English letters.

Test Set 1
Time limit: 20 seconds.
1≤ the length of S ≤8.

Test Set 2
Time limit: 40 seconds.
1≤ the length of S ≤10**4.
"""
def shuffler(input_file):

    not_a_match = 'IMPOSSIBLE'
    
    input_file = input_file.split("\r\n")

    #print(input_file[1:])
    
    #do we need this ? 
    #num_cases = input_file[0]

    for index,word in enumerate(input_file[1:]):

        word_length = len(word)
        
        #shuffle the word
            #if during the shuffling, shuffle[i] == word[i], break that shuffle and shuffle again

        scramble_match = ""
        loop_limit = 500
        found_signal = False
        while not found_signal & loop_limit > 0:
            scrambled_indeces = sample(range(word_length),word_length)
            scrambled_word = "".join([word[index] for index in scrambled_indeces])

            for i, char in enumerate(scrambled_word):
                if char == word[i]:
                    #print("{} is the {}th letter of {}".format(char, i, word))
                    continue

                scramble_match = scrambled_word
                found_signal = not found_signal
            
            loop_limit -= 1
        
        if not found_signal:
            scramble_match = not_a_match

            #test
            #found_signal = not found_signal
        
        print("Case #{}: {}".format(index + 1, scramble_match))


def main():

    shuffler(pyperclip.paste())




if __name__ == "__main__":
    import pyperclip
    from random import sample
    from functools import lru_cache   

    main()