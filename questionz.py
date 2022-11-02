import random
import sys
import time

testQuestionDictionary = {}
alist = []
with open('questions.txt') as f: # read list of all lines 
    l = f.read().splitlines()
    # print(l)
        
def convert_list_to_dict(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

testQuestionDictionary = convert_list_to_dict(l)
# allreadyAsked = []
start = False
points = 0
# put all the questions in a list
l = list(testQuestionDictionary.keys())


print('####################################################################')
print('Welcome to the quiz game "Questionz"                             ###')
print('Answer each question as fast as you can to get higher scores     ###')
print('Answer y for YES and n for NO                                    ###')
print('To quit press Ctrl-C                                             ###')
print('####################################################################')
s = input("to start press y and hit enter\n")

if s == 'y' or s == 'Y':
    start = True

# needs to set a timer DONE
# needs to arrange a way to flag questions as used ( or delete them after asked) Partially DONE
# needs a point system (based on time?) DONE
# needs to fetch questions randomly DONE
# needs a function to se if answers correct DONE
# ask how many questions the user would like
# check when there is no more questions DONE
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

def checkTime():
    #should return time in seconds from when the question was asked
    t = int(time.perf_counter())
    return t

def checkAnswer(answer, theQuestion):
    # handle if user input is upper case
    answer = answer.lower()

    if answer == testQuestionDictionary[theQuestion]:
        print("GOOD JOB\n")        
    else:
        print("SORRY WRONG ANSWER\n")
        
def askQuestion(theQuestion):
    print(theQuestion)
    # set start time for points calculation
    tic = checkTime()
    """need a different way instead of removing questions, maybe put each used
     question in another list and check against it ever time a new questions 
     is about to be asked"""
    l.remove(theQuestion)
    answer = input()
    # set end time for points calculation
    toc = checkTime()
    # the time it took for user to answer is 'end time' - 'start time'
    time = int(toc-tic)
    
    #set points with separate methods
    checkAnswer(answer, theQuestion)
    p = setPoints(time)
    return p

while start:
    try:
        # check if there are no questions left in l and present the players score
        if len(l) == 0:
            print("END OF GAME")
            print("YOUR SCORE: " + str(points))
            break

        # shuffle each iteration to allways assign a random question from l to parameter q
        random.shuffle(l)
        q = l[0]
        # askQuestion returns a point value by calling setPoints inside askQuestion
        val = askQuestion(q)
        points += val
    except KeyboardInterrupt:
        sys.exit(0)



