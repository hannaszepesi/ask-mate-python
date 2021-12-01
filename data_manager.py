import csv
import os
import database_common
from psycopg2 import sql
SORTING_OPTIONS = ['title', 'submission_time', 'message', 'view_number', 'vote_number']
ORDER_OPTIONS = ['ASC', 'DESC']

@database_common.connection_handler
def get_data(cursor, table):
    if table == 'question':
        query = """
            SELECT *
            FROM question
            """
    if table == 'answer':
        query = """
            SELECT *
            FROM answer
            """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def write_question(cursor, submission_time, view_number, vote_number, title, message, image):
    query = """
    INSERT INTO question (submission_time, view_number, vote_number, title, message, image) 
    VALUES (%s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, (submission_time, view_number, vote_number, title, message, image))


@database_common.connection_handler
def write_comment(cursor):
    query = """
    INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count) 
    VALUES (%s, %s, %s, %s, %s);"""
    cursor.execute(query, (question_id, answer_id, message, submission_time, edited_count))


@database_common.connection_handler
def write_answer(cursor, submission_time, vote_number, question_id, message, image):
    query = """
    INSERT INTO answer (submission_time, vote_number, question_id, message, image) 
    VALUES (%s, %s, %s, %s, %s);"""
    cursor.execute(query, (submission_time, vote_number, question_id, message, image))


@database_common.connection_handler
def write_tag(cursor):
    query = """
    INSERT INTO tag (submission_time, view_number, vote_number, title, message, image) 
    VALUES (%s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, (submission_time, view_number, vote_number, title, message, image))


@database_common.connection_handler
def modify_question_vote(cursor, question_id, vote):
    query = """
        UPDATE question
        SET vote_number = vote_number + %(vote)s
        WHERE id = %(question_id)s;
        """
    cursor.execute(query, {"vote": vote, "question_id": question_id})


@database_common.connection_handler
def modify_answer_vote(cursor, vote, answer_id):
    query = """
        UPDATE answer
        SET vote_number = vote_number + %s
        WHERE id = %s;
        """
    cursor.execute(query, (vote, answer_id,))


@database_common.connection_handler
def delete_an_answer(cursor, answer_id):
    query = """
        DELETE from answer
        WHERE id = %s;"""
    cursor.execute(query, (answer_id,))


@database_common.connection_handler
def delete_a_question(cursor, question_id):
    query1 = """
        DELETE from question
        WHERE id = %s;
        """
    query2 = """
            DELETE from question_tag
            WHERE question_id = %s;
            """
    query3 = """
            DELETE from comment
            WHERE question_id = %s;
            """
    cursor.execute(query3, (question_id,))
    cursor.execute(query2, (question_id,))
    cursor.execute(query1, (question_id,))


@database_common.connection_handler
def get_question_by_id(cursor, id):
    query = """
        SELECT *
        FROM question
        WHERE id = %(id)s
        """
    cursor.execute(query, {"id": id})
    return cursor.fetchone()


@database_common.connection_handler
def get_answer_by_id(cursor, id):
    query = """
        SELECT *
        FROM answer
        WHERE id = %(id)s
        """
    cursor.execute(query, {"id": id})
    return cursor.fetchone()


@database_common.connection_handler
def modify_question(cursor,  title, message, image_path, question_id):
    query = """
            UPDATE question
            SET title, message, image_path = %s, %s, %s
            WHERE question_id = %s;"""
    cursor.execute(query, (title, message, image_path, question_id,))


@database_common.connection_handler
def sort_questions(cursor, sortby='submission_time', order='DESC'):
    query = sql.SQL("SELECT id, title FROM question ORDER BY {sort_by} {orderby} LIMIT 5;")
    cursor.execute(query.format(sort_by=sql.Identifier(sortby), orderby=sql.SQL(order)))
    return cursor.fetchall()


@database_common.connection_handler
def edit_answer(cursor, message, answer_id):
    query = """
            UPDATE answer
            SET message = %s
            WHERE id = %s;"""
    cursor.execute(query, (message, answer_id,))


@database_common.connection_handler
def get_question_tag(cursor, question_id):
    query = """SELECT q.question_id, t.id, t.name 
            FROM question_tag q 
            INNER JOIN tag t 
            ON q.tag_id = t.id
            WHERE q.question_id = %(id)s;"""
    cursor.execute(query, {"id": question_id})
    return cursor.fetchall()

@database_common.connection_handler
def get_tags(cursor):
    query = """
        SELECT id, name 
        FROM tag;
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def write_tags(cursor, tag_id, question_id):
    query = """ INSERT INTO question_tag (question_id, tag_id) 
                VALUES (%s, %s);"""
    cursor.execute(query, (question_id, tag_id))

@database_common.connection_handler
def write_new_tag(cursor, tag_name):
    query = """ 
                INSERT INTO tag (name)
                VALUES (%(name)s);"""
    cursor.execute(query, {"name": tag_name})



