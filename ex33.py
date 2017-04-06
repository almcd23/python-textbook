def buildList(x, y):
    numList = []
    i = 0
    while i < x:
        print "At the top i is %d" % i
        numList.append(1)

        i += y
        print "Numbers now: ", numList
        print "At the bottom i is %d" % i

buildList(5, 2)
