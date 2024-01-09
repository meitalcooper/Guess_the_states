import turtle
import csv
import pandas

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S  States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.textinput(title="Educate Yourself" , prompt="enter all the sataes you know.\n to reveal the states you don't know enter : 'exit' \n press enter to start the game")

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

guessed_states =[]
missing_states = []


def write_state():
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)

def write_missind_state():
    t.hideturtle()
    t.penup()
    missing_state_data = data[data.state == states]
    t.goto(int(missing_state_data.x), int(missing_state_data.y))
    t.color("red")
    t.write(states, font=("Arial", 8, "normal"))
    


# Game loop to run until all 50 states are guessed 
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?:")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        for states in states_list:
            if states not in guessed_states:
                missing_states.append(states)
                write_missind_state()
        screen.exitonclick()
        
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        write_state()

# Filter the original data for missing states
missing_states_data = data[data['state'].isin(missing_states)]

# Save the missing states with their coordinates to a new CSV file
missing_states_data.to_csv("states_to_learn.csv", index=False)



        
