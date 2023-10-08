from flask import Flask, render_template
from speech_recognition_module import recognize_speech
from commands import process_command

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_command', methods=['POST'])
def process_voice_command():
    command = recognize_speech()
    result = process_command(command)
    return render_template('done_command.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
