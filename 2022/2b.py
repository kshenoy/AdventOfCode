from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=2, width=120)

Play = Enum("Play", ["Rock", "Paper", "Scissor"])
Outcome = Enum("Outcome", ["Win", "Lose", "Draw"])

# Read the input file. The with statement automatically closes the file after the block
with open("2_in.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def convertToOutcome(i):
    if i == "X":
        return Outcome.Lose
    elif i == "Y":
        return Outcome.Draw
    elif i == "Z":
        return Outcome.Win


def convertToPlay(i):
    if i == "A":
        return Play.Rock
    elif i == "B":
        return Play.Paper
    elif i == "C":
        return Play.Scissor


def getOutcome(opponentsPlay, myPlay):
    if opponentsPlay == myPlay:
        return Outcome.Draw
    elif (opponentsPlay == Play.Scissor) and (myPlay == Play.Rock):
        return Outcome.Win
    elif (opponentsPlay == Play.Rock) and (myPlay == Play.Scissor):
        return Outcome.Lose
    elif myPlay.value > opponentsPlay.value:
        return Outcome.Win
    else:
        return Outcome.Lose


def getMyPlay(opponentsPlay, desiredOutcome):
    if desiredOutcome == Outcome.Draw:
        return opponentsPlay
    elif desiredOutcome == Outcome.Win:
        if opponentsPlay == Play.Scissor:
            return Play.Rock
        else:
            return Play(opponentsPlay.value + 1)
    else:
        if opponentsPlay == Play.Rock:
            return Play.Scissor
        else:
            return Play(opponentsPlay.value - 1)


def getScore(opponentsPlay, desiredOutcome):
    myPlay = getMyPlay(opponentsPlay, desiredOutcome)
    outcomeScore = {Outcome.Lose: 0, Outcome.Draw: 3, Outcome.Win: 6}[desiredOutcome]
    return myPlay.value + outcomeScore


totalScore = 0
for line in lines:
    (opponentsPlaySym, desiredOutcomeSym) = line.split()
    opponentsPlay = convertToPlay(opponentsPlaySym)
    desiredOutcome = convertToOutcome(desiredOutcomeSym)

    roundScore = getScore(opponentsPlay, desiredOutcome)
    totalScore += roundScore
    # print(
    #     "Opponent played "
    #     + opponentsPlay.name
    #     + " and I played "
    #     + myPlay.name
    #     + ". The score is "
    #     + str(roundScore)
    # )
print("My total score is " + str(totalScore))
