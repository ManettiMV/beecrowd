'''
Your little brother has just learnt to write one, two and three, in English. He has written a 
lot of those words in a paper, your task is to recognize them. Note that your little brother is 
only a child, so he may make small mistakes: for each word, there might be at most one wrong letter. 
The word length is always correct. It is guaranteed that each letter he wrote is in lower-case, and 
each word he wrote has a unique interpretation.

Input
The first line contains the number of words that your little brother has written. Each of the 
following lines contains a single word with all letters in lower-case. The words satisfy the 
constraints above: at most one letter might be wrong, but the word length is always correct. 
There will be at most 1000 words in the input.

Output
For each test case, print the numerical value of the word.
'''

one = "one"
quantity = int(input())
for _ in range(quantity):
    word = input()

    if len(word) == 5:
        print(3)
    else:
        similaritys = sum([1 if word[i] == one[i] else 0 for i in range(3)])
        if(similaritys > 1):
            print(1)
        else:
            print(2)