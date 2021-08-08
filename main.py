from scoreboard import Scoreboard, Welcome  # mOm!!! i nKoW oOp!!!!
from turtle import Screen
from snake import Snake
from food import Food
import platform
import random
import time
import os
''' The game requires you to have sox and tk installed on your linux machine,
for windows you may need tk if it's not there .. you won't need sox.
sudo apt install sox tk : ubuntu/debian
sudo pacman -S sox tk : arch'''
# 2030 awardee of world's most entertaining game ever made.
# Been accused 'cause of being heavily reliant on GPU resources.. as it used to consume 7GB of vRAM.
# But CEO and Founder of the game Assem Mohammed aka @zaSavior aka @zaHijacker announced>
# a shocking update note saying "We've solved the issue and the game now only needs 6.9GB"!!!
# "he gotta be kidding tho.. OMG if he isn't, then I'mma kill myself", news reporter.

opsys = platform.system()
windowz = 'Windows'
if opsys == windowz:  # Best OS.
    import winsound

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SnAdele')  # cREaTiviTy
screen.listen()

snake = Snake()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
score = Scoreboard()
food = Food()
alive = True


def game_switch():
    """It's like a ba-on To tan on the game. a bre-ish ba-on."""
    play_song()
    welcome.clear()
    global alive
    while alive:  # Curse your life.
        screen.update()
        time.sleep(0.08)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.add()
        # detect collision with the wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            # the above line is a one-time code. You write it.. And never try to read at it again.
            alive = False  # RIP
            score.game_over()
            stop_song()

        for segment in snake.segments[1:]:  # Mom!!!! I know slIC    iNg!!!!
            if snake.head.distance(segment) < 10:
                alive = False  # Just fucking die, mate!
                score.game_over()
                stop_song()
                

def play_song():
    """Pire-ed songs."""
    random_first_digit = str(random.randint(0, 1))
    random_second_digit = str(random.randint(0, 9))
    random_number = int(random_first_digit + random_second_digit)
    # and just like that we've got a number from 01 to 19.
    # f"{Science} bitch!"  # Science = "Math"

    if opsys == windowz:  # You be-ir install linux... Just saying.
        winsound.PlaySound(f'Adele\\{random_number}*', winsound.SND_ASYNC)
    else:
        os.system(f'play Adele/{random_number}* &')
    print(random_number)


def stop_song():
    """Doesn't matter... Adele will sue you either way."""
    if opsys == windowz:  # For real tho, just install the damn thing!
        winsound.PlaySound(None, winsound.SND_PURGE)
    else:
        os.system('killall play')


welcome = Welcome()
screen.onkey(game_switch, 'Return')
screen.onkey(stop_song, 'm')
screen.exitonclick()
