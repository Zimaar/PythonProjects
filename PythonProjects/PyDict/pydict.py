from nltk.corpus import wordnet

word = input("Enter one word to find the meaning: ") #getting user input
syns = wordnet.synsets(word) #using wordnet module to find related synonym set
print(syns[0].definition()) #extracting definition of synonym set and printing

