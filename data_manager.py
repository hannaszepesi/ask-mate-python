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
    if table == 'comment':
        query = """
            SELECT *
            FROM comment
        """
    if table == 'tag':
        query = """
        SELECT id, name
        FROM tag
        """
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def write_question(cursor, submission_time, view_number, vote_number, title, message, image, user_id):
    query = """
    INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, (submission_time, view_number, vote_number, title, message, image, user_id))


@database_common.connection_handler
def write_comment(cursor, question_id, message, submission_time, user_id):
    query = """
    INSERT INTO comment (question_id, message, submission_time, user_id) 
    VALUES (%s, %s, %s, %s);"""
    cursor.execute(query, (question_id, message, submission_time, user_id))


@database_common.connection_handler
def write_comment_to_answer(cursor, answer_id, message, submission_time, user_id):
    query = """
    INSERT INTO comment (answer_id, message, submission_time, user_id) 
    VALUES (%s, %s, %s, %s);"""
    cursor.execute(query, (answer_id, message, submission_time, user_id))


@database_common.connection_handler
def write_answer(cursor, submission_time, vote_number, question_id, message, image, user_id):
    query = """
    INSERT INTO answer (submission_time, vote_number, question_id, message, image, user_id) 
    VALUES (%s, %s, %s, %s, %s, %s);"""
    cursor.execute(query, (submission_time, vote_number, question_id, message, image, user_id))


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
def get_answers_for_question(cursor, question_id):
    query = """
    SELECT * 
    FROM answer
    WHERE question_id = %(question_id)s
    """
    cursor.execute(query, {"question_id": question_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_question_comments(cursor, question_id):
    query = """
            SELECT * 
            FROM comment 
            WHERE question_id = %(question_id)s 
            AND answer_id is NULL ;"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@database_common.connection_handler
def get_answer_comments(cursor, answer_id):
    query = """
            SELECT * 
            FROM comment 
            WHERE answer_id = %(answer_id)s
            AND question_id is NULL ORDER BY submission_time DESC;"""
    cursor.execute(query, {'answer_id': answer_id})
    return cursor.fetchall()


@database_common.connection_handler
def modify_question(cursor,  title, message, image_path, question_id):
    query = """
            UPDATE question
            SET title = %s, message = %s, image = %s
            WHERE id = %s;"""
    cursor.execute(query, (title, message, image_path, question_id,))


@database_common.connection_handler
def sort_questions(cursor, sortby='submission_time', order='DESC'):
    query = sql.SQL("SELECT id, title, view_number, vote_number FROM question ORDER BY {sort_by} {orderby} LIMIT 5;")
    cursor.execute(query.format(sort_by=sql.Identifier(sortby), orderby=sql.SQL(order)))
    return cursor.fetchall()


@database_common.connection_handler
def edit_answer(cursor, message, answer_id, image_path):
    query = """
            UPDATE answer
            SET message = %s, image = %s
            WHERE id = %s;"""
    cursor.execute(query, (message, image_path, answer_id))

@database_common.connection_handler
def search_question(cursor, search_phrase):
    search_phrase = f'%{search_phrase}%'
    query = """
            SELECT title, message
            FROM question
            WHERE title LIKE %(found_data)s or message LIKE %(found_data)s;
            """
    cursor.execute(query, {'found_data':search_phrase})
    return cursor.fetchone()

@database_common.connection_handler
def increase_view(cursor, question_id):
    query = """
            UPDATE question
            SET view_number = view_number +1
            WHERE id = %s;"""
    cursor.execute(query, (question_id,))


@database_common.connection_handler
def get_comment_by_question_id(cursor, comment_id):
    query="""
    SELECT question_id 
    FROM comment
    WHERE id = %s;
    """
    cursor.execute(query, (comment_id,))
    return cursor.fetchall()

@database_common.connection_handler
def get_question_by_answer_id(cursor, answer_id):
    query="""
    SELECT question_id 
    FROM answer
    WHERE id = %s;
    """
    cursor.execute(query, (answer_id))
    return cursor.fetchone()

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


@database_common.connection_handler
def edit_comment(cursor, comment, submission_time, id):
    query = """
            UPDATE comment
            SET message = %s, submission_time = %s
            WHERE id = %s;"""
    cursor.execute(query, (comment, submission_time, id))


@database_common.connection_handler
def get_comment(cursor, id):
    query = """
        SELECT question_id, message
        FROM comment
        WHERE id = %s
        """
    cursor.execute(query, (id,))
    return cursor.fetchone()


@database_common.connection_handler
def delete_comment(cursor, comment_id):
    query = """
    DELETE FROM comment
    WHERE id = %s;
    """
    cursor.execute(query, (comment_id,))

@database_common.connection_handler
def delete_tag(cursor, question_id, tag_id):
    query = """
    DELETE FROM question_tag
    WHERE question_id = %(q_id)s AND tag_id = %(t_id)s
    """
    cursor.execute(query, {"q_id": question_id, "t_id": tag_id})


@database_common.connection_handler
def get_user_by_email(cursor, username):
    query = """
         SELECT *
         FROM users
         WHERE username = %(username)s;
         """
    cursor.execute(query, {"username":username})
    return cursor.fetchone()


@database_common.connection_handler
def get_users(cursor):
    query = """
    SELECT u.username, u.registration_date, u.reputation,
    COUNT (distinct question.id) as asked_questions, COUNT (distinct answer.id) as answers, COUNT (distinct comment.id) as comments
    FROM users as u
    LEFT JOIN question ON u.user_id = question.user_id
    LEFT JOIN answer ON u.user_id = answer.user_id
    LEFT JOIN comment ON u.user_id = comment.user_id
    GROUP BY u.username, u.registration_date, u.reputation;   
    """
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def add_new_user(cursor, username, hashed_password, reg_date):
    query = """
    INSERT INTO users (username, hashed_password, registration_date, reputation)
    VALUES( %s, %s, %s, 0);"""
    cursor.execute(query, (username, hashed_password, reg_date,))


@database_common.connection_handler
def change_reputation(cursor, increment, user_id):
    query = """
             UPDATE users
             SET reputation = reputation + %s
             WHERE user_id = %s;"""
    cursor.execute(query, (increment, user_id,))


@database_common.connection_handler
def get_tags_with_numbers(cursor):
    query = """
        SELECT t.name, COUNT(q.tag_id) as number
        FROM tag as t
        LEFT OUTER JOIN question_tag as q
        ON t.id = q.tag_id
        GROUP BY t.id;
         """
    cursor.execute(query)
    return cursor.fetchall()
