import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game")
wn.screensize(600, 400)
wn.bgcolor("green")
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.goto(0, 0)
head.penup()
head.direction = "stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.penup()
food.shape("circle")
food.color("red")
food.goto(0, 100)
food.penup()

#Functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"
def move(speed):
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)
#Keyboeard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

segments = []

#Main Game Loop
while True:
    wn.update()
    #Collision with Foood
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.goto(0, 0)
        new_segment.penup()
        segments.append(new_segment)

    #Move the end segments in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    time.sleep(delay)
    move(20)

wn.mainloop()