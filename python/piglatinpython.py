###practicing some code with python###

###global variable for ending for PL output###
pyg = 'ay'

###prompt for input###
original = raw_input('Enter a word:')
###if block for formatting
if len(original) > 0 and original.isalpha():
  print original
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  ###logic to check if the first letter in input was uppercase###
  if original[0] == original[0].upper():
      new_word = new_word.title()
      print new_word
  else:
      print new_word
else:
  print 'statement is not a valid string'

print "Does this count as a change for you atom?"