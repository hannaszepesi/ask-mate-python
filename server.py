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
def new_answer(question_id):
    from datetime import datetime
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    if request.method == "POST":
        new_answer = {
            "id": data_manager.get_max_id()+1 #A unique identifier for the answer.
            "submission_time":int(now_timestamp) #floatot ad ki alapból, The UNIX timestamp when the answer is posted.
            "vote_number":str(0) #The sum of votes the answer receives.
            "question_id": #The ID of the question to which this answer belongs.
            "message": request.form.get("message") #The answer text.
            "image":request.form.get("image") #The path to the image for this answer.
        }
        data_manager.write_answers((new_answer))
        return redirect("/question"+str(question_id))
    return render_template("new_answer.html", question_id = question_id)

@app.route('/add_question', method = ["POST", "GET"])
def add_question():
    from datetime import datetime
    now = datetime.now()
    now_timestamp = datetime.timestamp(now)
    if method == "POST":
        new_question = {
            "id": data_manager.get_max_id()+1  #A unique identifier for the question.
            "submission_time":now_timestamp #The UNIX timestamp when the question is posted.
            "view_number": #The number of times this question is displayed in the single question view.
            "vote_number": #The sum of votes this question receives.
            "title": #The title of the question.
            "message":request.form.get("message") #The question text.
            "image":request.form.get("url")#The path to the image for this question.
        }
        data_manager.write_quiestions()
        return redirect(="/list")
    return render_template("add_question.html")


#Berni
#Vero
@app.route('/question/<question_id>', methods = ['GET', 'POST'])
def display_question():


#Vero
#Luti
#Luti

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
