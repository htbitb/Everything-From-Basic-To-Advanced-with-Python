import turtle 
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "Python/7. Working with Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Python/7. Working with Pandas/50_states.csv")
all_states = data.state.to_list()

# screen.exitonclick()
guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_state == 'exit':
        missing_state = []
        for state in all_states:
            if state not in guess_state:
                missing_state.append(state)
        new_df = pandas.DataFrame(missing_state)
        new_df.to_csv("missing_state.csv")
        screen.exit()
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


    
screen.exitonclick()