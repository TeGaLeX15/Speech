import webbrowser

def process_command(command):
    if "youtube" in command.lower():
        webbrowser.open('https://www.youtube.com/')
        return "Открыл YouTube. Приятного просмотра!"
    # Добавьте здесь обработку других команд

    return "Команда выполнена: " + command
