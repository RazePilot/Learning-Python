from sys import argv

script, filename = argv # pylint: disable=unbalanced-tuple-unpacking 

print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."

# this is weird, look more into it 
target.write(line1 + '\n' + line2 + '\n' + line3)


print "And finally, we close it."
target.close()