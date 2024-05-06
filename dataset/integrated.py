from flask import Flask, request, jsonify, send_file
import os
import cv2
import pyttsx3
import speech_recognition as sr
import scrap
from FAQ import college_qa_list
from nltk.chat.util import Chat, reflections
import numpy as np

app = Flask(__name__)

# Define the directory where QR code images are stored
WAYFINDER_DIR = r'C:\Users\sheri\AppData\Local\Programs\Python\Python312\NEXUS\wayfinder'
# Initialize the speech engine
engine = pyttsx3.init()

# Get the scraped data
positions_names, facilities_str = scrap.scrape_data()

# Define pairs of patterns and responses
pairs = [
    ['hi|hello', ['Hello!', 'Hi there!', 'How can I help you?']],
    ['how are you?', ['I am fine, thank you!', 'I\'m doing well, how about you?']],
    ['(.*)who created(.*)', ['I was created by Developer Sherin in 2024.']],
    ['(.*) your name?', ['My name is Assistant.']],
    ['(.*) help (.*)', ['Sure, I can help you with that.']],
    ['(.*) (bye|goodbye)', ['Goodbye!', 'Take care!']],
    ['.*facilities.*', [f'Facilities are: {facilities_str}']],
    ['(.*)positions and names(.*)', [f'Positions and names are: {positions_names}']],
    ['(.*)chairman(.*)', ['The chairman is ' + [name for position, name in positions_names if 'chairman' in position.lower()][0]]],
]

# Define pairs with FAQ patterns and responses
faq_pairs = []
for qa in college_qa_list:
    faq_pairs.append([qa.question, [qa.answer]])

# Add FAQ pairs to the existing pairs
pairs += faq_pairs

# Create a chatbot using the pairs and reflections
chatbot = Chat(pairs, reflections)

# Define the face detection cascade classifier
face_cascade = cv2.CascadeClassifier('face reco/haarcascade_frontalcatface_extended.xml')
cap = cv2.VideoCapture(0)

@app.route('/wayfinder', methods=['GET'])
def wayfinder():
    # Get the department requested by the user
    department = request.args.get('department')

    # Check if the requested department exists
    department_dir = os.path.join(WAYFINDER_DIR, department.lower())
    if os.path.exists(department_dir):
        # Assume the QR code file is named 'qr.png' within the department directory
        qr_code_path = os.path.join(department_dir, 'qr.png')
        return send_file(qr_code_path, mimetype='image/png')
    else:
        return jsonify({'error': 'Department not found'})

def process_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            user_input = r.recognize_google(audio)
            print("You said: " + user_input)
            return user_input
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None

if __name__ == '__main__':
    r = sr.Recognizer()
    print("Welcome to the virtual assistant. Speak 'quit' to exit.")
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # If faces are detected, speak a welcome message and ask for user input
        if len(faces) > 0:
            engine.say("Welcome to our college. How can I help you?")
            engine.runAndWait()

            user_input = process_audio()
            if user_input and user_input.lower() == 'quit':
                break

            response = chatbot.respond(user_input)
            print("Assistant:", response)

            # Make the chatbot say the response
            engine.say(response)
            engine.runAndWait()

            # Display the QR code image for wayfinding
            department = user_input.split()[-1]
            department_dir = os.path.join(WAYFINDER_DIR, department.lower())
            if os.path.exists(department_dir):
                qr_code_path = os.path.join(department_dir, 'qr.png')
                qr_img = cv2.imread(qr_code_path)
                cv2.imshow('QR Code', qr_img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
