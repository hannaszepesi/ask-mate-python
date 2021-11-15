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
#Berni
#Vero
#Vero
#Luti
#Luti

if __name__ == "__main__":
    app.run()
