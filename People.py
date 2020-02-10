from random import randint, shuffle
from turtle import Turtle, Screen, Shape
import winsound
import sys
import time
class Person:
    def __init__(self, color, x, y):
        self.color = color
        self.t = Turtle(shape='circle')
        self.t.penup()
        self.xpos = x
        self.ypos = y
        self.f = Shape('compound')
    def birth(self, s, name):
        self.t.shapesize(0.7)
        arms = ((15,-10),(15,10))
        body = ((9,0), (30,0))
        leftleg = ((30,0),(38,-8))
        rightleg = ((30,0), (38, 8))
        self.f.addcomponent(arms, self.color)
        self.f.addcomponent(body, self.color)
        self.f.addcomponent(leftleg, self.color)
        self.f.addcomponent(rightleg, self.color)
        self.f.addcomponent(self.t.get_shapepoly(), self.color)
        s.register_shape(name, self.f)
        self.t.shape(name)
    def goTo(self):
        self.t.speed('fastest')
        self.t.goto(self.xpos, self.ypos)
    def death(self):
        self.t.clear()
def generateNames(names, numpeople):
    for i in range(numpeople):
        names.append(str(i))
def switchPeople(people): #work on !!!!
    for p in people:
        pass
def numColor(people, color):
    f = 0
    for p in people:
        if p.color==color:
            f+=1
    return f
def writeAt(t, message, x, y, color, size, align):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.color(color)
    style = ('Courier', size, 'bold')
    t.write(str(message), font=style, align=align)

def writeAtB(t, message, x, y, color, size):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.color(color)
    style = ('Courier', size, 'bold')
    t.write(str(message), font=style)

colors = ['red', 'orange', 'yellow', 'dark green', 'blue', 'purple']
winsound.PlaySound('C:\\Users\\rober\\Desktop\\PythonPracticeFiles\\APCSPeopleGame\\Flyflyfly', winsound.SND_ASYNC)
s = Screen()
s.screensize()
s.setup(width = 1.0, height = 1.0)
screenheight = s.window_height()
screenwidth = s.window_width()
s.bgcolor('black')
rules = Turtle()
writeAt(rules, 'People in a City', 0, 0, 'white', 30, 'center')
time.sleep(5)
timeseconds = 0
rules.clear()
writeAtB(rules, 'You have 10 seconds to observe the crowd.', -480, 150, 'white', 16)
writeAtB(rules, 'Your score is the absolute value of the difference between your guess and the actual amount.', -480, 120, 'white', 16)
writeAtB(rules, 'Smaller score = better. (0 is the best)', -480, 90, 'white', 16)
writeAtB(rules, 'A window will pop up for you to submit response.', -480, 60, 'white', 16)
writeAtB(rules, 'Press enter to submit.', -480, 30, 'white', 16)
writeAtB(rules, 'Good luck! Have fun.', -480, 0, 'white', 20)
while timeseconds < 10:
    timeseconds+=1
    time.sleep(1)
rules.clear()
screencolor = colors[randint(0, len(colors)-1)]
s.bgcolor(screencolor)
people = []
grayGame = False

def checkTooClose(x, y, people):
    distance = 0
    for i in people:
        xdiff = i.t.position()[0]-x
        ydiff = i.t.position()[1]-y
        if abs(xdiff) < 20 and abs(ydiff) < 45:
            return False
    return True

def drawingColor(i, grayindex, randcolor):
    if i == grayindex:
        return 'gray'
    return randcolor

def adjustSpeed(people):
    for i in people:
        i.t.speed('fastest')

def gotoEach(people, color, t, speed):
    t.speed(speed)
    firstDone = False
    numtimes = 1
    numberwriter = Turtle()
    numberwriter.hideturtle()
    t.color(color)
    t.hideturtle()
    for p in people:
        if p.color == color:
            t.goto(p.xpos, p.ypos)
            writeNumber(numberwriter, numtimes, p.xpos, p.ypos)
            if not firstDone:
                t.pendown()
                firstDone = True
            numtimes+=1

def writeNumber(t, number, x, y):
    t.penup()
    t.goto(x,y)
    t.color('black')
    style = ('Courier', 16, 'italic')
    t.write(str(number), font=style, align='center')
    time.sleep(0.5)
    
def writeDigits(t, numlist):
    t.goto(500, 0)
    style = ('Courier', 18, 'bold')
    for i in numlist:
        t.write(str(i), font=style, align='center')
        t.forward(15)

def listToNum(arr):
    k = len(arr) - 1
    answer = 0
    for i in arr:
        answer += i * (10** k)
        k-=1
    return answer
def countdown(t, seconds, time):
    t.goto(-300,280)
    for i in range(seconds, -1, -1):
        t.color('black')
        writeAtB(t, i, screenwidth/2-100, screenheight/2-100, 'black', 40)
        time.sleep(1)
        t.clear()
def disappear(t):
    t.hideturtle()
    t.penup()

numpeople = s.numinput('Generate people', "How many people are in the city?", default=20, minval=20, maxval=150)
while numpeople is None or int(numpeople)!=numpeople:
    numpeople = s.numinput('Generate people', "How many people are in the city?", default=20, minval=20, maxval=150)
numpeople = int(numpeople)
print(numpeople)
names = []
generateNames(names, numpeople)
windowsizex = 290
windowsizey = 290
if grayGame:
    grayindex = randint(0,numpeople-1)
else:
    grayindex = numpeople

i = 0
loading = Turtle()
disappear(loading)
loading.speed('fastest')
writeAtB(loading, 'Loading', -100, screenheight/2 - 100, 'black', 30)
loadingx = loading.position()[0]
loadingx+=150
while i < numpeople:
    randx = randint(-windowsizex, windowsizex)
    randy = randint(-windowsizey, windowsizey)
    randcolor = colors[randint(0,len(colors)-1)]
    if i==0 or checkTooClose(randx, randy, people):
        c = drawingColor(i, grayindex, randcolor)
        p = Person(c, randx, randy)
        p.birth(s, names[i])
        s.update()
        p.goTo()
        people.append(p)
        i+=1
    if i%(numpeople//4)==0:
        pos = loadingx
        dots = Turtle()
        disappear(dots)
        dots.speed(4)
        time.sleep(0.4)
        for r in range(3):
            pos += 15
            writeAtB(dots, '.', pos, screenheight/2 - 100, 'black', 30)
        time.sleep(0.7)
        dots.clear()
loading.clear()
s.bgcolor('white')
if grayGame:
    people[grayindex].t.speed('slowest')
    people[grayindex].t.goto(0,0)
    people[grayindex].t.circle(50)
adjustSpeed(people)
numcolorpeople = numColor(people, screencolor)
timer = Turtle()
disappear(timer)
questionwriter = Turtle()
disappear(questionwriter)
print(numcolorpeople)
writeAt(questionwriter, 'How many '+ screencolor + ' people are there?', 0, screenheight/2-100, 'black', 30, 'center')
countdown(timer, 10, time)
questionwriter.clear()
s.bgcolor(screencolor)
guess = s.numinput(screencolor + ' people', "How many " + screencolor + " people are there?", default=0, minval=0, maxval=numpeople)
while guess is None or int(guess)!=guess:
    guess = s.numinput(screencolor + ' people', "How many " + screencolor + " people are there?", default=0, minval=0, maxval=numpeople)
score = abs(guess - numcolorpeople)
scorewriter = Turtle()
disappear(scorewriter)
writeAtB(scorewriter, 'Score:', -1*screenwidth/2 +100, screenheight/2-100, 'black', 50)
t = Turtle()
disappear(t)
s.bgcolor('white')
writeAtB(scorewriter, 'Guess:', screenwidth/2 - 350, screenheight/2-100, 'black', 50)
writeAtB(scorewriter, int(guess), screenwidth/2 - 200, screenheight/2-250, 'black', 50)
if numcolorpeople > 17:
    gotoEach(people, screencolor, t, 'fast')
else:
    gotoEach(people, screencolor, t, 3)
writeAtB(scorewriter, int(score), -1*screenwidth/2 +200, screenheight/2-250, 'black', 50)
if score == 0:
    writeAtB(scorewriter, 'Perfect!', -1*screenwidth/2 +100, screenheight/2-320, 'black', 50)
    winsound.PlaySound("C:\\Users\\rober\\Desktop\\PythonPracticeFiles\\APCSPeopleGame\\Kids Saying Yay [Sound Effect]", winsound.SND_FILENAME)
winsound.PlaySound('C:\\Users\\rober\\Desktop\\PythonPracticeFiles\\APCSPeopleGame\\Flyflyfly', winsound.SND_ASYNC)
s.clear()
s.bgcolor('black')
writeAt(scorewriter, 'Created By:', 0, 150, 'white', 45, 'center')
writeAt(scorewriter, 'EpIcCrEaToR', 0, 50, 'white', 45, 'center')
time.sleep(1.3)
scorewriter.clear()
writeAt(scorewriter, 'Programming By:', 0, 150, 'white', 45, 'center')
writeAt(scorewriter, 'EpIcPrOgRaMmEr', 0, 50, 'white', 45, 'center')
time.sleep(1.3)
scorewriter.clear()
writeAt(scorewriter, 'Beats By:', 0, 150, 'white', 45, 'center')
writeAt(scorewriter, 'EpIcBeAtZmAkEr', 0, 50, 'white', 45, 'center')
time.sleep(1.3)
scorewriter.clear()
writeAt(scorewriter, 'Thanks for playing!', 0, 0, 'white', 45, 'center')
s.exitonclick()