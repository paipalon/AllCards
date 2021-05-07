
##############################################################################
#
# Blackjack miniprojekti esittely. Toimii vain codeskulptorilla.
# https://py3.codeskulptor.org/
#
# Lisätty Card luokkaan get_suit ja get_rank metodit.
#
# Draw-metodina korttipakan kaikkien korttien piirtäminen
#
# TEKIJÄ:        Päivi Palonen
# LUONTI_PVM:    20.04.2021
# TIEDOSTO_NIMI: Miniprojekti_3.py
# VERSIO:        1.0 
#
##############################################################################

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)      # pelikortin koko, älä muuta
CARD_CENTER = (36.5, 49)  #pelikortin keskikohta, älä muuta
CARD_SPACE = 5            # korttien väli,  älä muuta
# seuraavien kahden rivin paikkakoordinaatteja voit muuttaa

DEALER_VERT_POS, DEALER_VTEXT, SCORE_VPOS = 200, 180, 100 
PLAYER_VERT_POS, PLAYER_VTEXT, OUTCOME_VTEXT = 400, 380, 580

card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")

p = (3.0,6.0) #koordinaatit

# initialize some useful global variables
in_play = False
outcome = "Deal ?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)
            
    def __str__(self):
        
        return str(self.suit) + str(self.rank)

    # Lisäys PP: maan ja arvon palauttavat metodit
    
    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    #def draw(self, canvas, pos):
        #canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_CENTER[0], DEALER_VERT_POS + CARD_CENTER[1]], CARD_SIZE)

        
# define hand class
class Hand:
    def __init__(self,name):
        pass
        
    def __str__(self):
        pass


                    
    def draw(self, canvas, p):
        pass
           
             
        
# define deck class
class Deck:
    def __init__(self):
        pass

    # add cards back to deck and shuffle
    def shuffle(self):
        pass

    def deal_card(self):
        
        # mieti mitä tapahtuu korttipakalle, kun siitä jaetaan kortti
        pass
            

#define event handlers for buttons
def deal():
    global outcome, in_play, score

    # tähän koodia
    #     
    in_play = True
    outcome = "Hit or stand ?"

def hit():
    
    global outcome, in_play, score
    
    # if the hand is in play, hit the player
    # replace with your code below
    # if busted, assign an message to outcome, update in_play and score
    
def stand():
    global in_play,score,outcome
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        # deal until hand value is 17 or more
        
        in_play = False
    # assign a message to outcome, update in_play and score

    
# Lisäys PP: draw handler piirtää tässä ohjelmassa kaikki kortit  
def draw(canvas):
    #for index in range(0,4): #maan mukaan riville
    for s in range(0,4): #arvon mukaan sarakkeeseen
        for r in range(0,14): #arvon mukaan sarakkeeseen
            card = Card(SUITS[s],RANKS[r])
            
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * s,
            CARD_CENTER[1] + CARD_SIZE[1] * r)

            print("Muuttuja card_loc sai arvon",card_loc)
            
            canvas.draw_image(card_images, card_loc, CARD_SIZE[0],
            [p[0] + CARD_CENTER[0] + r *(CARD_SIZE[0] + CARD_SPACE),
            p[1] + CARD_CENTER[1]], CARD_SIZE[1])
            
            
    # test to make sure that card.draw works, replace with your code below

    #canvas.draw_text("Pelinnimi", (100, SCORE_VPOS), 30, "Navy")
    #canvas.draw_text("pISTEET: " + str(score), (350, SCORE_VPOS), 30, "Black")
    #canvas.draw_text("jAKAJA", (10, DEALER_VTEXT), 20, "Black")  
    #canvas.draw_text("PELAAJA", (10, PLAYER_VTEXT), 20, "Black")
    #canvas.draw_text(outcome, (50, OUTCOME_VTEXT), 20, "Maroon")
    #player_hand.draw(canvas, [0, PLAYER_VERT_POS])
    #dealer_hand.draw(canvas, [0,DEALER_VERT_POS])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
#frame.add_button("Deal", deal, 200)
#frame.add_button("Hit",  hit, 200)
#frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
player_hand = Hand("player")
dealer_hand = Hand("dealer")
deck = Deck()

# get things rolling
frame.start()


