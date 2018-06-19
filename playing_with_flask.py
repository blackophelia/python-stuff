from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

questions = [
  {"id": "1", "text": "This is question 1", "options": ["option 1.1", "option 1.2", "option 1.3"] },
  {"id": "2", "text": "This is question 2", "options": ["option 2.1", "option 2.2", "option 2.3"] }
]

@app.route("/questions")
def get_questions():
    all_questions = ''
    for question in questions:
        for k, v in question.items():
            all_questions = all_questions + ''.join('{}: {}'.format(k, v)) + '</br>'

    return all_questions
