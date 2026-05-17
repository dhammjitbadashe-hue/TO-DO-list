# TO-DO-list
from flask import Flask,render_template,request
import mysql.connector
app= Flask(__name__)
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="to do list"
)
cursor=db.cursor()
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit_task' ,methods=["post"])
# def submit():
#     a=request.form["task"]
#     b=request.form["priority"]
#     c=request.form["submit"]
#     return render_template ("task.html", a=a, b=b, c=c)
def submit():
    task= request.form["task"]
    priority=request.form["priority"]


    q="INSERT INTO `task`(`task`, `priority`  ) VALUES(%s,%s)"
    v=(task,priority)
    cursor.execute(q,v)
    db.commit()
    return render_template("task.html", a=task, b=priority)
app.run(debug=True)
