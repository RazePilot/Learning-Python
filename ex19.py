# the only fucking interesting thing here, actually does something cool by making cheese_and_crackers a constant no matter what
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# does it again, more numbers for stuff that doesn't have defined numbers
print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

#makes more unnecessary variables that equal integers 
print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# assigns 10+20 and 5+6 to cheese_count and cracker_count 
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# does addition with the variables and assigns them to cheese_and_crackers, (on top of what it's already defined as) then prints it 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
