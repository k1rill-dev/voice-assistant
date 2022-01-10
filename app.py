import speech_recognition
import os
import random
import pyttsx3
import wave
import json


"""
Это голосовой помощник по имени Моника! (почему именно Моника не скажу)
"""
sr = speech_recognition.Recognizer()
#пауза между произнесенными словами
sr.pause_threshold = 0.5
#словарь, где указаны команды в еще одном словаре, где указаны слова-триггеры, которые вызывают определенные команды(фух)


commands = {
    'commands': {
        'hi': ['привет', 'приветствую'],
        'create_task':['добавь задачу', 'создай задачу'],
        'play_music': ['включи музыку']
    }
}

def listen():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except:
        print('Я тебя не понимаю...')


def hi():
    return 'Привет солнышко :З'

def play_music():
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system(f'start {random_file}')

    return f'Я нашла такую песню - {random_file.split("/")[-1]}'

def create_task():
    print('Скажи, что нужно добавить в список дел, и я добавлю)')

    query = listen()
    with open('list.txt', 'a', encoding='utf-8') as file:
        file.write(f'{query} \n')
    return f'Все готово) задача {query} добавлена в список дел. Смотри не забудь про нее! :З'

def main():
    query = listen()
    for i, j in commands['commands'].items():
        if query in j:
            print(globals()[i]())

if __name__ == "__main__":
    main()
