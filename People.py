from random import randint, shuffle
from turtle import Turtle, Screen, Shape
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

colors = ['red', 'orange', 'yellow', 'dark green', 'blue', 'purple', 'black']
s = Screen()
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

def gotoEach(people, color, t):
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
    

numpeople = 15
names = []
generateNames(names, numpeople)
windowsizex = 290
windowsizey = 290
if grayGame:
    grayindex = randint(0,numpeople-1)
else:
    grayindex = numpeople

i = 0
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
s.bgcolor('white')
if grayGame:
    people[grayindex].t.speed('slowest')
    people[grayindex].t.goto(0,0)
    people[grayindex].t.circle(50)
adjustSpeed(people)
numcolorpeople = numColor(people, screencolor)
print(numcolorpeople)
guess = int(input('How many ' + screencolor + ' people are there?\n'))
t = Turtle()
t.penup()
t.speed(5)
gotoEach(people, screencolor, t)
if guess == numcolorpeople:
    print('You Win')
else:
    print('You Lose')

s.exitonclick()
