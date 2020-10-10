import random #Imports random

def getAnswer(n): #Defines getAnswer(n) n is your variable you chose, so it thinks getAnswer = n and as such they mean the same so by saying n = 4 that makes getAnswer = 4 its essentally the parent value for it
    if n == 0: #Assigns n = 0 if it gets landed on in the randint part of the code
        return 'It is certain' #If it lands on 0 then it will then return to this value of 'It is certain'
    elif n == 1:
        return 'Without a doubt'
    elif n == 2:
        return 'You may rely on it'
    elif n == 3:
        return 'Yes, definitely'
    elif n == 4:
        return 'It is decidely so'
    elif n == 5:
        return 'Ask again later'
    elif n == 6:
        return 'Most likely'
    elif n == 7:
        return 'Reply hazy, try again'
    elif n == 8:
        return 'My sources say no'
    elif n == 9:
        return 'Very doubtful'

print("Think of a yes/no question, and press enter to see the outcome")#Basic print
raw_input()#Takes user input

print(getAnswer(random.randint(0, 9))) #Takes N and says ok let me take a random interger and say what it means, then print it
#Its says, hey im gonna take one of these random number and check what they mean, and whatever they mean it prints
#Its the same thing for the def getAnswer(n)
#They are part of the parent values for it, so if it draws a 7 for example it assigns n the value of 7, and the value of 7 is the return 'Reply Hazy, try again


#So is this still tripping you up? print(getAnswer(random.randint(0, 9)))
#This is a basic magic 8 ball script, congrats you took your first steps
#Ight man, take it easy