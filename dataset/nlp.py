import nltk
from nltk.chat.util import Chat, reflections
import speech_recognition as sr
import scrap
import pyttsx3
from flask import Flask, request, jsonify
from FAQ import college_qa_list

app = Flask(__name__)

# Initialize the speech engine
engine = pyttsx3.init()

# Get the scraped data
positions_names, facilities_str = scrap.scrape_data()

# Define pairs of patterns and responses for the chatbot
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
faq_pairs = [[qa.question, [qa.answer]] for qa in college_qa_list]

# Add FAQ pairs to the chatbot pairs
pairs += faq_pairs

# Create a chatbot using the pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print("You said: " + user_input)
            return user_input
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))
            return None

# Flask route to handle incoming speech requests
@app.route('/speak', methods=['POST'])
def speak():
    user_input = request.json.get('text', '')
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    print("Welcome to the virtual assistant. Speak 'quit' to exit.")
    while True:
        user_input = recognize_speech()
        if not user_input:
            continue
        if user_input.lower() == 'quit':
            break
        response = chatbot.respond(user_input)
        print("Assistant:", response)
        engine.say(response)
        engine.runAndWait()
