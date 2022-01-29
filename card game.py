#import everything that you are going to use.
import random

from tkinter.messagebox import NO, YES



class intro:
    #introduction to the game
    print ("welcome to the card game!")



#the play section responsible for keeping track of the players score and whether or not they want to continue playing.
def play(score):
    #set the win score.
    if score >= 1000:
        print("YOU WIN")
        input()
    
    elif score > 0:
        print (f"\nyou have {score} points.\n")
        error = YES
        #some error handeling 
        while error == YES:
            play_game = False
            # ask if the player wants to play.
            player_in = input("Play Again? [y/n]: ")

            if player_in.lower() == "y":
                play_game = True
                error = NO
            elif player_in.lower() == "n":
                play_game = False
                error = NO

            else:
                error = YES
                print("Error invalid input! please try again.")
            #if the player_in is y then initiate the game.
            if play_game == True:
            
                game(score)
    #set the loose score. 
    elif score <= 0:
        print("GAME OVER")
        input()
 
#the game section is responseable for the meat of the game so picking the random numbers, giving the player a choice, giving responses and recording the player score.
def game(score):

    # create the two random cards
    start_card = random.randrange(1, 14)
    next_card = random.randrange(1, 14)
    #create an if statment to make sure that the cards are not the same.
    if next_card == start_card:
        next_card = random.randrange(1, 14)
    #add a while statment for error handling.
    guess_error = YES
    while guess_error == YES:
        print (f"\nThe start card is {start_card}.")
        player_guess = input("\nHigher or Lower [h/l]: ")
        print(f"The next card is {next_card}.")
        if player_guess.lower() == "l":
            guess_error = NO
        elif player_guess.lower() == "h":
            guess_error = NO
            
        else:
            guess_error = YES
            print("Error invalid input! please try again.")

    #compaire the players input to the cards and send a message and add or remove pt.
    if player_guess.lower() == "h":

        if next_card > start_card:
            print("\nnice you got it! +100 pt")
            score += 100
            play(score)
        elif next_card < start_card:
            print("\nsorry but that was wrong! -75 pt")
            score -= 75
            play(score)

    elif player_guess.lower() == "l":

        if next_card < start_card:
            print("\nnice you got it! +100 pt")
            score += 100
            play(score)
        elif next_card > start_card:
            print("\nsorry but that was wrong! -75 pt")
            score -= 75
            play(score)
start_game = play
game_file = game



class main:
    intro
    #main starts the play portion of the game and gives the starting score. 
    score = 300
    play(score)
    
        

main
