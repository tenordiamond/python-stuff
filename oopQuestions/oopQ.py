""" A version of the same quiz game but built with object oriented programing
    First ask the name of player and then how many questions they want
    Print the gameboard and if player press a button, start the game with a countdown from 3
"""
"""TODO"""
# Work with the runGame method to start the actual game


import random
import sys
import time
import os

class GameClass:
    questions = {}
    gameBoard = ""
    
class PlayerClass:
    name = ""
    points = 0

def createPlayer():
    p = PlayerClass
    print("Type your chosen name\n")
    p.name = input()
    p.points = 0

    return p

def createGame(thePlayer):
    print("How many questions do you want 1-6")
    nq = input()
    p = thePlayer
    game = GameClass()
    game.questions = collectQuestions(nq)
    game.gameBoard = createGameBoard(p, nq)
    return game

def createGameBoard(aPlayer, numQuestions):
    name = player.name
    nq = numQuestions
    gameBoard = '####################################################################\nHello ' + name + ' Welcome to the quiz game "Questionz"\nAnswer each of the ' + numQuestions + ' questions as fast as you can to get higher scores\nAnswer y for YES and n for NO\nTo quit press Ctrl-C\n####################################################################'
    return gameBoard

def collectQuestions(usersChoise):
    """ Takes the number of questions that the user stated he/she wants and builds the question dictionary
    """
    questions = []
    #Build question dict below
    with open('questions.txt') as f: # read list of all lines 
        qaList = [line.rstrip() for line in f]
    
    # Put as many questions in the list as the user wants
    # Convert the list into a dictionary
    questions = qaList[:int(usersChoise) * 2 ]
    questions = convertListToDict(questions)
    
    return questions

def convertListToDict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def timeGiver(startTime, answertime):
    tic = startTime
    toc = answertime
    time = int(toc-tic)
    return time

def checkTime():
    #should return time in seconds from when the question was asked
    t = int(time.perf_counter())
    return t


def runGame(user, game):
    #run game in while loop and put a try/catch to fetch ctrl-c for the ending of the game
    # ask questions
    # check start time
    # check if answer correct
    # check end time
    # check total time consumed with timeGiver()
    # set points with total time
    # check if it's game over
    return 0

def intro():
    s = input("To start the game press y and hit enter\n")
    if s == 'y' or s == 'Y':
        return True
    

if __name__ == "__main__":
    
    
    if intro():
        player = createPlayer()
        game = createGame(player)
        print(game.gameBoard,'\n')
        runGame(player, game)
    

    # os.system('clear')
    