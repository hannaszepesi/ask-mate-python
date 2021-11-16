from flask import Flask, render_template, request, redirect, url_for
import data_manager
from datetime import datetime

app = Flask(__name__)

#Hanna
@app.route("/list")
@app.route("/")
def list_questions():
    questions = data_manager.get_questions()
    question_dict = {}
    for question in questions:
        question_dict[question['title']] = question['id']
    sorted_question_dict = dict(sorted(question_dict.items(), key=lambda item: item[1]))
    return render_template('list.html', questions=sorted_question_dict)
#Hanna
#Berni
#new answer / post an answer
@app.route('/question/<question_id>/new-answer', methods = ['GET', 'POST'])
def new_answer(question_id):
    from datetime import datetime
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    if request.method == "POST":
        new_answer = {
            "id": data_manager.get_max_id()+1, #A unique identifier for the answer.
            "submission_time":int(now_timestamp), #floatot ad ki alapból, The UNIX timestamp when the answer is posted.
            "vote_number":str(0), #The sum of votes the answer receives.
            "question_id": 15,#Ide majd az az ID kell, ami ami a View Questionből jön, Verótól
            "message": request.form.get("message"), #The answer text.
            "image":request.form.get("image") #The path to the image for this answer.
            }
        data_manager.write_answers(new_answer)
        return redirect("/question/"+str(question_id))
    return render_template("new_answer.html", question_id = question_id)


#Berni
#Vero
@app.route("/question/<question_id>")
def display_question(question_id):
    questions = data_manager.get_questions()
    for question in questions:
        if question['id'] == question_id:
            title = question['title']
            message = question ['message']
    list_of_answers = data_manager.get_answers()  #cserélve lesz!
    answers=[]
    for answer in list_of_answers:
        if answer['question_id'] == question_id:
            answers.append(answer['message'])
    return render_template("display_question.html", title=title, message=message, answers=answers, question_id = question_id)
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

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )