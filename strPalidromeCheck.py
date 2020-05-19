word = input('Please enter a word/string: ')

word =  word.lower()

# determine the length of the word
L = len(word)

flag = True

# run a for loop for helf the length of the word
for i in range(L//2):
    # if word index i == word last index - i
    # L - 1 to give us 6 as last letter is at index 6 due to indexes starting at 0
    # - i, on ther first iteration, i == 0
    if word[i] == word[(L-1) - i]:
        continue
    else:
        flag = False
        break


if flag ==  True:
    print(word, 'is a palindrome')
else:
    print(word, 'is not a palidrome')
        
    
