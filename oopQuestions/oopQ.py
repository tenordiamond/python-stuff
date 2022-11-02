""" a version of the same quiz game but built with object oriented programing"""

class GameClass:
    questions = {}
    pTime = 0

class PlayerClass:
    name = ""
    points = 0

def collectQuestions(usersChoise):
    #takes the number of questions that the user stated he/she wants
    questions = []
    return questions

def timegiver():
    # set start time for points calculation
    tic = checkTime()
    # set end time for points calculation
    toc = checkTime()
    # the time it took for user to answer is 'end time' - 'start time'
    time = int(toc-tic)
    
    return time

#def runGame(user, game):
    #while true:

if __name__ == "__main__":
    print("HELLO")
