""" A version of the same quiz game but built with object oriented programing
    First ask the name of player and then how many questions they want
    Print the gameboard and if player press a button, start the game with a countdown from 3
"""
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

def collectQuestions(usersChoise):
    """ Takes the number of questions that the user stated he/she wants and builds the question dictionary
    """
    questions = {}
    #Build question dict below
    return questions

def timegiver(startTime, answertime):
    time = int(toc-tic)
    
    return time

def checkTime():
    #should return time in seconds from when the question was asked
    t = int(time.perf_counter())
    return t


#def runGame(user, game):
    #while true:

def intro():
    print('####################################################################')
    print('Welcome to the quiz game "Questionz"                             ###')
    print('Answer each question as fast as you can to get higher scores     ###')
    print('Answer y for YES and n for NO                                    ###')
    print('To quit press Ctrl-C                                             ###')
    print('####################################################################')
    s = input("To start the game press y and hit enter\n")
    if s == 'y' or s == 'Y':
        return True
    

if __name__ == "__main__":
    intro()
    os.system('clear')
    