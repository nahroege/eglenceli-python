import turtle

########################################################################
class Kaplumbagam(turtle.Turtle):

    #----------------------------------------------------------------------
    def __init__(self):
        turtle.Turtle.__init__(self, shape="turtle")
        screen = turtle.Screen()
        screen.bgcolor("lightgrey")
        self.pensize(3)

    #----------------------------------------------------------------------
    def daireCiz(self, x, y, renk, derece=50):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.color(renk)
        self.circle(derece)

    #----------------------------------------------------------------------
    def olimpiyatSemboluCiz(self):
        positions = [(0, 0, "blue"), (-120, 0, "purple"), (60,60, "red"),
                     (-60, 60, "yellow"), (-180, 60, "green")]
        for x, y, renk in positions:
            self.daireCiz(x, y, renk)

    #----------------------------------------------------------------------

if __name__ == "__main__":
    t = Kaplumbagam()
    t.olimpiyatSemboluCiz()
    turtle.getscreen()._root.mainloop()
