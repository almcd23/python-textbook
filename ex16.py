# imports an argument
from sys import argv
# the script and filename are the argument
script, filename = argv
# offers to erase the file
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# asks for input
raw_input ("?")
# opens the file
print "Opening the file..."
target = open(filename, 'w')
# erases the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# re writes the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# writes the lines to the file
target.write('%r\n%r\n%r\n' % (line1, line2, line3))
# closes the file
print "And finally, we close it."
target.close()
