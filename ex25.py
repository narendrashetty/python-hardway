#string functions

def break_words(stuff):
	words = stuff.split(' ')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	word = words.pop(0)
	print word
	
def print_last_word(words):
	word = words.pop(-1)
	print word
	
def sort_sentence(sent):
	words = break_words(sent)
	return sort_words(words)
	
def print_first_n_last(sent):
	words = break_words(sent)
	print_first_word(words)
	print_last_word(words)
	
def print_first_n_last_sorted(sent):
	words = sort_sentence(sent)
	print_first_word(words)
	print_last_word(words)
	
print """
break word : %s
sort word : %s
""" % (break_words("Hi How Am I"), sort_words(break_words("Hi How Am I")))

print_first_word(break_words("Hi How Am I"))
print_last_word(break_words("Hi How Am I"))