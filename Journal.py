from flask import Flask, render_template
import json
import datetime
import Question_generator
from pathlib import Path



app = Flask(__name__)



def generate_new_question():
    # Check if last_question is empty or if a day has passed since the last question was generated
    file_path = Path('questions.json')
    if not file_path.exists():
         return True
    
    else:
         with open('questions.json', 'r') as file:
            temp = json.load(file)

    if "generated" in temp:
        last_generated = temp["generated"]
    else:
        last_generated=None
    if not last_generated or last_generated =="":
        return True
    today = datetime.date.today()
    return datetime.datetime.strptime(last_generated, '%m-%d-%Y').date() < today

@app.route('/')
def index():

    if generate_new_question():
        Question_generator.main()

    with open('questions.json', 'r') as file:
        data = json.load(file)
    questions = data["questions"]
    return render_template('index.html', questions_list=questions)

if __name__ == '__main__':
    app.run(port=5055)