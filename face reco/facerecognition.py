import cv2
import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech():
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

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(r'C:\Users\sheri\AppData\Local\Programs\Python\Python312\NEXUS\face reco\haarcascade_frontalcatface_extended.xml')

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        engine.say("Welcome to our college. How can I help you?")
        engine.runAndWait()

        user_query = recognize_speech()
        if user_query:
            # Process user's query and provide a response
            response = "You asked: " + user_query
            engine.say(response)
            engine.runAndWait()

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
