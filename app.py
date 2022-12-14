from flask import Flask, session
from character_utils import create_character_question_data
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile('config.py')

CORS(app, origins="http://localhost:3000", headers=['Content-Type', 'Authorization'], supports_credentials=True)

def get_question_no():
    return str(session["question"])

def update_user_question():
    session["question"] = session["question"] + 1
    return session["question"]

@app.route('/api/start')
def start_game():
    session["question"] = 1
    session["score"] = 0
    return "New game started", 200

@app.route('/api/question')
def create_question():
    characters = [create_character_question_data() for iter in range(4)]
    # # pick a random character to be correct 
    correct_character_id = characters[np.random.randint(0,3)]["id"]
    question_no = get_question_no()
    session[question_no] = correct_character_id
    return {"options": characters, "correct_id": correct_character_id}

@app.route('/api/score/<int:user_guess_id>', methods=["POST"])
def update_score(user_guess_id):
    correct_answer = session[get_question_no()]
    increment = 1 if correct_answer == user_guess_id else 0
    session["score"] = session["score"] + increment
    current_question_no = update_user_question()
    return {"question_no": current_question_no}

@app.route('/api/finish')
def end_game():
    score = session['score']
    return {"score": score}
