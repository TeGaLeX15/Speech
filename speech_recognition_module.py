import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

microphone_in_use = False

def recognize_speech():
    global microphone_in_use

    if microphone_in_use:
        print("Микрофон уже используется.")
        return None

    with microphone as source:
        print("Говорите...")
        try:
            audio = recognizer.listen(source)
            microphone_in_use = True  # Устанавливаем флаг, что микрофон используется
        except AssertionError as e:
            print("Ошибка:", e)
            microphone_in_use = False  # Снимаем флаг после ошибки
            return None

    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + command)
        microphone_in_use = False  # Снимаем флаг после успешного распознавания
        return command
    except sr.UnknownValueError:
        print("Речь не распознана")
        microphone_in_use = False  # Снимаем флаг после ошибки
        return ""
