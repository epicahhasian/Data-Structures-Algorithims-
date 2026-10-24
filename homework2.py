
def countdown(rocketcount): 
    if rocketcount <= 0:
        print ("Blast Off!")
        return rocketcount 
    else: 
        print (rocketcount)
        return countdown (rocketcount -1)


countdown(5)