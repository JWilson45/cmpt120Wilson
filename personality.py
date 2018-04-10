actions = ['reward', 'punish', 'threaten', 'joke', 'quit']
emotions = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']

reactionChart=[
	[3,3,5,3,3,3],
	[2,0,0,2,1,2],
	[2,0,0,2,2,0],
	[1,4,5,3,3,3]]

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
