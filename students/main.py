### integrate html with Flask
### HTTP verb GET and POST

##  Jinja2 template engine
'''
{%....%} conditions, for loops
{{ }} to print output
{#...#} for comments
'''



from flask import Flask, redirect, url_for,render_template, request, send_file
import pyodbc
import pandas as pd
import os
import json
from io import BytesIO
from werkzeug.utils import secure_filename


app=Flask(__name__)

connection=pyodbc.connect("Driver={SQL Server};Server=DESKTOP-37PHUQ7\SQLEXPRESS;Database=students")

@app.route('/', methods=['POST','GET'])
def welcome():
    if request.method=='POST':
        while(True):
                full_name = request.form['full_name']
                Email = request.form['Email']
                Phone_number = request.form['Phone_number']
                Password = request.form['Password']
                course = request.form['course']
                resume = request.files['resume']
                file=resume.filename
                pdf_file=resume.read()
                if  file:
                    # with open('details.txt', 'a') as f:
                    #     f.write(str({'name':full_name, 'email':Email, 'phone_number':Phone_number, 'password':Password, 'course':course,'resume':resume})+'\n')
                    #     f.close()
                    # data={'name':full_name, 'email':Email, 'phone_number':Phone_number, 'password':Password, 'course':course}
                    # file_details=json.dump(data)
                    cursor=connection.cursor()
                    cursor.execute('INSERT INTO students_details(Name, Email,Phone_Number,Password,course,Resume) Values(?,?,?,?,?,?)',(full_name,Email,Phone_number,Password,course,pdf_file))
                    connection.commit()
                    
                    data={
                         'name':full_name,
                          'email':Email,
                          'phone_number':Phone_number,
                          'password':Password,
                          'course':course
                        }
                    json_data=[]
                    try:
                        with open('details.json', 'r') as json_file:
                            json_data = json.load(json_file)
                    except FileNotFoundError:
                        pass
                    json_data.append(data)
                    with open('details.json','w') as json_file:
                         json.dump(json_data,json_file,indent=5)
                        #  json_file.write(file_details)
                    resume.save(os.path.join('C:/Users/Noel/Flask/students/resume',file))
                    return render_template('thank_you.html')    
                else:
                    continue
    return render_template('form.html')

@app.route('/view')
def view():
    # with open('details.txt') as file:
    #     content=file.read()
    # df = pd.read_json("details.json")
    # temp = df.to_dict('records')
    # columnNames = df.columns.values
    # return render_template('view.html', records=temp, colnames=columnNames)

    cursor=connection.cursor()
    cursor.execute("SELECT * FROM students_details")
    data_results = cursor.fetchall()

    return render_template('view.html', data_results=data_results)


@app.route('/display/<int:pdf_id>', methods=['POST','GET'])
def display(pdf_id):
    query = "SELECT * FROM students_details WHERE Phone_Number = ?"

    cursor=connection.cursor()
    cursor.execute(query,(pdf_id))
    result= cursor.fetchone()
    pdf_data = BytesIO(result.Resume)

    return send_file(pdf_data, mimetype='application/pdf')
    

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