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

def CreatePlayer():
    p = PlayerClass
    print("Type your chosen name\n")
    p.name = input()
    p.points = 0

    return p

def CreateGame():
    print("How many questions do you want 1-6")
    nq = input()
    game = GameClass()
    game.questions = collectQuestions(nq)
    game.gameBoard = "ASDASASDASASDSADASDASD"
    return game

def collectQuestions(usersChoise):
    """ Takes the number of questions that the user stated he/she wants and builds the question dictionary
    """
    questions = {}
    print("USER CHOISE IS: " + usersChoise)
    #Build question dict below
    with open('questions.txt') as f: # read list of all lines 
        klist = f.read().splitlines()
        #must build list with as many questions as user demands!?? HOW??
 
    questions = convert_list_to_dict(l)
    
    print(usersChoise)
    return questions

def convert_list_to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def timegiver(startTime, answertime):
    tic = startTime
    toc = answertime
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
    
    if intro():
        player = CreatePlayer()
        game = CreateGame()
        # print(game.gameBoard,'\n')
        print(game.questions)

    # os.system('clear')
    