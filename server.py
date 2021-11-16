from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)


@app.route("/")
def hello():
    question_list = data_manager.get_questions()
    return render_template("list.html", questions = question_list)



#Hanna
@app.route("/list")
def list_questions():
    questions = data_manager.get_questions()
    question_dict = {}
    for question in questions:
        question_dict[question['title']] = question['id']
    sorted_question_dict = dict(sorted(question_dict.items(), key=lambda item: item[1]))
    return render_template('list.html', questions=sorted_question_dict)
#Hanna
#Berni
#Berni
#Vero
#Vero
#Luti
#Luti

if __name__ == "__main__":
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )

