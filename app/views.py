from flask import render_template, jsonify
from app import app, services


@app.route('/')
@app.route('/index')
def index():
    quizzes = services.list()
    return render_template('list.html', quizzes=quizzes)


@app.route('/detail/<token>')
def detail(token):
    quiz = services.detail(token)
    print(quiz)
    return render_template('detail.html', quiz=quiz)


@app.route('/quiz/detail/<token>')
def quiz_detail(token):
    quiz = services.detail(token)
    return render_template('fragments/info.html', quiz=quiz)


@app.route('/quiz/next/<token>', methods=['POST'])
def quiz_next(token):
    services.start_next_question(token)
    quiz = services.detail(token)
    return render_template('fragments/info.html', quiz=quiz)


@app.route('/quiz/submit/<token>', methods=['POST'])
def quiz_submit(token):
    answer = 'blah'
    services.submit_answer(token, answer)
    quiz = services.detail(token)
    return render_template('fragments/info.html', quiz=quiz)
