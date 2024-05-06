import os
import json
import re
import pyttsx3
from bs4 import BeautifulSoup
import speech_recognition as sr

def fetch_files_from_local(directory):
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        print("An error occurred while fetching files:", e)
        return None

def parse_html(contents):
    parsed_data = {}
    soup = BeautifulSoup(contents, 'html.parser')
    return parsed_data

def parse_php(contents):
    parsed_data = {}
    php_content = re.findall(r'\<\?php(.*?)\?\>', contents, re.DOTALL)
    parsed_data['PHP_Content'] = php_content
    return parsed_data

def parse_txt(contents):
    parsed_data = {}
    parsed_data['Text'] = contents
    return parsed_data

def parse_json(contents):
    parsed_data = {}
    try:
        parsed_data = json.loads(contents)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
    return parsed_data

def handle_query(query, files, repo_directory):
    response = []
    for file_name in files:
        if query.lower() in file_name.lower():
            file_path = os.path.join(repo_directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()
                if file_name.endswith('.html'):
                    parsed_data = parse_html(file_contents)
                elif file_name.endswith('.php'):
                    parsed_data = parse_php(file_contents)
                elif file_name.endswith('.txt'):
                    parsed_data = parse_txt(file_contents)
                elif file_name.endswith('.json'):
                    parsed_data = parse_json(file_contents)
                else:
                    parsed_data = {}
                response.append(parsed_data)
    if not response:
        response = ["No relevant files found."]
    return response


def speak_response(response):
    engine = pyttsx3.init()
    for text in response:
        engine.say(text)
    engine.runAndWait()

def main():
    repo_directory = r"C:\Users\sheri\AppData\Local\Programs\Python\Python312\Scripts\smcoe_webpage-main"

    files = fetch_files_from_local(repo_directory)
    if files:
        print("Files in the repository:", files)
    else:
        print("Failed to fetch files from the repository.")
        return

    recognizer = sr.Recognizer()
    while True:
        speak_response(["Ask me a question:"])
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            try:
                query = recognizer.recognize_google(audio)
                print("You said:", query)
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                continue
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                continue

        if query.lower() == "exit":
            print("Exiting...")
            break
        
        response = handle_query(query, files, repo_directory)  # Passing repo_directory
        print("Response:", response)
        speak_response(response)

if __name__ == "__main__":
    main()
