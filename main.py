import random

gameChoices = ["Rock","Paper","Scissors"]
playerScore = 0
computerScore = 0
roundsPlayed = 0
anotherRound = 1

def playRound(playerChoice, computerChoice):
    global playerScore, computerScore
    if playerChoice == computerChoice:
        print("Player choice is: " + playerChoice)
        print("Computer choice is: " + computerChoice)
        print("THIS GAME IS A DRAW")
    elif(playerChoice == "Rock" and computerChoice == "Scissors" 
        or playerChoice == "Paper" and computerChoice == "Rock" 
        or playerChoice == "Scissors" and computerChoice == "Paper"):
        playerScore += 1
        print("Player choice is: " + playerChoice)
        print("Computer choice is: " + computerChoice)
        print("PLAYER 1 WIN")
    else:
        computerScore += 1
        print("Player choice is: " + playerChoice)
        print("Computer choice is: " + computerChoice)
        print("COMPUTER WIN")
    print("Player Score: " , playerScore)
    print("Computer Score: " , computerScore)

def game():
    global anotherRound, roundsPlayed
    if roundsPlayed == 0:
       print("WELCOME")
    else:
        print("¿U Wanna play more? ")
        print("1. yes ")
        print("or press any key if not")
        anotherRound = int(input())
        if anotherRound != 1:
            return
    print("Select your option: 1. Rock 2. Paper 3. Scissors")
    playerIndex = int(input())
    playerChoice = gameChoices[playerIndex - 1]

    computerIndex = random.randint(0,2)
    computerChoice = gameChoices[computerIndex]

    playRound(playerChoice, computerChoice)
    roundsPlayed += 1

while True:
    game()
    if anotherRound != 1:
        print("good bye")
        break
