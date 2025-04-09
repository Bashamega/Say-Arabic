# Say Arabic - نطق العربية


This project provides a Python application that generates videos from Arabic words and their meanings. Each video includes the word spoken using text-to-speech, displayed with its meaning, and accompanied by an audio pronunciation.

## Features

- **Text-to-Speech**: Converts Arabic text to speech using gTTS.
- **Video Generation**: Creates a video with Arabic text and audio.
- **Support for Arabic Script**: Utilizes `arabic_reshaper` and `python-bidi` to properly display Arabic script.

## Requirements

Ensure you have Docker installed on your system to build and run this application using the provided Dockerfile. Alternatively, you can manually install the dependencies listed in `requirements.txt`.

## Setup and Usage

1. **Clone the Repository**
   ```
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Build the Docker Image**
   ```
   docker build -t arabic-pronunciation .
   ```

3. **Run the Container**
   ```
   docker run arabic-pronunciation
   ```

Alternatively, if you prefer to run it locally without Docker:

1. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the script:
   ```
   python main.py
   ```