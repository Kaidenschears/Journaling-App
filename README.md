# Journaling Web App

## Overview
Welcome to the Journaling Web App! This application is designed to help you reflect and document your thoughts with ease. Each weekday, you will be presented with 3 thought-provoking questions, and on Sundays, you'll receive 7 questions. The app provides a calm and serene environment with a sunset background to help you relax and focus on your journaling.

## Features
- **Daily Questions:** Receive 3 questions on weekdays and 7 questions on Sundays.
- **Calm Environment:** Write in a tranquil setting with a soothing sunset background.
- **Timer:** A 3-minute timer per question to guide your journaling session, with no consequences if the time runs out.
- **Export Entries:** Download your journal entries as a `.txt` file after each session.

## Getting Started
1. **Launch the App:** Open the web app in your browser.
2. **Daily Questions:** Each day, you will be presented with a set of questions to answer.
3. **Timer:** A 3-minute timer will start for each question, providing a gentle nudge to keep you focused.
4. **Write:** Reflect and write your answers in the provided text boxes.
5. **Export:** At the end of your session, click the export button to download your entries as a `.txt` file.

## Installation
To run the app locally, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/journaling-web-app.git
    cd journaling-web-app
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Start the App:**
    ```bash
    flask run
    ```

4. **Open in Browser:**
    Open your browser and go to `http://localhost:5000`.

## Dependencies
- annotated-types==0.7.0
- anyio==4.4.0
- blinker==1.8.2
- certifi==2024.7.4
- click==8.1.7
- distro==1.9.0
- exceptiongroup==1.2.1
- Flask==3.0.3
- h11==0.14.0
- httpcore==1.0.5
- httpx==0.27.0
- idna==3.7
- importlib_metadata==8.0.0
- itsdangerous==2.2.0
- Jinja2==3.1.4
- MarkupSafe==2.1.5
- openai==1.35.10
- pydantic==2.8.2
- pydantic_core==2.20.1
- sniffio==1.3.1
- tqdm==4.66.4
- typing_extensions==4.12.2
- Werkzeug==3.0.3
- zipp==3.19.2

## Getting an OpenAI API Key
To use the journaling app, you need an API key from OpenAI. Follow these steps to get your API key:

1. **Sign Up or Log In to OpenAI:**
    - Visit the [OpenAI website](https://www.openai.com/).
    - Sign up for an account or log in if you already have one.

2. **Generate an API Key:**
    - Go to the [API Keys page](https://platform.openai.com/account/api-keys).
    - Click on "Create new secret key" to generate a new API key.
    - Copy the generated API key.

3. **Configure the App:**
    - Add your API key to the application's configuration file or environment variable as required.

For more detailed instructions, visit the [OpenAI API documentation](https://platform.openai.com/docs/).

## Usage
- **Daily Questions:** Answer the questions presented each day to reflect on your thoughts and experiences.
- **Timer:** Use the 3-minute timer to pace yourself. Feel free to continue writing if the timer runs out.
- **Export Entries:** After completing your session, click the export button to download your journal entries.

## Contributing
We welcome contributions to improve the Journaling Web App. To contribute, please follow these steps:

1. **Fork the Repository:**
2. **Create a Branch:**
    ```bash
    git checkout -b feature/your-feature
    ```
3. **Commit Changes:**
    ```bash
    git commit -m 'Add your feature'
    ```
4. **Push to Branch:**
    ```bash
    git push origin feature/your-feature
    ```
5. **Create Pull Request:**

## License
This project is open-source and licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mi) file for more details.

## Contact
For any questions or suggestions, please open an issue or contact us at support@journalingwebapp.com.

Enjoy your journaling journey!
