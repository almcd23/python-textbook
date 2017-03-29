# x is the variable, containing %d as the variable, defined as 10
x = "There are %d types of people." % 10
#defining binary
binary = "binary"
#defining do not
do_not = "don't"
#placing binary and do_not in this sentence (y) as variables
y = "Those who know %s and those who %s." % (binary, do_not)
#printing it
print x
print y
#re printing x
print "I said: %r." % x
#re printing y
print "I also said: '%s'." % y
#setting hilarious equal to false
hilarious = False
#setting joke evaluation equal to this sentence
joke_evaluation = "Isn't that joke so funny?! %r"
#printing joke evaluation
print joke_evaluation % hilarious
#making 2 more variables
w = "This is the left side of..."
e = "a string with a right side."
#printing those two variables
print w + e
