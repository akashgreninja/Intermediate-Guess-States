import turtle
from turtle import Turtle,Screen
import pandas


screen=Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491,width=725)


turtle.shape(image)

the_csv=pandas.read_csv("50_states.csv")
states=the_csv.state.to_list()

# print(x)

gussed_states=[]
while len(gussed_states) <50:
    answer_state=screen.textinput(title=f"{len(gussed_states)}/50 States Correct ",
                                  prompt="Whats the next state ").title()
    print(answer_state)


    if answer_state =="Exit":
        missing_states=[]
        for i in states:
            if i != gussed_states:
                missing_states.append(i)
        print(missing_states)
        new_data=pandas.DataFrame(missing_states).to_csv("rem_states.csv")
        # new_data.to_csv("states.csv")
        break


    if  answer_state in states:
        gussed_states.append(answer_state)
        # x=the_csv.x
        # y=the_csv.y
        # turtle.goto(x,y)
        turtle=Turtle()
        turtle.penup()
        turtle.hideturtle()
        # t.color("black")

        coordinates=the_csv[the_csv.state == answer_state]
        turtle.goto(int(coordinates.x), int(coordinates.y))

        turtle.write(answer_state)







# screen.exitonclick()



