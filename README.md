# MAX AI Assistant

**MAX** is a Python-based AI assistant designed to help you with various tasks using voice commands. It can open websites, play music, fetch the latest news, provide the current time and date, and even chat with you using Google's Generative AI (Gemini).

## Features

- **Voice Commands**: Control MAX using natural language.
- **Web Browsing**: Open popular websites like Google, Facebook, YouTube, and more.
- **Music Playback**: Play songs from a predefined music library.
- **News Updates**: Get the latest headlines using the News API.
- **Time and Date**: Ask for the current time and date.
- **AI-Powered Chat**: Engage in conversations with AI using Google Generative AI (Gemini).

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/max-ai-assistant.git
    cd max-ai-assistant
    ```

2. **Install the required packages**:
    Make sure you have Python 3.7+ installed. Then, install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up API keys**:
    - **News API**: Get your API key from [newsapi.org](https://newsapi.org/) and replace the placeholder in the code (`newsapi = "YOUR_API_KEY"`).
    - **Google Generative AI (Gemini)**: Set up your Gemini API key in your environment variables:

    ```bash
    export GEMINI_API_KEY="your_gemini_api_key"
    ```

4. **Run MAX**:

    ```bash
    python max.py
    ```

## Usage

After running MAX, say "MAX" or "Hey MAX" to activate it, and then provide your command. Example commands include:

- "Good morning"
- "Open Google"
- "Play [song name]"
- "What's the news?"
- "What's the time?"
- "Who are you?"

MAX will process your command and respond either through predefined actions or by generating a response using Google Generative AI.

## Customization

- **Music Library**: Modify `musicLibrary.py` to customize your music library with your preferred songs and their links.
- **Commands**: Add or modify commands in the `processCommand` function to extend MAX's capabilities.

## Pushing to GitHub

To push this project to GitHub, follow these steps:

1. **Initialize Git in your project directory**:

    ```bash
    git init
    ```

2. **Add your files to the staging area**:

    ```bash
    git add .
    ```

3. **Commit your changes**:

    ```bash
    git commit -m "Initial commit of MAX AI Assistant project"
    ```

4. **Add your remote repository**:

    ```bash
    git remote add origin https://github.com/yourusername/repository-name.git
    ```

5. **Push your changes to GitHub**:

    ```bash
    git push -u origin main
    ```

## Dependencies

- `speech_recognition`
- `pyttsx3`
- `requests`
- `google-generativeai`

Make sure these are listed in your `requirements.txt` file.

## Contributing

Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!

