from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import Query, Entry
import markovify
import pickle

def generate(count, name):
    with open("mylist", "rb") as input_file:
        lst = pickle.load(input_file)

    text_model = markovify.NewlineText(lst, state_size = 2)

    generated = []

    
    for i in range(count):
        newSentence = text_model.make_sentence()

        print('name not empty', name != '')
        print('newSentence is not None', newSentence is not None)


        if (name != '') and (newSentence is not None) and ('CustomerName' in newSentence):
            newSentence = newSentence.replace('CustomerName', name)
            generated.append(newSentence)
        elif newSentence is not None:
            generated.append(newSentence)
            

    print('done')
    return generated

pswd = 'rps2020'

results = ''

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def entry():
    form = Entry()
    if form.validate_on_submit(): 

        if form.pswd.data == pswd:

            return redirect(url_for('index'))
        else:
            flash('Invalid login')
    return render_template('entry.html',form=form)

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Query()
    if form.validate_on_submit():
        global results
        print('customer asdf name:', form.customerName.data)
        results = generate(form.headlines.data, form.customerName.data)
        
        return redirect(url_for('result'))
    return render_template('index.html', form=form)

@app.route('/result')
def result():
    return render_template('result.html', resultCount=len(results), results=results)





if __name__ == '__main__': app.run(debug=True)