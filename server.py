from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import data_manager
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} #not compulsory to define extensions

like_button = '/home/luti/codecool/Web/Projects/ask-mate/like.jpeg'


#Hanna
@app.route("/list")
@app.route("/", methods=['GET'])
def list_questions():
    questions = data_manager.get_data()
    question_dict = {}
    if request.args:
        sort_by = request.args['sort_by']
        order = request.args['order']
    else:
        sort_by = 'submission_time'
        order = 'descending'
    for question in questions:
        question_dict[question['title']] = [question[sort_by], question['id']]
    sorted_question_dict = dict(sorted(question_dict.items(), key=lambda item: item[1][0], reverse=True))
    if order == 'ascending':
        sorted_question_dict = dict(sorted(question_dict.items(), key=lambda item: item[1][0]))
    order_options = data_manager.ORDER_OPTIONS
    return render_template('list.html', questions=sorted_question_dict, like=like_button,
        sort_options=data_manager.SORTING_OPTIONS, sort_by=sort_by, order_options=order_options, order=order)
#Hanna
#Berni
#new answer / post an answer
@app.route('/question/<question_id>/new-answer', methods = ['GET', 'POST'])
def new_answer(question_id):
    answers = data_manager.get_data()
    from datetime import datetime
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    if request.method == "POST":
        new_answer = {
            "id": data_manager.get_max_id(data_manager.ANSWER_PATH)+1, #A unique identifier for the answer.
            "submission_time":int(now_timestamp), #floatot ad ki alapból, The UNIX timestamp when the answer is posted.
            "vote_number":str(0), #The sum of votes the answer receives.
            "question_id": question_id,#Ide majd az az ID kell, ami ami a View Questionből jön, Verótól
            "message": request.form.get("message"), #The answer text.
            "image":request.form.get("image") #The path to the image for this answer.
            }
        answers.append(new_answer)
        data_manager.write_answer(submission_time, vote_number, question_id, message, image)
        return redirect("/question/" + str(question_id))
    return render_template("new_answer.html", question_id=question_id)


@app.route('/answer/<answer_id>/delete')
def delete_an_answer(answer_id):
    data_manager.delete_an_answer(answer_id)
    # return redirect("/question/" + str(question_id))
    return redirect("/")

@app.route('/question/<question_id>/delete')
def delete_a_question(question_id):
    data_manager.delete_a_question(int(question_id))
    return redirect("/")

#Berni
#Vero
@app.route("/question/<question_id>")
def display_question(question_id):
    questions = data_manager.get_data()
    title = ""
    message = ""
    for question in questions:
        if question['id'] == question_id:
            title = question['title']
            message = question['message']
            image_path = question['image']
    list_of_answers = data_manager.get_data()  # cserélve lesz!
    answers = []
    for answer in list_of_answers:
        if answer['question_id'] == question_id:
            answer_dict = {}
            answer_dict['id'] = answer['id']
            answer_dict['message'] = answer['message']
            answers.append(answer_dict)

    return render_template("display_question.html", title=title, message=message, answers=answers,
                           question_id=question_id, image_path=image_path)



@app.route("/question/<question_id>/edit", methods=["GET", "POST"]) #get amikor megjelenít, ha rányom a submit gombra, akkor Post
def edit_question(question_id):
    question=data_manager.get_question_by_id(question_id) #vedd ki a szükséges kérdést
    if request.method == 'POST': #ha rányom a submit-ra, akkor az új infót küldd el a d_m.py-nak
        new_title = request.form['title']
        new_message = request.form['message']
        filename = ''
        if 'image' in request.files:
            image = request.files['image']
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
        data_manager.modify_question(new_title, new_message, filename, question_id)  # ez írja át a question.csv-t
        return redirect(f'/question/{question_id}') #jelenítsd meg a frissült kérdést
    return render_template("edit.html", question_id=question_id,
                           current_title=question['title'],
                           current_message=question['message'])

#Vero
#Luti

@app.route("/add-question", methods=['POST', 'GET'])
def add_question():
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    questions = data_manager.get_data()
    question = {}
    view_number = 0
    vote_number = 0
    if request.method == 'POST':
        question['id'] = data_manager.get_max_id(data_manager.QUESTION_PATH)
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


@app.route('/answer-vote/<answer_id>/<vote>', methods=['POST'])
def answer_vote(answer_id, vote):
    increment = 1 if vote == 'vote_up' else -1
    data_manager.modify_answer_vote(answer_id, increment)
    return redirect('/')


@app.route('/question-vote/<id>/<vote>', methods=['POST'])
def question_vote(id, vote):
    increment = 1 if vote == 'vote_up' else -1
    data_manager.modify_question_vote(id, increment, data_manager.QUESTION_PATH, data_manager.QUESTION_HEADER)
    return redirect('/')

# Luti

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
