from turtle import *
from colorsys import *
speed(40)
bgcolor("black")
h = 0
#Dibujar el tallo verde del girasol
penup()
goto(-35, -80)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(20)
end_fill()

#Dibujar el girasol
penup()
goto(0,0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)
#Colorear el centro de marrón
penup()
goto(-0, 15)
pendown()
color("brown")
begin_fill()
circle(44)
end_fill()
done()
