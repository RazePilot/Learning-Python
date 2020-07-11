def houses(a, b):
    print "I don't own any houses, but if I could I would own %d + %d of them." % (a, b)
    return a + b 

amount = houses(5, 4)

print amount


def addition(a, b):
    return a + b

print "Do you have any numbers you would like to add?"
input_test = addition(int(raw_input()), int(raw_input()))

print "That equals %d" % input_test
