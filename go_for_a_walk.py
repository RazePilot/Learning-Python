print "It's a brisk fall evening, and you're sick of being cooped up inside all day."
print "Fancy a walk?"

walk = raw_input("> ")

if walk == "Y" or walk == "y" or walk == "Yes" or walk == "yes":
    print "shouldn't you put your shoes on first?"

    shoes = raw_input("> ")

    if shoes == "Y" or shoes == "y" or shoes == "Yes" or shoes == "yes":
        print "You find a small note inside of your left shoe."
        print "Read the note?"

        read = raw_input("> ")

        if read == "Y" or read == "y" or read == "Yes" or read == "yes":
            print "You open the note"
            print "It reads: \n Dearest friend, I require your immediate assistance. I'm located just south of the old barn, come to me when you get this \n"
            print "Isn't that interesting? You should probably go see what that's all about."
            print "You step out the door into the light of the setting sun."
        







    elif shoes == "N" or shoes == "n" or shoes == "No" or shoes == "no":
        print "Going for a walk without any shoes? Well it's your life, not mine."
        print "You step out the door into the light of the setting sun."

elif walk == "N" or walk == "n" or walk == "No" or walk == "no":
    print "Well, it was a bit cold out anyways. Maybe tomorrow."
