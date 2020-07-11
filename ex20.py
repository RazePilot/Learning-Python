from sys import argv

# makes ipnut_file the thing we type with argv
script, input_file = argv # pylint: disable=unbalanced-tuple-unpacking 

# defines print_all so it reads and prints any file
def print_all(f):
    print f.read()

# makes rewind seek to line 0? I think?
def rewind(f):
    f.seek(0)

# defines print_a_line so it prints line_count and then reads the line
def print_a_line(line_count, f):
    print line_count, f.readline()

# opens the input file we defined with argv
current_file = open(input_file)

print "First let's print the whole file:\n"

# self explanatory
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewinds, still not sure how seek works, a force movement for reading?
rewind(current_file)

print "Let's print three lines:"

# moves to the current line, being 1, then prints the contents of the line
current_line = 1
print_a_line(current_line, current_file)

# does the same thing, but reads the next line
current_line += 1
print_a_line(current_line, current_file)

# same as above
current_line += 1
print_a_line(current_line, current_file)