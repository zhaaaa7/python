# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
# further revised by Karthik Ramanathan and Megh Marathe
import nltk
import nltk.data
import random
from nltk import word_tokenize,sent_tokenize

def main():
	text_data = ""
	tagmap = {"NN":"a noun","NNS":"a plural noun", "NNP": "a proper noun", "NNPS": "a plural proper noun", 
				"JJ":"an adjective", "JJR":"a comparative adjective (ex: 'larger')", "JJS":"a superlative adjective (ex: 'largest')"}
	final_words = []

	# TODO 1: Read the text file "gutenberg.txt" and store it in the variable text_data
	# Write your code here
	text_data=open('gutenberg.txt','r').read()

	tokens = nltk.word_tokenize(text_data)
	tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

	# TODO 2: Create a list of i) nouns and ii) adjectives and print the two lists
	# Write your code here
	n_l=[]
	a_l=[]
	for i in tagged_tokens:
		if i[1] in ['NN','NNS','NNP','NNPS']:
			n_l.append(i[0])
		if i[1] in ['JJ','JJR','JJS']:
			a_l.append(i[0])
			
	print(n_l)
	print(a_l)

	sel_nouns = random.sample(n_l,2)
	sel_adjs = random.sample(a_l,2)
	print(sel_nouns)
	print(sel_adjs)

	# TODO 3: Randomly sample two of the nouns and store them in the list sel_nouns
	# TODO (ctd): Randomly two of the adjectives and store them in the list sel_adjs
	# Write your code here
 #
	for (word, tag) in tagged_tokens :
		if word in sel_nouns or word in sel_adjs:
			if tag in ['NN','NNS','NNP','NNPS']:
				r=input('enter a noun:')
				final_words.append(r)
			if tag in ['JJ','JJR','JJS']:
				r=input('enter a noun:')
				final_words.append(r)
		else:
			# TODO 4: If the word is among the randomly selected nouns or adjectives, prompt the user
			# to add a new word and append the new word to the list of final_words.
			# Write your code here
			final_words.append(word)
		
			
# Code for printing the old version of the text
	print("******* OLD TEXT *******")
	print(" ".join(tokens))
	print("\n\n******* NEW TEXT *******")
	# TODO 5: Print the new text
	# Write your code here

main()