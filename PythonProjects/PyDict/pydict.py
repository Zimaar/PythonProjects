from nltk.corpus import wordnet

meaning = input("Enter one word to find the meaning: ")
syns = wordnet.synsets(meaning)
print(syns[0].definition())

