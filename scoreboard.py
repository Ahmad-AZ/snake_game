from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Verdana ', 20, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0,270)
        self.pencolor("white")
        self.print_score()



    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()


    def print_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):

        game_over = Turtle()
        game_over.penup()
        game_over.color("white")
        game_over.write("Game Over",  move=False, align=ALIGNMENT, font=FONT)


