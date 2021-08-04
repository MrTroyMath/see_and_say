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
    if request.method == 'POST':
        pass
    else:
        noises = {
        "dog":"Dog goes 'woof'",
        "cat":"Cat goes 'meow'",
        "bird":"Bird goes 'woof'",
        "mouse":"Mouse goes 'squeak'",
        "cow":"cow goes 'moo'",
        "frog":"Frog goes 'croak'",
        "elephant":"the elephant goes 'toot'",
        "duck":"ducks say 'quack'",
        "fox":"What Does the fox say?"}
        animals_list = list(noises.keys())
      
    return render_template('index.html', noises = noises , animals_list=animals_list, images = images)

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
