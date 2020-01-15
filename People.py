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
    

numpeople = 100
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
def displayQuestion(t, color):
    t.goto(0,10)
    t.color('black')
    style = ('Courier', 24, 'bold', 'italic')
    displaystr = 'How many ' + color + ' people are there?'
    t.write(displaystr, font=style, align='center')
print(numcolorpeople)
questionWriter = Turtle()
questionWriter.penup()
questionWriter.hideturtle()
displayQuestion(questionWriter, screencolor)
t1 = Turtle()
t1.hideturtle()
t1.penup()
t1.goto(-100, -50)
def show0():
    style = ('Courier', 18, 'bold')
    t1.write('0', font=style, align='center')
    t1.forward(15)
def show1():
    style = ('Courier', 18, 'bold')
    t1.write('1', font=style, align='center')
    t1.forward(15)
def show2():
    style = ('Courier', 18, 'bold')
    t1.write('2', font=style, align='center')
    t1.forward(15)
def show3():
    style = ('Courier', 18, 'bold')
    t1.write('3', font=style, align='center')
    t1.forward(15)
def show4():
    style = ('Courier', 18, 'bold')
    t1.write('4', font=style, align='center')
    t1.forward(15)
def show5():
    style = ('Courier', 18, 'bold')
    t1.write('5', font=style, align='center')
    t1.forward(15)
def show6():
    style = ('Courier', 18, 'bold')
    t1.write('6', font=style, align='center')
    t1.forward(15)
def show7():
    style = ('Courier', 18, 'bold')
    t1.write('7', font=style, align='center')
    t1.forward(15)
def show8():
    style = ('Courier', 18, 'bold')
    t1.write('8', font=style, align='center')
    t1.forward(15)
def show9():
    style = ('Courier', 18, 'bold')
    t1.write('9', font=style, align='center')
    t1.forward(15)
t = Turtle()
t.penup()
t.hideturtle()
def revealanswer():
    global people, screencolor, t
    gotoEach(people, screencolor, t)
def cleanup():
    t1.clear()
    t1.goto(-100, -50)
#s.onkey(up, 'Up')
s.onkeyrelease(lambda: cleanup(), 'Delete')
s.onkeyrelease(lambda: revealanswer(), 'KP_Enter')
s.onkeyrelease(lambda: show0(), '0')
s.onkeyrelease(lambda: show1(), '1')
s.onkeyrelease(lambda: show2(), '2')
s.onkeyrelease(lambda: show3(), '3')
s.onkeyrelease(lambda: show4(), '4')
s.onkeyrelease(lambda: show5(), '5')
s.onkeyrelease(lambda: show6(), '6')
s.onkeyrelease(lambda: show7(), '7')
s.onkeyrelease(lambda: show8(), '8')
s.onkeyrelease(lambda: show9(), '9')
s.listen()
'''if guess == numcolorpeople:
    print('You Win')
else:
    print('You Lose')'''

s.exitonclick()
