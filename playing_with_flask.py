from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# This method returns questions. Note it is called in both methods executed by the routes.
# going forward, you could update this method to read questions from CSV or Dynamo.
def get_questions():
    questions = [
      {"id": "1", "text": "This is question 1", "options": ["option 1.1", "option 1.2", "option 1.3"], "type": "radio" },
      {"id": "2", "text": "This is question 2", "options": ["option 2.1", "option 2.2", "option 2.3"], "type": "checkbox" }
    ]
    return questions

@app.route("/text")
def get_questions_as_text():
    all_questions = ''
    for question in get_questions():
        for k, v in question.items():
            all_questions = all_questions + ''.join('{}: {}'.format(k, v)) + '</br>'

    return all_questions

@app.route('/fancy')
def get_questions_rendered():
    return render_template('questions.html', questions=get_questions())
