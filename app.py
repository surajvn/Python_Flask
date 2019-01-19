from flask import Flask,render_template
from data import Faculties

app=Flask(__name__)
myFaculties=Faculties()

@app.route('/')
def index():
    # return "<h1>Hello World</h1>"
    return render_template('index.html')

@app.route('/Login')
def login():
    return "<h1> Login Page </h1>"

@app.route('/register')
def regist():
    return render_template('reg.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html',facultyList=myFaculties)


if(__name__=='__main__'):
    app.run(debug=True)
