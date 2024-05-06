import random

gameChoices = ["Rock","Paper","Scissors"]
playerScore = 0
computerScore = 0
roundsPlayed = 0
anotherRound = 1

def playRound(playerChoice, computerChoice):
    global playerScore, computerScore
    if playerChoice == computerChoice:

        print("Player choice: " + playerChoice + " Computer choice: " + computerChoice)
        print("°°° THIS GAME IS A DRAW °°°")

    elif(playerChoice == "Rock" and computerChoice == "Scissors" 
        or playerChoice == "Paper" and computerChoice == "Rock" 
        or playerChoice == "Scissors" and computerChoice == "Paper"):

        playerScore += 1
        print("Player choice: " + playerChoice + " Computer choice: " + computerChoice)
        print("!!!!!!!!!!!!! PLAYER 1 WIN !!!!!!!!!!!!!") 

    else:

        computerScore += 1
        print("Player choice: " + playerChoice + " Computer choice: " + computerChoice)
        print("!!!!!!!!!!!!! COMPUTER WIN !!!!!!!!!!!!!")

        print("Player Score: " , playerScore)
        print("Computer Score: " , computerScore)


def game():
    global anotherRound, roundsPlayed
    if roundsPlayed == 0:
       print("WELCOME")
    else:
        print("¿U Wanna play more? \n 1. yes \n or press any key if not")
        anotherRound = int(input())

        if anotherRound != 1:
            return
    print("Select your option: \n 1. Rock \n 2. Paper \n 3. Scissors")
    playerIndex = int(input())
    playerChoice = gameChoices[playerIndex - 1]

    computerIndex = random.randint(0,2)
    computerChoice = gameChoices[computerIndex]

    playRound(playerChoice, computerChoice)
    roundsPlayed += 1

while True:
    game()
    if anotherRound != 1:
        print("BYE")
        break
