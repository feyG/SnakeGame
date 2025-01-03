import turtle
import time
import random

speed=0.15
#Window settings
window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("lightgreen")
window.setup(width=600,height=600)
window.tracer(0)

#Snake's head

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)  #(0,0)
head.direction="stop"

#Eat

eat=turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("blue")
eat.penup()
eat.goto(0, 0)  
eat.shapesize(0.80,0.80)


tails=[]

puan=0

write=turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("white")
write.penup()
write.goto(0, 260)
write.hideturtle()
write.write('Puan: {}'.format(puan),align='center',font=('Courier',24,'normal'))



#Movement

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

def goUp():
    if head.direction !='down':
        head.direction='up'

def goDown():
    if head.direction !='up':
        head.direction='down'

def goRight():
    if head.direction !='left':
        head.direction='right'
        
def goLeft():
    if head.direction !='right':
        head.direction='left'

window.listen()
window.onkey(goUp,'Up')
window.onkey(goDown,'Down')
window.onkey(goRight,'Right')
window.onkey(goLeft,'Left')


while True:
    window.update()
    
    if head.xcor() > 300 or head.xcor()< -300 or head.ycor() >300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction='stop'
        
        for tail in tails:
            tail.goto(1000,1000)
            
        tails=[]
        puan=0
        write.clear()
        write.write('Puan: {}'.format(puan),align='center',font=('Courier',24,'normal'))
        
        speed=0.15
    
    if head.distance(eat)<20:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        eat.goto(x,y)
        
        puan=puan+10
        write.clear()
        write.write('Puan: {}'.format(puan),align='center',font=('Courier',24,'normal'))
        speed=speed-0.001
        
        
        newtail=turtle.Turtle()
        newtail.speed(0)
        newtail.shape('square')
        newtail.color('purple')
        newtail.penup()
        tails.append(newtail)
        
    for i in range(len(tails)-1,0,-1):
        x=tails[i-1].xcor()
        y=tails[i-1].ycor()
        tails[i].goto(x,y)
    
    if len(tails)>0:
        x=head.xcor()
        y=head.ycor()
        tails[0].goto(x,y)
        
        
    move()
    time.sleep(speed)
    

