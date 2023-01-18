import turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("US States Naming Game")
screen.setup(725, 491)

# Setting up the background
background = "us-states-game/blank_states_img.gif"
screen.addshape("us-states-game/blank_states_img.gif")
turtle.shape(background)



screen.exitonclick()