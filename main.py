from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['DEBUG'] = True


# images = ['grid_0.png', 'grid_1.png', 'grid_2.png', 'grid_3.png', 'grid_4.png',
#     'grid_5.png', 'grid_6.png', 'grid_7.png', 'grid_8.png']

images = ['dog.gif', 'cat.gif', 'bird.gif', 'mouse.gif', 'cow.gif',
    'frog.gif', 'elephant.gif', 'duck.gif', 'fox.gif']
    

@app.route('/', methods=['GET', 'POST'])

def show_grid():
    noises = {
    "dog":"Dog goes 'woof'",
    "cat":"Cat goes 'meow'",
    "bird":"Bird goes 'tweet'",
    "mouse":"Mouse goes 'squeak'",
    "cow":"cow goes 'moo'",
    "frog":"Frog goes 'croak'",
    "elephant":"the elephant goes 'toot'",
    "duck":"ducks say 'quack'",
    "fox":"What Does the fox say?"}
    display_noise = 'Click on an animal to find out what it says'

    if request.method == 'POST':
        
        name_value = request.form['animal_selection']
        
        print(name_value)

        display_noise = noises[name_value]


        # choice = int(request.form['choice'])    # Collect the radio button value from the form.
        # old_steps = request.form['steps']       # Retrieve the old 'steps' string from the webpage. 
        # steps = f"{old_steps}-{choice}"     # Generate a new 'steps' string.
        # image = images[choice]              # Assign a file name from the images list.
        # choices = fill_choices(choice)      # Call the fill_choices() function, which returns a dictionary of the allowed directions and values for the new box.
    
    
    animals_list = list(noises.keys())
      
    return render_template('index.html', noises = noises , animals_list=animals_list, images = images, display_noise = display_noise)

if __name__ == '__main__':
    app.run()


# Dog goes "woof"
# Cat goes "meow"
# Bird goes "tweet"
# And mouse goes "squeek"
# Cow goes "moo"
# Frog goes "croak"
# And the elephant goes "toot"
# Ducks say "quack"

# What does the fox say?
# "Ring-ding-ding-ding-dingeringeding!
# Gering-ding-ding-ding-dingeringeding!
# Gering-ding-ding-ding-dingeringeding!"
