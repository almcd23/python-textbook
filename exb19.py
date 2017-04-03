def animals(cats, dogs, goats, horses):
    print "You have %d cats!" % cats
    print "You have %d dogs!" % dogs
    print "You have %d goats!" % goats
    print "You have %d horses!" % horses



print "You have this many animals: "
animals(12, 6, 10, 2)

print "You have this many animals: "
amount_of_cats = 12
amount_of_dogs = 6
amount_of_goats = 10
amount_of_horses = 2

print "Let's add up how many animals you have: "
animals(12, + 6, + 10, + 2)

print "Let's see how many animals there are now: "
animals(amount_of_cats + 2, amount_of_dogs + 4, amount_of_goats, amount_of_horses + 4)

print "How many animals do you think you have?"
raw_input()

print "There are actually 28."
