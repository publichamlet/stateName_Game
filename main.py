#!/usr/bin/env python3

import sys, os
from tkinter import TclError
import turtle

if sys.platform == 'linux':
    if os.getcwd() != os.path.dirname(__file__):
        os.chdir(os.path.dirname(__file__))

turtle.setup(941, 836, startx=100, starty=1)
turtle.bgpic('rsz_india.gif')

screen = turtle.Screen()
screen.title('Indian States Game')
t = turtle.Turtle()
t.hideturtle()
t.penup()

states = ['Kerala', 'Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Goa', 'Maharashtra', 'Chhattisgarh', 'Odisha', 'Gujarat', 'Madhya Pradesh', 'Jharkhand', 'West Bengal', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 'Sikkim', 'Assam', 'Arunachal Pradesh', 'Nagaland', 'Manipur', 'Mizoram', 'Tripura', 'Meghalaya', 'Delhi', 'Haryana', 'Punjab', 'Himachal Pradesh', 'Uttarakhand', 'Jammu & Kashmir(UT)']


with open('data.csv', 'r') as file_r:
    data = file_r.read().split('\n')
data = data[1:]

try:
    count = 0
    while True:
        name = screen.textinput(title=f'{count}/29 States', prompt='Enter the State')
        for item in data:
            state, x, y = item.split(',')
            if name.lower() == 'delhi':
                continue
            elif name.lower() == state.lower():
                t.goto(float(x), float(y))
                t.write(state, font=('Calibri', 14, 'bold'))
                count += 1
            elif count == 29:
                break
            else:
                continue
except TclError:
    print(TclError)

except AttributeError:
    t.clear()
    for item in data:
        state, x, y = item.split(',')
        if state.lower() == 'delhi':
            continue
        x, y = float(x), float(y)
        t.goto(x, y)
        t.write(state, font=('Calibri', 12, 'bold'))


screen.mainloop()




    

# screen.onscreenclick(goto)
# screen.onclick(write_)






""" Code to identify the points of turtle screen and store in a file """
# def goto(x,y):
#     with open('state_list.txt', 'a') as file_w:
#         file_w.write(f'({x}, {y})\n')
#     print(x, y)
# screen.onscreenclick(goto)
# screen.mainloop()

""" Code to generate the data.csv file """
# with open('state_list.txt', 'r') as file_r:
#     # print(file_r.read().split('\n')[0].split(', '))
#     lt = file_r.read().split('\n')

# lp = (len(states))

# for i in range(len(states)):
#     x, y = [float(x) for x in lt[i].split(', ')]
#     if i == 0:
#         with open('data.csv', 'w') as file_w:
#             file_w.write('state,X-axis,Y-axis\n')
#             file_w.write(f'{states[i]},{x},{y}\n')
#     else:
#         with open('data.csv', 'a') as file_w:
#             file_w.write(f'{states[i]},{x},{y}\n')


