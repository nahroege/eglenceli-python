5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

from turtle import Turtle
t=Turtle()

def up():
    if not(t.heading() == 90):
        t.setheading(90)
        t.fd(50)
    else:
        t.fd(50)

def down():
    if not(t.heading() == 270):
        t.setheading(270)
        t.fd(50)
    else:
        t.fd(50)

def right():
    if not (t.heading() == 0):
        t.setheading(0)
        t.fd(50)
    else:
        t.fd(50)

def left():
    if not (t.heading() ==180):
        t.setheading(180)
        t.fd(50)
    else:
        t.fd(50)

def undo_button():
    t.undo()

def keyboard_commands():
    t.screen.onkey(up,"Up")
    t.screen.onkey(down,"Down")
    t.screen.onkey(right,"Right")
    t.screen.onkey(left,"Left")
    t.screen.onkey(undo_button,"End")
    t.screen.listen()

keyboard_commands()
t.screen.mainloop()
