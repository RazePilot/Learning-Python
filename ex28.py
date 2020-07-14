a1 = True and True # true
a2 = False and True # false
a3 = 1 == 1 and 2 == 1 # false
a4 = "test" == "test" # true
a5 = 1 == 1 or 2 != 1 # true
a6 = True and 1 == 1 # true
a7 = False and 0 != 0 # false
a8 = True or 1 == 1 # true
a9 = "test" == "testing" # false
a10 = 1 != 0 and 2 == 1 # false
a11 = "test" != "testing" # true 
a12 = "test" == 1 # false
a13 = not (True and False) # true
a14 = not (1 == 1 and 0 != 1) # true
a15 = not (10 == 1 or 1000 == 1000) # false
a16 = not (1 != 10  or 3 == 4) # true
a17 = not ("testing" == "testing" and "Zed" == "Cool Guy") # true
a18 = 1 == 1 and not ("testing" == 1 or 1 == 0) # true
a19 = "chunky" == "bacon" and not (3 == 4 or 3 == 3) # false
a20 = 3 == 3 and not ("testing" == "testing" or "Python" == "fun") # false

print a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20


# Lake: 10011101001011011100
# Answers: 10011101001010001100

print (18.0 / 20.0)
# 90% is good enough for me 