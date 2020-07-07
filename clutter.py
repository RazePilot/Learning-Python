from sys import argv

script, number = argv # pylint: disable=unbalanced-tuple-unpacking 

for i in range(0, int(number)):
    f= open("Clutter%d.txt" % i ,"w+") 
    f.close()