
from sys import argv #import argv from sys

def custom_strip(i):
	new_item = i.replace("?", "")
	new_item = new_item.replace(",", "")
	new_item = new_item.replace(".", "")
	new_item = new_item.replace(";", "")
	new_item = new_item.replace(":", "")
	new_item = new_item.replace("'", "")
	return new_item

script, filename = argv

text = open(filename).read().lower() #open text file, read whole file and make file all lower case

clean_text = custom_strip(text)

filename_word_list = clean_text.split() # split the text file into individual word strings

word_tally = {} #create an empty  dictionary

for word in filename_word_list: #serach through the elements char (our word strings that we created above)
	word_tally[word] = word_tally.get(word, 0) + 1 # for the elements in the dictionary characters for each element char create a value that it points to and iterate through - as an indetical char is identified add 1 and return to the beginning of the for loop

# print (word_tally) # print out the dictionary


for word, num in word_tally.iteritems(): #for the dictionary we have created above
	print word, num #print out the key and value side by side

