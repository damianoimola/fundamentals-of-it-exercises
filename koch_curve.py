worldWidth = 600
worldHeight = 500
w = makeWorld(worldWidth, worldHeight)
t = Turtle(w)

def koch(width, t):
# @param width : Int
# @param t : Turtle
    assert width % 3 == 0, "inserisci come lunghezza del segmento una potenza di 3"
    # 4 is the number of strokes that should be generated each parent stroke
    for step in range(0, 4):
        # turning turtle in the right direction
        if step == 1 or step == 3:
            t.turn(-60)
        elif step == 2:
            t.turn(120)
        # drawing the stroke
        if width == 3:
            t.forward(width)
            t.turn(-60)
            t.forward(width)
            t.turn(120)
            t.forward(width)
            t.turn(-60)
            t.forward(width)
        else:
            koch(width/3, t)

mainStrokeWidth = 81
t.penUp()
t.turnRight()
t.backward((worldWidth/2) - 20)
t.penDown()
t.penColor = black
koch(mainStrokeWidth, t)