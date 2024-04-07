from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    script_dir = os.path.dirname("index.html")
    print(__file__)
    file_path = os.path.join(script_dir, 'questions.json')
    with open('questions.json', 'r') as file:
        data = json.load(file)
    questions = data["questions"]
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app.run(port=5055)