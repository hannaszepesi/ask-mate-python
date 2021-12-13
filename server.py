<<<<<<< HEAD
from flask import Flask, render_template
from bonus_questions import SAMPLE_QUESTIONS
=======
from flask import Flask
>>>>>>> ask-mate-2-python-hannaszepesi/master

app = Flask(__name__)


<<<<<<< HEAD
@app.route("/bonus-questions")
def main():
    return render_template('bonus_questions.html', questions=SAMPLE_QUESTIONS)


if __name__ == "__main__":
    app.run(debug=True)
=======
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
>>>>>>> ask-mate-2-python-hannaszepesi/master
