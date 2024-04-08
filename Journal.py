from flask import Flask, render_template
import json
import os
import datetime
import Question_generator

app = Flask(__name__)

with open('questions.json', 'r') as file:
        temp = json.load(file)
last_generated = temp["generated"]


def should_generate_new_question():
    # Check if last_question is empty or if a day has passed since the last question was generated
    if not last_generated:
        return True
    today = datetime.date.today()
    return datetime.datetime.strptime(last_generated, '%m-%d-%Y').date() < today

@app.route('/')
def index():
    script_dir = os.path.dirname("index.html")
    print(__file__)
    file_path = os.path.join(script_dir, 'questions.json')
    if should_generate_new_question():
        Question_generator.main()
        last_generated=datetime.datetime.now()

    with open('questions.json', 'r') as file:
        data = json.load(file)
    questions = data["questions"]
    return render_template('index.html', questions_list=questions)

if __name__ == '__main__':
    app.run(port=5055)