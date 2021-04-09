from turtle import *

color('red', 'red') #shape colors
begin_fill() #for drawing a shape
while True:
    forward(200)
    left(170)

    if abs(pos()) <1:
        break
end_fill()
done()

