from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=2, width=120)

Play = Enum("Play", ["Rock", "Paper", "Scissor"])
Outcome = Enum("Outcome", ["Win", "Lose", "Draw"])

# Read the input file. The with statement automatically closes the file after the block
with open("2_in.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def convertToPlay(i):
    if i == "A" or i == "X":
        return Play.Rock
    elif i == "B" or i == "Y":
        return Play.Paper
    elif i == "C" or i == "Z":
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


def getScore(opponentsPlay, myPlay):
    inputScore = myPlay.value
    outcomeScore = {Outcome.Lose: 0, Outcome.Draw: 3, Outcome.Win: 6}[
        getOutcome(opponentsPlay, myPlay)
    ]
    return inputScore + outcomeScore


totalScore = 0
for line in lines:
    (opponentsPlay, myPlay) = [convertToPlay(sym) for sym in line.split()]
    roundScore = getScore(opponentsPlay, myPlay)
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
