# imports argv
from sys import argv

# applies filename to argv
script, filename = argv # pylint: disable=unbalanced-tuple-unpacking 

# filename = raw_input('What is the name of the file you are trying to open? ')
# ^used this for testing purposes^

# assigns the variable 'txt' to open the argv
txt = open(filename)

# tells us what file we just opened
print "Here's your file %r:" % filename
# spits out the contents of that file
print txt.read()

# gives the user another instruction
print "Type in the filename again:" 
# gives the user a space to type the file name again 
file_again = raw_input("> ")

# makes the txt_again variable open the file from the above raw input 
txt_again = open(file_again)

# prints txt_again, which opens the file and then spits out its contents with .read
print txt_again.read()
