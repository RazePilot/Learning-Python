from sys import argv

string, i = argv # pylint: disable=unbalanced-tuple-unpacking 

f= open("ex%s.py" % i ,"a") 
f.close()
