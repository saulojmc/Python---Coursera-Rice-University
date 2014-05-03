# implementation of card game - Memory

import simplegui
import random
moves=0

# helper function to initialize globals
def init():
    global listOfCards,exposed,openedCard,clickCounter,moves
    listOfCards=[i for i in range(8)]+[i for i in range(8)]
    random.shuffle(listOfCards)
    exposed=[False for i in range(16)]
    openedCard=[]
    clickCounter=0
    moves=0

     
# define event handlers
def mouseclick(pos):
    global clickCounter,moves
    if clickCounter==0:
        openedCard.append(pos[0]//50)
        exposed[pos[0]//50]=True
        clickCounter+=1
        moves=1
        
    elif clickCounter==1:
        if not (pos[0]//50 in openedCard):
            openedCard.append(pos[0]//50)
            clickCounter+=1
        exposed[pos[0]//50]=True
       
    else:
        if not (pos[0]//50 in openedCard):
            if listOfCards[openedCard[-1]]!=listOfCards[openedCard[-2]]:
                exposed[openedCard[-1]]=False
                exposed[openedCard[-2]]=False
                openedCard.pop()
                openedCard.pop()
            clickCounter=1
            moves+=1
            exposed[pos[0]//50]=True
            openedCard.append(pos[0]//50)

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
        l.set_text("Moves = "+str(moves))
        for i in range(16):
            canvas.draw_line([50*(i%15+1),0], [50*(i%15+1),100], 2, "White")
            if exposed[i]:
                canvas.draw_text(str(listOfCards[i]), [15+50*i,70], 35, "White")
         
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric
