import pyodbc
from flask import Flask
# Connect to the SQL Server
app=Flask(__name__)
conn = pyodbc.connect("Driver={SQL Server};Server=DESKTOP-37PHUQ7\SQLEXPRESS;Database=students")

@app.route('/display_pdf/<int:pdf_id>')
def display_pdf(pdf_id):
    # Prepare the SQL query to retrieve the PDF file based on the ID
    query = "SELECT pdf_file FROM your_table WHERE Phone_Number = ?"

    # Execute the query and fetch the result
    cursor = conn.cursor()
    cursor.execute(query, (pdf_id,))
    result = cursor.fetchone()

    # Return the PDF file data as a response
    return result.Resume


if __name__=='__main__':
    app.run(debug=True)