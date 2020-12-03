import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=710, height=500)

turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()


states = pandas.read_csv("50_states.csv")
state_count = 0
correct_guesses = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{state_count}/50 State Correct", prompt="What's another state's name?")\
        .title()
    state_list = states.state.to_list()
    if answer_state == "Exit":
        game_is_on = False
    if answer_state in state_list:
        x_pos = int(states[states.state == answer_state].x)
        y_pos = int(states[states.state == answer_state].y)
        writer.goto(x_pos, y_pos)
        writer.write(answer_state)
        state_count += 1
        correct_guesses.append(answer_state)
    if len(correct_guesses) == len(state_list):
        game_is_on = False

left_states = list(set(state_list) - set(correct_guesses))
print(left_states)

