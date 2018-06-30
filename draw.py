import turtle
import random

t = turtle.Turtle()
t.reset()
t.speed(0)
t.penup()

colors=['red', 'blue', 'purple', 'green', 'orange', 'light blue', 'pink', 'light green']

screen = turtle.Screen()

# t.hideturtle()
def print_mouse_location(x,y):
  t.goto(x,y)
  t.dot(10, random.choice(colors))



t.ondrag(print_mouse_location)
screen.onclick(print_mouse_location)  
  
