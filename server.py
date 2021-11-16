from flask import Flask, render_template, request, redirect, url_for
import data_manager
from datetime import datetime

app = Flask(__name__)

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
now = datetime.now()
now_timestamp = datetime.timestamp(now)

@app.route("/add-question", methods=['POST', 'GET'])
def add_question():
    questions = data_manager.get_questions()
    question = {}
    view_number = 0
    vote_number = 0
    if request.method == 'POST':
        question['id'] = data_manager.get_max_id() + 1
        question['submission_time'] = int(now_timestamp)
        question['view_number'] = view_number
        question['vote_number'] = vote_number
        question['title'] = request.form['title']
        question['message'] = request.form['message']
        question['image'] = vote_number
        questions.append(question)
        data_manager.write_questions(questions)
        return redirect('/question/<question_id>')
    return render_template('add-question.html', id=id, question=question)
#Luti


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )

