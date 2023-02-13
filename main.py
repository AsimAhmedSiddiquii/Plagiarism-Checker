from flask import Flask, render_template, request, redirect, session
from forms import PlagForm
import Requests_ex
import math
app = Flask(__name__)

app.config['SECRET_KEY'] = '827e763e55e41e32381c13afc4338d5f'

get_text = []
@app.route('/', methods=['POST', 'GET'])
def index():
    form = PlagForm()
    if form.validate_on_submit():
        text = form.checkText.data
        print(text)
        get_text.clear()
        get_text.append(text)
        return redirect('/results')
    return render_template('index.html', form=form)

@app.route('/results')
def results():
    ans = Requests_ex.main_function(get_text[0])
    sentences = Requests_ex.tokenize_sentence(get_text[0])
    avg_len = sum(len(x.split()) for x in sentences) / len(sentences)
    words = get_text[0].split()

    reading = (len(words) / 200) * 10
    speaking = (len(words) / 140) * 10

    average = sum(len(word) for word in words) / len(words)
    return render_template('results.html', output=ans, no_of_words=len(words), sentences=len(sentences), average=int(average), avg_len=int(avg_len), reading=math.ceil(reading), speaking=math.ceil(speaking))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
    