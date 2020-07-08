from sys import argv

script, filename = argv # pylint: disable=unbalanced-tuple-unpacking 

print "Time to read %r." % filename

print "Ready to see what lies within?"
raw_input("> ")

target = open(filename)

print target.read()

print "Were you satisfied with what you saw?"
raw_input("> ")

print "It seems my program was a success, congratulations! This file will now close."
target.close()