
from sys import argv #import argv from sys

script, filename = argv

text = open(filename).read().lower() #open text file, read whole file and make file all lower case

filename_word_list = text.split() # split the text file into individual word strings

word_tally = {} #create an empty  dictionary

filename_word_list = [x.strip(",") for x in filename_word_list] #strip out commas from the beginning or end of words
filename_word_list = [x.strip(".") for x in filename_word_list] # strip out periods from the beginning or end of words

for word in filename_word_list: #serach through the elements char (our word strings that we created above)
	word_tally[word] = word_tally.get(word, 0) + 1 # for the elements in the dictionary characters for each element char create a value that it points to and iterate through - as an indetical char is identified add 1 and return to the beginning of the for loop

print (word_tally) # print out the dictionary

for word, num in word_tally.iteritems(): #for the dictionary we have created above
	print word, num #print out the key and value side by side


