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

colors = ['red', 'orange', 'yellow', 'dark green', 'blue', 'purple', 'black']
s = Screen()
s.screensize()
s.setup(width = 1.0, height = 1.0)
screenheight = s.window_height()
screenwidth = s.window_width()
'''s.setup(1500, 800)
s.bgcolor('black')
rules = Turtle()
writeAt(rules, 'People in a City', 0, 0, 'white', 30, 'center')
time.sleep(5)
rules.clear()
writeAtB(rules, 'You have 10 seconds to observe the crowd.', -480, 150, 'white', 16)
writeAtB(rules, 'Your score is the absolute value of the different between your guess and the actual amount.', -480, 120, 'white', 16)
writeAtB(rules, 'Smaller score = better.', -480, 90, 'white', 16)
writeAtB(rules, 'You have 2 seconds to type your answer on the screen.', -480, 60, 'white', 16)
writeAtB(rules, 'Press enter to submit. Press delete to clear your response, backspace just for 1 character.', -480, 30, 'white', 16)
writeAtB(rules, 'Good luck! Have fun.', -480, 0, 'white', 20)
time.sleep(10)
rules.clear()'''
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
print(numcolorpeople)
timer = Turtle()
timer.hideturtle()
timer.penup()
countdown(timer, 10, time)
s.bgcolor(screencolor)
guess = s.numinput(screencolor + ' people', "How many " + screencolor + " people are there?", default=0, minval=0, maxval=numpeople)
score = abs(guess - numcolorpeople)
scorewriter = Turtle()
scorewriter.hideturtle()
scorewriter.penup()
print('Height: ', s.window_height())
print('Width: ', s.window_width())
writeAtB(scorewriter, 'Score:', -1*screenwidth/2 +100, screenheight/2-100, 'black', 50)
t = Turtle()
t.hideturtle()
t.penup()
s.bgcolor('white')
writeAtB(scorewriter, 'Guess:', screenwidth/2 - 350, screenheight/2-100, 'black', 50)
writeAtB(scorewriter, int(guess), screenwidth/2 - 200, screenheight/2-250, 'black', 50)
gotoEach(people, screencolor, t)
writeAtB(scorewriter, int(score), -1*screenwidth/2 +200, screenheight/2-250, 'black', 50)
'''questionWriter = Turtle()
questionWriter.hideturtle()
questionWriter.penup()
writeAt(questionWriter, 'How many ' + screencolor + ' people are there?', 0, 340, 'black', 24, 'center')
digitsEntered = []
t1 = Turtle()
t1.hideturtle()
t1.penup()
t1.goto(500, 0)
timer = Turtle()
timer.hideturtle()
timer.penup()
def countdown(t, seconds, time):
    t.goto(-300,280)
    for i in range(seconds, -1, -1):
        t.color('black')
        style = ('Courier', 20, 'bold')
        t.write(str(i), font=style, align='center')
        time.sleep(1)
        t.clear()
def show0():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('0', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(0)
def show1():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('1', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(1)
def show2():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('2', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(2)
def show3():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('3', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(3)
def show4():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('4', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(4)
def show5():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('5', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(5)
def show6():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('6', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(6)
def show7():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('7', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(7)
def show8():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('8', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(8)
def show9():
    global digitsEntered
    style = ('Courier', 18, 'bold')
    t1.write('9', font=style, align='center')
    t1.forward(15)
    digitsEntered.append(9)
def backspace():
    global digitsEntered
    t1.clear()
    digitsEntered = digitsEntered[0:-1]
    writeDigits(t1, digitsEntered)
t = Turtle()
t.hideturtle()
t.penup()
def revealanswer():
    global screencolor, t, people, questionWriter
    t1.clear()
    questionWriter.clear()
    gotoEach(people, screencolor, t)
    s.bye()
def cleanup():
    global digitsEntered
    t1.clear()
    t1.goto(500, 0)
    digitsEntered.clear()
#s.onkey(up, 'Up')
#countdown(timer, 10, time)
s.onkeyrelease(lambda: cleanup(), 'Delete')
s.onkeyrelease(lambda: backspace(), 'BackSpace')
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
s.onkeyrelease(lambda: revealanswer(), 'Return')
s.listen()
s.exitonclick()
answer = listToNum(digitsEntered)
print(answer)'''
s.exitonclick()