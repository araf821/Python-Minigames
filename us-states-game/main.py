import turtle
import pandas

# Setting up the screen
screen = turtle.Screen()
screen.title("US States Naming Game")
screen.setup(725, 491)

# Setting up the background
background = "us-states-game/blank_states_img.gif"
screen.bgpic(background)

# Adjusting the turtle
turtle.pu()
turtle.ht()

# Bringing in our data
states_data = pandas.read_csv("us-states-game/50_states.csv")
all_states = states_data.state.to_list()

# Prompting the user
states_guessed = 0
already_guessed = []
while states_guessed < 50:
    answer = screen.textinput(f"{states_guessed}/50 States Named", "Name a state!").title()
    if answer == "Exit" or "Quit":
        break
    if answer not in already_guessed:
        if answer in all_states:
            state = states_data[states_data.state == answer]
            state_x = state.x
            state_y = state.y
            turtle.goto(state.x.values[0], state.y.values[0])
            turtle.write(arg=answer, align="center", font=("Courier", 8, "normal"))
            already_guessed.append(answer)
            states_guessed += 1

# When all states have been guessed
if states_guessed == 50:
    turtle.goto(0, 0)
    turtle.write(arg="Game Over!", align="center", font=("Courier", 60, "bold"))
    turtle.goto(0, -23)
    turtle.write(arg="You know...everything?!", align="center", font=("Courier", 30, "bold"))
