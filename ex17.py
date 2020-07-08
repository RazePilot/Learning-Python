from sys import argv
from os.path import exists

script, from_file, to_file = argv  # pylint: disable=unbalanced-tuple-unpacking 

# one shitty line, fuck off
print "Copying from %s to %s" % (from_file, to_file) ; in_file = open(from_file) ; indata = in_file.read() ; print "The input file is %d bytes long" % len(indata) ;  print "Does the input file really exist? %r" % exists(to_file) ; print "Does the output file really exist? %r" % exists(from_file) ; out_file = open(to_file, 'w') ; out_file.write(indata) ; print "Alright, all done." ; out_file.close() ; in_file.close()

'''
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()


# here's the more user-friendly version 

print "The input file is %d bytes long" % len(indata)

print "Does the input file really exist? %r" % exists(to_file)
print "Does the output file really exist? %r" % exists(from_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()


out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
'''