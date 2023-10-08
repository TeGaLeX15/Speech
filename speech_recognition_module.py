import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def recognize_speech():
    with microphone as source:
        print("Говорите...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + command)
        return command
    except sr.UnknownValueError:
        print("Речь не распознана")
        return ""
