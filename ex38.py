ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not ten things on that list. Let's fix that."
# splits the ten_things list
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop(more_stuff)
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    # appends(stuff)
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."
# prints the item at 1 with stuff
print stuff[1]
# prints the last thing of stuff
print stuff[-1]
# returns the last item in stuff
print stuff.pop()
# prints the completed list
print ' '.join(stuff)
# prints list from 3 to 5
print '#'.join(stuff[3:5])
