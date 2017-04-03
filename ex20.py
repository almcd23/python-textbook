# imports the argument
from sys import argv
# defines the argument
script, input_file = argv
# defines the print all function
def print_all(f):
    print f.read()
# defines the rewind function
def rewind(f):
    f.seek(0)
# defines the print a line function
def print_a_line(line_count, f):
    print line_count, f.readline()
# sets current file equal to opening the input file
current_file = open(input_file)

print "First let's print the whole file:\n"
# prints all of the current file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# takes us back to the start of the current file
rewind(current_file)

print "Let's print three lines:"
# prints the first line of the current file
current_line = 1
print_a_line(current_line, current_file)
#prints the second line
current_line += 1
print_a_line(current_line, current_file)
# prints the third line
current_line += 1
print_a_line(current_line, current_file)
