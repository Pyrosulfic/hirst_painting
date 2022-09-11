from random import randint
from turtle import Turtle, Screen, colormode
winner=""
game_on = False
colormode(255)
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
for i in range(6):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=-125 + 50 * i)

if user_bet:
    game_on = True

while game_on:
    for item in turtles:
        item.forward(randint(0, 10))
        item.clear()
        item.write((0,0))
        if item.xcor() >= 250:
            game_on = False
            winner = turtles.index(item)

if winner == colors.index(user_bet):
    print(f"Correct!. {user_bet.upper()} is the winner!")
else:
    print(f"Nice try, but {colors[winner].upper()} is the winner!")
screen.exitonclick()
