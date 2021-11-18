import csv
import os
dirname = os.path.dirname(__file__)
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
ANSWER_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/answer.csv'
QUESTION_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else dirname + '/sample_data/question.csv'
SORTING_OPTIONS = ['title', 'submission_time', 'message', 'view_number', 'vote_number']

def get_max_id(path):
    input_file = csv.DictReader(open(path))
    max_id = 0
    for row in input_file:
        max_id += 1
    return max_id


def get_data(path):
    data_list = []
    input_file = csv.DictReader(open(path))
    for questions in input_file:
        data_list.append(questions)
    return data_list


def write_data(type, PATH, HEADER):
    with open(PATH, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()
        for answer in type:
            writer.writerow(answer)


def modify_vote(id, vote):
    lines = get_data(QUESTION_PATH)
    for line in lines:
        if line['id'] == id:
            line['vote_number'] = int(line['vote_number']) + vote
    write_data(lines, QUESTION_PATH, QUESTION_HEADER)




def delete_an_answer(answer_id):
    answer_file = get_answers()
    with open(answer_file, 'w') as csv_file:
        for i in range(len(answer_file)):
            if answer_file[i]['id'] == answer_id:
                del answer_file[i]
            write_answers(answer_file[i])


def get_question_by_id(id):
    questions = get_data(QUESTION_PATH)
    for question in questions:
        if question['id'] == id:
            return question #returns question as dictionary

def modify_question(id, new_title, new_message):
    #changes 'title' and 'message' of question_to_edit, and writes it back to questions.csv
    question_to_edit = get_question_by_id(id)
    edited_question = {}
    edited_question['id'] = question_to_edit ['id']
    edited_question['submission_time'] = question_to_edit['submission_time']
    edited_question['view_number'] = question_to_edit['view_number']
    edited_question['vote_number'] = question_to_edit['vote_number']
    edited_question['title'] = new_title
    edited_question['message'] = new_message
    questions = get_data(QUESTION_PATH)
    edited_questions = []
    for question in questions:
        if question['id'] == id:
            edited_questions.append(edited_question)
        else:
            edited_questions.append(question)
    write_data(edited_questions, QUESTION_PATH, QUESTION_HEADER) #a dictionary-k listáját kell visszaadjam neki

