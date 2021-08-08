from turtle import Turtle


class Scoreboard(Turtle):
    """A gigantic diamond masterpiece scoreboard,
    only god knows what it took me to get it in this game."""
    def __init__(self):
        super(Scoreboard, self).__init__()
        """see that super() thing.. it's so cool.. all the credit goes to auto completion"""
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color('white')
        self.update_score_board()

    def update_score_board(self):
        """Pure magic. Don't try to understand it with your poor programmer mind"""
        self.clear()
        self.write(f'score: {self.score}', False, 'center', ('Courier', 24, 'normal'))

    def add(self):
        """Don't fuckin' dare to change the amount of added score."""
        self.score += 1
        self.update_score_board()

    def game_over(self):  # Turning into music player mode.
        """helpful tip: (like really helpful.)
        to stop the song hit 'm' as in Mutant.
        to play a new song hit 'Enter' as in Interception But with E instead of the I.
        spam 'Return' as in "Costa-Rica"[6] to piss your neighbours out.
        Hit 'm' ASSuckingP if your neighbour came to... you know..."""
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', ('Courier', 24, 'normal'))
        self.goto(0, -40)
        self.write('(press Enter to play another song!)', False, 'center', ('Courier', 15, 'normal'))
        self.goto(0, -80)
        self.write('"m" to stop it.', False, 'center', ('Courier', 15, 'normal'))


class Welcome(Turtle):
    """Like what stronghold crusader's deep voiced voice actor says sometime.
    Or in windowz welcome screen. LMFAOOAOFISJFSIDJ.. ehm.."""

    def __init__(self):
        super(Welcome, self).__init__()  # Dope.
        self.penup()
        self.hideturtle()
        self.color('white')
        self.write('tab "Enter" to play!', False, 'center', ('Courier', 18, 'normal'))

    def start_game(self):
        """It doesn't actually start anything,
        just clears the screen and waits for other functions to do the real job.
        reminds me of my future co-workers."""
        self.clear()
