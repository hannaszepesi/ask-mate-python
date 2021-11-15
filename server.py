from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route("/")
def hello():
    question_list = data_manager.get_questions()
    return render_template("list.html", questions = question_list)



#Hanna
#Hanna
#Berni
#new answer / post an answer
@app.route('/question/<question_id>/new-answer', methods = ['GET', 'POST'])
def new_answer():
    return render_template("new_answer.html")
#Berni
#Vero
#Vero
#Luti
#Luti

if __name__ == "__main__":
    app.run()
