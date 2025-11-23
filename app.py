import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('quiz.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    category = request.args.get('category')
    if not category:
        return "Category not specified!", 400
    return render_template('quiz.html', category=category)

@app.route('/api/questions')
def get_questions():
    category = request.args.get('category')
    conn = get_db_connection()
    # CONFIRMED: Quiz length is set to 10 questions
    questions_from_db = conn.execute(
        'SELECT * FROM questions WHERE category = ? ORDER BY RANDOM() LIMIT 10', (category,)
    ).fetchall()
    conn.close()

    if not questions_from_db:
        return jsonify({"error": "No questions found for this category"}), 404

    questions = []
    for q in questions_from_db:
        questions.append({
            "question": q['question_text'],
            "section": q['section'],
            "options": [q['option_a'], q['option_b'], q['option_c'], q['option_d']],
            "answer": q['correct_answer']
        })
    return jsonify(questions)

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)