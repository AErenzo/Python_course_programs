phrase =  input('Please enter a phrase: ')

# strip white spacing from the phrase 
phrase = phrase.strip()

# change the phrase to upper case
phrase =  phrase.upper()

# create new variable containing the phrase split into seperate items
words = phrase.split()

# create empty list for first letter of each item in words 
letters = []

# for loop going through each item in words, extracting the first letter and adding it to letters
for i in words:
    letters.append(i[0])

# create new vaiable - joining each item in the letters list using no space. Saved as a new vairbale
avb = ''.join(letters)

print(avb)



