from flask import Flask
### WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to My Web Page. Building advance ML & DL Models.'

@app.route('/tests')
def tests():
    return 'First test model building'



if __name__=='__main__':
    app.run(debug=True)