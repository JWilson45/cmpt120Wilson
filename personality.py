actions = ['reward', 'punish', 'threaten', 'joke', 'quit']
emotions = ['anger', 'disgust', 'fear', 'happiness', 'sadness', 'surprise']
reactions =["I'm getting really ticked off!",'Thats just not right, somethings wrong with you',
            "You're scaring me! Please stop.",'That makes me feel very happy!',"Oh... :( that makes me sad.",
            "Oh my, that certinly is surprising!"]

reactionChart=[
	[3,3,5,3,3,3],
	[2,0,0,2,1,2],
	[2,0,0,2,2,0],
	[1,4,5,3,3,3]]

def text(emote,act):
    print('\nYou preformed the action: {}. The AI, Bill, now has the feeling of: {}'.format(actions[act].capitalize(),emotions[emote].capitalize()))
    print('Bill: ','"' + reactions[emote] + '"')
    

def startEmotion():
#Make random generator for the start emotion
    import random
    return random.randint(0,5)

def action():
#Get user input for the action
    while True:
        try: act = actions.index(input('\nHow will you treat me? (reward, punish, threaten, joke, or quit)\n').lower())
        except:
            print('Invalid command, try again.')
            continue
        return act
	
def quitCheck(act):
#check for quit input to end the loop
    if act == 4:
        return False
    return True

def getNewEmot(act, emotion):
#get the next emotion from the grid and return the result as a number
    emotion = reactionChart[act][emotion]
    return emotion
    
def intro():
#Prompt the intro message and get the first action for the loop
    emote = startEmotion()
    print('Welcome, my name is Bill. My current emotion is: {}'.format(emotions[emote].capitalize()))
    act = action()
    return emote, act

def loop(emote, act):
    #primary loop, prompt user and call funcitons
    while quitCheck(act):
        emote = getNewEmot(act, emote)
        text(emote,act)
        act = action()

def end():
#The end prompt
    print("\nGoodbye.")

def main():
#Emote and act will be the current emotion and user action
    emote, act = intro()
    loop(emote, act)
    end()

main()
