#sets people to 40
people = 40
#sets cars to 40
cars = 40
#sets buses to 40
buses = 40
#if cars is greater than people, do whats in the branch, if not, move on
if cars > people:
    print "We should take the cars."
#if the first if statement was false, run this instead
elif cars < people:
    print "We should not take the cars."
    #if neither the if or elif are true, print this
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we should take the cars."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."