import openai
import json
from datetime import datetime
from Secrets import API_KEY

# Set your OpenAI GPT-3 API key
openai.api_key = API_KEY


def generate_questions(day):
    # Define a prompt based on the day
    
    if day == "Sunday":
        prompt="Generate 7 reflective questions about the week."
    else:
        prompt = "Generate 2 reflective question about your day and one question to get to know yourself better. The structure of the output will be a numbered question followed by comma"

    # Make an API call to GPT-3 to generate questions
    response = openai.chat.completions.create(
        messages=[{ "role": "user", "content": prompt }],
        model="gpt-3.5-turbo", 
    )
    print(response.choices[0].message.content)
    # Extract and return the generated questions
    generated_questions = str(response.choices[0].message.content).strip().split('\n')

    return list(filter(lambda x: x != "", generated_questions)) #filters empty strings

def create_json_file(questions):
    # Create a dictionary with questions
    data = {'questions': questions, 'generated': str(datetime.now().strftime('%m-%d-%Y'))}

    # Convert data to JSON format
    custom_json = json.dumps(data, indent=2)

    # Save the JSON to a file
    with open('questions.json', 'w') as json_file:
        json_file.write(custom_json)

def main():
    # Get the current day of the week
    current_day = datetime.now().strftime('%A')

    # Generate questions based on the day
    questions = generate_questions(current_day)

    # Create and save the JSON file
    create_json_file(questions)

if __name__ == "__main__":
    main()