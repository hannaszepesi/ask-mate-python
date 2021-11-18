from flask import Flask, render_template, request, redirect, url_for
import data_manager
from datetime import datetime

app = Flask(__name__)
like_button = '/home/luti/codecool/Web/Projects/ask-mate/like.jpeg'


# Hanna
@app.route("/list")
@app.route("/")
def list_questions():
    questions = data_manager.get_data(data_manager.QUESTION_PATH)
    question_dict = {}
    SORTING_OPTIONS = data_manager.SORTING_OPTIONS
    for question in questions:
        question_dict[question['title']] = question['id']
    sorted_question_dict = dict(sorted(question_dict.items(), key=lambda item: item[1]))
    return render_template('list.html', questions=sorted_question_dict, like=like_button, sorting=SORTING_OPTIONS)


# Hanna
# Berni
# new answer / post an answer
@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def new_answer(question_id):
    answers = data_manager.get_data(data_manager.ANSWER_PATH)
    from datetime import datetime
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    if request.method == "POST":
        new_answer = {
            "id": data_manager.get_max_id(data_manager.ANSWER_PATH) + 1,  # A unique identifier for the answer.
            "submission_time": int(now_timestamp),
            # floatot ad ki alapból, The UNIX timestamp when the answer is posted.
            "vote_number": str(0),  # The sum of votes the answer receives.
            "question_id": question_id,  # Ide majd az az ID kell, ami ami a View Questionből jön, Verótól
            "message": request.form.get("message"),  # The answer text.
            "image": request.form.get("image")  # The path to the image for this answer.
        }
        answers.append(new_answer)
        data_manager.write_data(answers, data_manager.ANSWER_PATH, data_manager.ANSWER_HEADER)
        return redirect("/question/" + str(question_id))
    return render_template("new_answer.html", question_id=question_id)


@app.route('/answer/<answer_id>/delete')
def delete_an_answer(answer_id, data_header):
    data_manager.delete_an_answer(answer_id)
    return redirect("/question/<question_id>")


# Berni
# Vero
@app.route("/question/<question_id>")
def display_question(question_id):
    questions = data_manager.get_data(data_manager.QUESTION_PATH)
    for question in questions:
        if question['id'] == question_id:
            title = question['title']
            message = question['message']
    list_of_answers = data_manager.get_data(data_manager.ANSWER_PATH)  # cserélve lesz!
    answers = []
    for answer in list_of_answers:
        if answer['question_id'] == question_id:
            answers.append(answer['message'])
    return render_template("display_question.html", title=title, message=message, answers=answers,
                           question_id=question_id)



@app.route("/question/<question_id>/edit", methods=["GET", "POST"]) #get amikor megjelenít, ha rányom a submit gombra, akkor Post
def edit_question(question_id):
    question=data_manager.get_question_by_id(question_id) #vedd ki a szükséges kérdést
    if request.method == 'POST': #ha rányom a submit-ra, akkor az új infót küldd el a d_m.py-nak
        new_title = request.form['title']
        new_message = request.form['message']
        data_manager.modify_question(question_id, new_title, new_message) #ez írja át a question.csv-t
        return redirect(f'/question/{question_id}') #jelenítsd meg a frissült kérdést
    return render_template("edit.html", question_id=question_id, current_title=question['title'], current_message=question['message'])

#Vero
#Luti

@app.route("/add-question", methods=['POST', 'GET'])
def add_question():
    questions = data_manager.get_data(data_manager.QUESTION_PATH)
    question = {}
    view_number = 0
    vote_number = 0
    if request.method == 'POST':
        question['id'] = data_manager.get_max_id(data_manager.QUESTION_PATH) + 1
        question['submission_time'] = int(now_timestamp)
        question['view_number'] = view_number
        question['vote_number'] = vote_number
        question['title'] = request.form['title']
        question['message'] = request.form['message']
        question['image'] = vote_number
        questions.append(question)
        data_manager.write_data(questions, data_manager.QUESTION_PATH, data_manager.QUESTION_HEADER)
        return redirect(f'/question/{question["id"]}')
    return render_template('add-question.html', id=id, question=question)


# Luti

@app.route('/answer-vote/<id>', methods=['POST'])
def answer_vote(id):
    data_manager.modify_vote(id, 1)
    return redirect('/')

@app.route('/question-vote/<id>', methods=['POST'])
def question_vote(id):
    data_manager.modify_vote(id, 1)
    return redirect('/')

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
