""" A version of the same quiz game but built with object oriented programing
    First ask the name of player and then how many questions they want
    Print the gameboard and if player press a button, start the game with a countdown from 3
"""
"""TODO"""
# Work with the runGame method to start the actual game
# comment all stuff to make it more understandable


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
    try:
        questions = []
        #Not efficient to read all the lines from the file if the user only wants a couple of them. What if the file contains 100k questions
        #In the future implement a database
        with open('questions.txt') as f: # read list of all lines 
            qaList = [line.rstrip() for line in f]
        
        # Put as many questions in the list as the user wants
        # Convert the list into a dictionary
        questions = qaList[:int(usersChoise) * 2 ]
        questions = convertListToDict(questions)
    except ValueError:
        print(usersChoise + " is not a number\n Restart")
        sys.exit()
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

def askQuestion(theQuestion):
    q = theQuestion

def checkAnswer(answer, game, question):
    # if the answer match the value of the key in question dictionary return true
    if answer == game.questions.get(question):
        # print("EASY")
        return True
    else:
        return False

def gameOn(gameQuestions, counter):
    if len(gameQuestions) == counter:
        return False
    else:
        return True

def setPoints(time):
    p = 0
    if time < 1:
        p = 100
    elif time > 1 and time < 4:
        p = 5
    else:
        p = 1
    if p > 120:
        p += 150
    return p

def presentResult(playerPoints):
    print('Good job, your  total score is: ' +  str(playerPoints))


def runGame(player, game):
    p = player
    g = game
    
    #run game in while loop and put a try/catch to fetch ctrl-c for the ending of the game
    while True:
        try:
            # ask questions
            
            for q in game.questions:
                # check start time
                st = checkTime()
                #print question to user ant take the answer as input
                print(q)
                a = input("Yes or No? ")
                # check end time
                et = checkTime()
                # check if answer correct
                print(checkAnswer(a, g, q)) #need to make this function
                # check total time consumed with timeGiver()
                totalTime = timeGiver(st, et)
                if checkAnswer(a, g, q):
                    # set points with total time
                    player.points += setPoints(totalTime) #m??ste fixa en metid f??r setPoints
            presentResult(int(player.points))
            break   
        except KeyboardInterrupt:
            sys.exit(0)
    
    
    return 0

def intro():
    s = input("To start the game press y and hit enter\n")
    if s == 'y' or s == 'Y':
        return True
    
def ready():
    s = input("READY?  y/n\n")
    if s == 'y' or s == 'Y':
        return True

if __name__ == "__main__":
    
    
    if intro():
        player = createPlayer()
        game = createGame(player)
        print(game.gameBoard,'\n')
        if ready():
            runGame(player, game)
    

    # os.system('clear')
    