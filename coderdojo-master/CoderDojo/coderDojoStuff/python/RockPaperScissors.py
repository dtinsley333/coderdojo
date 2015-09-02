playerOne=input('Player One, Choose rock, paper, or scissors:  ')
playerTwo=input('Player Two, Choose rock, paper, or scissors:  ')


if (playerOne == 'rock' and playerTwo == 'rock'):
    print("Tie.")
if (playerOne == 'rock' and playerTwo == 'scissors'):
    print ("Player 1 wins.")
if (playerOne == 'rock' and playerTwo == 'paper'):
    print("Player 2 wins.")

    
#figure out what should happen if player one picks scissors and player two picks rock.
