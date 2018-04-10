#Create a list for emotions and user actions that will coorespond to the grid of reactions
#Create a grid of reacions for how the AI will react

def startEmotion():
#Make random generator for the start emotion
    pass

def action():
#Get user input for the action
    pass
	
def quitCheck(act):
#check for quit input to end the loop
    pass

def getNewEmot(act, emotion):
#get the next emotion from the grid and return the result as a number
    pass
def intro():
#Prompt the intro message and get the first action for the loop
    emote = startEmotion()
    act = action()
#    return emote, act
    pass

def loop(emote, act):
    #primary loop, prompt user and call funcitons
    while quitCheck(act):
        emote = getNewEmot(act, emote)
        act = action()

def end():
#The end prompt
	print('Goodbye.')

def main():
#Emote and act will be the current emotion and user action
    emote, act = intro()
    loop(emote, act)
    end()

main()
