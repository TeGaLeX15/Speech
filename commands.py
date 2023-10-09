import webbrowser

def process_command(command):
    # Открытие Youtube
    if "открой youtube" in command.lower():
        webbrowser.open('https://www.youtube.com/')
        return "Открыл YouTube. Приятного просмотра!"

    # Поиск в Google
    if command.lower().startswith("найди в google"):
        # Извлекаем фразу для поиска
        search_query = command[14:]  # Отсекаем "найди в google"
        search_query = search_query.strip()  # Убираем лишние пробелы

        if search_query:
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            print(f"Выполнил поиск в Google по запросу: {search_query}")
        else:
            print("Фраза для поиска не распознана.")

    # Поиск в Яндекс
    if command.lower().startswith("найди в яндексе"):
        # Извлекаем фразу для поиска
        search_query = command[16:]  # Отсекаем "найди в яндексе"
        search_query = search_query.strip()  # Убираем лишние пробелы

        if search_query:
            search_url = f"https://yandex.ru/search/?text={search_query}"
            webbrowser.open(search_url)
            print(f"Выполнил поиск в Яндексе по запросу: {search_query}")
        else:
            print("Фраза для поиска не распознана.")
    else:
        print("Команда не распознана.")

    # Поиск в YouTube
    if command.lower().startswith("найди в youtube"):
        # Извлекаем фразу для поиска
        search_query = command[15:]  # Отсекаем "найди в google"
        search_query = search_query.strip()  # Убираем лишние пробелы

        if search_query:
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(search_url)
            print(f"Выполнил поиск в YouTube по запросу: {search_query}")
        else:
            print("Фраза для поиска не распознана.")

    # Открытие почтового ящика
    if "открой мою почту" in command.lower():
        if "Gmail" in command:
            webbrowser.open('https://mail.google.com/')
            return "Открыл Gmail. Жду новых сообщений!"
        elif "Яндекс" in command:
            webbrowser.open('https://mail.yandex.ru/')
            return "Открыл Яндекс.Почту. Жду новых сообщений!"
        elif "email" in command:
            webbrowser.open('https://e.mail.ru/') 
            return "Открыл Email.ru. Жду новых сообщений!"
        # Если команда не соответствует ни одной из почтовых служб
        return "Извините, не могу понять, какую почту открыть."

    return "Команда выполнена: " + command
