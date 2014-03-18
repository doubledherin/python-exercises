# Given a row of "n" lightbulbs in the off position:
# Say you flipped the switch for each one (so that they were all on).
# Then you flipped the switch for each second one (so that every other one was off).
# Then you flipped the switch for each third one ... etc.
# And you did this n times, where n equals the number of lightbulbs.
# What would the final pattern of lightbulbs turned on?

# Thanks to Ava St. John for this challenge!
 
def switchflipper(n):
    
    # create empty list to start
    lights = []
    
    # fill list with n False ("off") values
    for i in range(0, n):
        lights.append(False)
        
    # initiate step variable, which we'll soon start incrementing
    step = 1
    
    # set end boundary for step incrementation
    while step <= len(lights): 
        
        # start flipping switches!
        for j in range(0, len(lights), step):
            lights[j] = not lights[j]
        
        # increment step
        step += 1
    
    # create list of results
    on = []
    for i in range(len(lights)):
        if lights[i] == True:
            on.append(i)
        
    print "After all switch-flipping is complete, the following lightbulbs are on: ", on
    
    # create list showing pattern
    off = []    
    k = 0
    while k < (len(on)-1):
        off.append(on[k+1] - on[k])
        k += 1
        
    print "Here is a list of how many 'off' bulbs are between each 'on' bulb: ", off
    

    
    
switchflipper(1000)