# imports the argument
from sys import argv
# assigns peramters to the argument
script, filename = argv
# commands the file to open with the txt prompt
txt = open(filename)
# prints out the filename and file
print "Here's your file %r:" % filename
print txt.read()
# prompts you to call the file again
print "Type the filename again:"
file_again = raw_input("> ")
# opens the file again
txt_again = open(file_again)
# prints the file again
print txt_again.read()
