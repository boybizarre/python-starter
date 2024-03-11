import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# print(data)
while len(guessed_states) < 50:
    answer_state = turtle.textinput(
        title=f"{len(guessed_states)}/50 States correct",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # t.write(state_data.state.item())


# print(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.exitonclick()
# turtle.mainloop()
