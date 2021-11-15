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
    ids = []
    if request.method == "POST":
        new_answer = {
            "id": data_manager.generate_id(ids)
            "submission_time":
            "view_number":
            "vote_number":str(0)
            "title":
            "message": request.form.get("message")
            "image":
        }
        data_manager.write_answers((new_answer))
        return redirect("/question"+str(question_id))
    return render_template("new_answer.html", question_id = question_id)
#Berni
#Vero
#Vero
#Luti
#Luti

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
