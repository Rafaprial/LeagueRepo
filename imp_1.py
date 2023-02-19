import pyautogui
import math
import keyboard
import sys
from random import randint
import time
#
#
# R = 400
#
# (x,y) = pyautogui.size()
#
# (X,Y) = pyautogui.position(x/2,y/2)
#
# pyautogui.moveTo(X+R,Y)

# for i in range(360):

#
#         if i%6==0:
#             pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
import random
import turtle


# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX)
# print(currentMouseY)

R = 100
# turtle.colormode(255)
(x,y) = pyautogui.size()

(X,Y) = pyautogui.position(x/2,y/2)

pyautogui.moveTo(X+R,Y)
# def isInScreen(w,t):
#     leftBound = - w.window_width()
#     rightBound = w.window_width()
#     topBound = w.window_height()
#     bottomBound = -w.window_height()
#
#     turtleX = t.xcor()
#     turtleY = t.ycor()
#
#     stillIn = True
#     if turtleX > rightBound or turtleX < leftBound:
#         stillIn = False
#     if turtleY > topBound or turtleY < bottomBound:
#         stillIn = False
#
#     return stillIn
#
# t = turtle.Turtle()
# wn = turtle.Screen()
#
# t.shape('turtle')
# while isInScreen(wn,t):



with pyautogui.hold('win'):
    pyautogui.press('2')
    pyautogui.press('up')

time.sleep(1)
pyautogui.click(279, 171)
time.sleep(3)
while True:
    for i in range(360):
        if i%6==0:
            pyautogui.dragTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
            if(keyboard.is_pressed('Esc')):
                sys.exit(0)
#     coin = random.randrange(0, 2)
#     if coin == 0:
#     t.left(90)
#     # else:
#     #     t.right(90)
#     t.color(randint(0, 255),randint(0, 255),randint(0, 255))
#     t.forward(50)

# wn.exitonclick()

