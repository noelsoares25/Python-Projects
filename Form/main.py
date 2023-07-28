### integrate html with Flask
### HTTP verb GET and POST

##  Jinja2 template engine
'''
{%....%} conditions, for loops
{{ }} to print output
{#...#} for comments
'''



from flask import Flask, redirect, url_for,render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='Pass'
    else:
        res='Fail'
    exp={'score':score, 'res':res}
    return render_template('result.html',result=exp)

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

### Result checker submit html page
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience)/4

    return redirect(url_for("success",score=total_score))

if __name__=='__main__':
    app.run(debug=True)