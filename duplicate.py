'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and 
sorting them alphanumerically. Suppose the following input is 
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()

# test
# Define this function to return the expected output
# Do not print it from this function
def singlify(str):
        ori = str.split()
        uni = []
        ori.sort(key = lambda x: x.lower())
        for word in ori:
          for i in range(len(uni)):
            if uni[i].lower() == word.lower():
              break
          else:
            uni.append(word)
        out = ' '.join(uni)
        return out
        pass

print(singlify(sentence))
