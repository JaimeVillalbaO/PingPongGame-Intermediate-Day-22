from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()
        
       
    def update_scoreboard(self):
        self.goto(-100, 180)
        self.write(self.lscore, align = 'center', font= ('courier', 80, 'normal') )
        self.goto(100, 180)
        self.write(self.rscore, align = 'center', font= ('courier', 80, 'normal') )


    
    def l_point(self):
        self.lscore += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.rscore += 1
        self.clear()
        self.update_scoreboard()