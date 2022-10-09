
import random
import webbrowser
import os
import speech_recognition
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands = {
    'commands': {
        'play_music': ['музыка', 'включить музыку', 'дискотека'],
        'open_yandex': ['яндекс', 'включить яндекс', 'запустить яндекс'],
        'open_mozilla': ['мозила', 'мазила', 'firefox', 'mozilla'],
        'open_vkontakte': ['вк', 'вконтакте', 'открыть vk'],
        'open_instagram': ['instagram', 'открыть instagram', 'инста'],
        'open_instagram_clever': ['клевер', 'открыть клевер', 'инстаграм клевер'],
        'power_off': ['выключить', 'выключить компьютер', 'выключение'],
        'nakrutka_instagram': ['накрутка', 'накрутка инстаграм', 'запустить накрутку'],
        'cls': ['очистка', 'очистить консоль', 'обнал'],
        'stop_firefox': ['остановка', 'остановить браузер', 'биглайк'],
        'start_vinchik': ['леонардо', 'дайвинчик', 'лайки'],
        "ctime": ['текущее время', 'сейчас времени', 'который час', 'время'],
    }
}


class Listener:
    def __int__(self):
        pass

    def listen_command(self):
        """Listen microphone"""
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
                split_query = query.split(' ')
                if len(split_query) <= 2:
                    print(query)
                    return query
        except speech_recognition.UnknownValueError:
            print("[log] Голос не распознан!")
        except speech_recognition.RequestError:
            print("[log] Неизвестная ошибка, проверьте интернет!")

    def play_music(self):
        """On music in catalog"""
        file_on_dir = 'C:\\Users\\kokos\\Music\\Аудио\\'
        files = os.listdir(file_on_dir)
        random_music = f'{file_on_dir}{random.choice(files)}'
        os.system(f'start {random_music}')

    def speak(self, what):
        """Tell text"""
        print(what)
        speak_engine = pyttsx3.init()
        speak_engine.say(what)
        speak_engine.runAndWait()
        speak_engine.stop()

    def ctime(self):
        """Time now"""
        now = datetime.datetime.now()
        self.speak("Сейчас " + str(now.hour) + ":" + str(now.minute))


    def open_yandex(self):
        os.system(f'start C:\\Users\\kokos\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe')

    def open_mozilla(self):
        os.system(f'cd C:\\Program Files\\Mozilla Firefox\\')
        os.system(f'start firefox.exe')

    def open_vkontakte(self):
        webbrowser.open_new_tab('https://vk.com/')

    def open_instagram(self):
        webbrowser.open_new_tab('https://www.instagram.com/')

    def open_instagram_clever(self):
        try:
            os.system('python C:\\Users\\kokos\\Desktop\\programing\\Python\\Bots\\VoicAsistent\\funstions\\clever.py')
        except:
            pass

    def power_off(self):
        os.system('shutdown -s')


    def nakrutka_instagram(self):
        os.system(r'python  C:\Users\kokos\Desktop\programing\Python\Bots\Instagramnakrytka\BigLike\RunFile.py')


    def cls(self):
        os.system(f'cls')


    def stop_firefox(self):
        os.system('taskkill /IM firefox.exe /T /F')


    def start_vinchik(self):
        os.system(r'python  C:\Users\kokos\Desktop\programing\Python\Bots\NotLionatdo.py')


def main():
    obj = Listener()
    i = 0
    while True:
        query = obj.listen_command()

        if i == 7:
            os.system(f'cls')
            i = 0
        i += 1
        for k, v in commands['commands'].items():
            if query in v:
                exec(f'obj.{k}()')


if __name__ == "__main__":
    main()
