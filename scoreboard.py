from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Verdana ', 20, 'bold')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_data()
        self.hideturtle()
        self.goto(0,270)
        self.pencolor("white")
        self.print_score()
        self.read_data()



    def increase_score(self):
        self.score += 1
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}     High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_data()
        self.score = 0
        self.print_score()


    def read_data(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())


    # def game_over(self):
    #
    #     game_over = Turtle()
    #     game_over.penup()
    #     game_over.color("white")
    #     game_over.write("Game Over",  move=False, align=ALIGNMENT, font=FONT)


    def write_data(self):
        with open("data.txt", mode = "w") as file:
            file.write(f"{self.high_score}")





