from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'ThisIsSecret'
import random

@app.route('/')
def index():
    if 'randNum' in session:
        session['randNum'] = session['randNum']
    else:
        session['randNum'] = random.randrange(0, 101)
    if 'guessNum' in session:
        session['guessNum'] = session['guessNum']
    else:
        session['guessNum'] = 0
    randNum = int(session['randNum'])
    guessNum = int(session['guessNum'])
    return render_template("index.html", randNum=randNum, guessNum=guessNum)

@app.route('/guess', methods=['POST'])
def guess():
    session['guessNum'] = request.form['guess']
    return redirect('/')

@app.route('/play_again', methods=['POST'])
def play_again():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

