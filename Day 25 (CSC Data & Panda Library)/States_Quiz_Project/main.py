import turtle
import pandas
from show_state import show_answer

#write the correct guesses onto the map


# Getting Data
data = pandas.read_csv('50_states.csv')
state_dict = data.to_dict()
print(state_dict)
state_list = data['state'].to_list()
print(state_list)

# Setting Up Screen
screen = turtle.Screen()
screen.title('U.S States Game')

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

scribe = show_answer()

#Setting up Score
score = 0
guesses = []

# Program Running
game_running = True
while game_running:
    
    answer_state = screen.textinput(title = "Guess the State", prompt= "What's another state's name?").title()
    print(answer_state)

    for state in state_list:
        if answer_state == state:
            score += 1
            state_data = data[data['state'] == answer_state]
            guesses.append(answer_state)
            print(guesses)
            scribe.write_answer(x=int(state_data['x']),y = int(state_data['y']), state = answer_state)
        elif answer_state == 'Exit':
            game_running
        
        if score == 50:
            game_running = False
        


screen.mainloop()

