import speech_recognition
from threading import Thread
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os 
import serial
import random
import wikipedia
import keyboard
ttsEngine = pyttsx3.init()
ser = serial.Serial('com4',9600);
result = [0,0]
wikipedia.set_lang("ru")




#########################################
names = ["саня","сань","алиса","привет сири","компьютер","санчоус","санечек","сантьяго","сани","александр"]

name_answers = ["внимательно слушаю","что надо?","что такое?","слушаю","я здесь"]

call_pogoda = ["что с погодой","расскажи о погоде","проанализируй воздух","какая погода","что с воздухом","какая сейчас влажность"]

call_lockpc = ["заблокируй пк","заблокируй компьютер","спать","блокируй компьютер"]

############################################


class VoiceAssistant:

    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""


def setup_assistant_voice():
    """
    Установка голоса по умолчанию (индекс может меняться в 
    зависимости от настроек операционной системы)
    """
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()

def record_and_recognize_audio(*args: tuple): 
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Жду имени...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google 
        try:
            print("Распознаю обращение...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data
def record_and_recognize_command(*args: tuple): 
    """
    Запись и распознавание аудио
    """

    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Словил имя, слушаю...")
            text = name_answers[random.randint(0,4)]
            play_voice_assistant_speech(text)
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google 
        try:
            print("Распознаю команду...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data
 #ABOBA
while True:
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        # старт записи речи с последующим выводом распознанной речи 
        voice_input = record_and_recognize_audio()
        print(voice_input)
        if voice_input in names:
            command_input = record_and_recognize_command()
            print(command_input)
            ################################################    УПРАВЛЕНИЕ ПОДСВЕТКЕОЙ
            if(command_input)=="включи подсветку":
                val = '0'
                ser.write(val.encode())
                play_voice_assistant_speech("включаю подсветку")
            if(command_input)=="выключи подсветку":
                val = '1'
                ser.write(val.encode())
                play_voice_assistant_speech("выключаю подсветку")
            ################################################    УПРАВЛЕНИЕ БОЛЬШИМ СВЕТОМ
            if(command_input)=="выключи свет": #
                val = '5'
                ser.write(val.encode())
                play_voice_assistant_speech("выключаю свет")
            if(command_input)=="включи свет":
                val = '4'
                ser.write(val.encode())
                play_voice_assistant_speech("включаю свет")
            #################################################   ЗАПРОС НА ВЛАЖНОСТЬ И ТЕМПЕРАТУРУ
            if(command_input) in call_pogoda:
                val = '3'
                hum = [0,0]
                temp = [0,0]
                pogoda_comment = ""
                ser.write(val.encode())
                hum_p = ser.read()
                hum_p = hum_p.decode("UTF-8")
                hum[0] = hum_p                   
                hum_p = ser.read()
                hum_p = hum_p.decode("UTF-8")
                hum[1] = hum_p
                hum_res = str(hum[0] + hum[1])
                temp_p = ser.read()
                temp_p = temp_p.decode("UTF-8")
                temp[0] = temp_p
                temp_p = ser.read()
                temp_p = temp_p.decode("UTF-8")
                temp[1] = temp_p
                temp_res = str(temp[0] + temp[1])
                pogoda = "Влажность воздуха " + hum_res + "%, а температура, " + temp_res + " градусов"
                play_voice_assistant_speech(pogoda)
            #################################################   ПОИСК В ВИКИПЕДИИ
            if "что такое" in str(command_input)  or "кто такой" in str(command_input): 
                search = str(command_input)
                search =  search[10:]
                answer = wikipedia.summary(search,sentences=2)
                play_voice_assistant_speech(answer)
            #################################################   БЛОКИРОВКА ПК ДОДЕЛАТЬ!!!
            #if(command_input) in call_lockpc:
            #    keyboard.press_and_release("windows+l")  

