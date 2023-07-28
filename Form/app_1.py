### Building URL Dynamically

from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my youtube channel'

@app.route('/success/<int:score>')
def success(score):
    return '<html><body><h1>The person has passed and the score is '+str(score)+'</h1></body></html>'

@app.route('/fail/<int:score>')
def fail(score):
    return '<html><body><h1>The person has failed and the score is '+str(score)+'</h1></body><html>'

# Result checker
@app.route('/results/<int:marks>')
def result(marks):
    if marks<50:
        result='fail'

    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)