#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random, string
import os
import time, datetime

# константы решил хранить в словаре
constants = {"web_site": "https://www.thisis.media/#media",
             "media": "//li[@id='anchor-media']",
             "culture": "//li[@id='anchor-culture']",
             "video": "//li[@id='anchor-video']",
             "about_us": "//li[@id='anchor-about-us']",
             "article_click": "preview-datalist-item preview-datalist-item__tag",
             "input_article": "subscribe-input",
             "subscribe_article": "subscribe-btn",
             "checkbox": "checkbox-label"}

# домены имейлов, которые будут случайно выбираться ии добавляться
email_domains = ("@gmail", "@yandex.ru", "@mail.ru",
                 "@inbox.ru", "@bk.ru", "@list.ru")


# этот класс генерирует и возвращает имейл
class RandomMail(object):
    def __init__(self):
        self.mail = None

    @staticmethod  # статикметод чтобы не создавать объект класса, а сразу использовать метод из класса
    def random_mail(self):
        random_range = random.randint(8, 12)  # рандомная длинна имейла, от 8 до 12, можно указать свою
        # следующая строка выбирает случайные символы из ASCII букв и случайные числа
        self.mail = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random_range))
        self.mail += random.choice(email_domains)  # выбирает и добавляет домен из email_domain
        print(self.mail)  # отпечатать получившийся email
        return self.mail  # вернуть email


class SetUpPreconditions(object):
    """Этот класс создает окружение для логирования тестов"""

    def __init__(self):
        self.current_dir = os.getcwd()  # текущая дирректория
        self.date_time = datetime.datetime.today().strftime("%Y%m%d")  # текущая дата
        self.path_to_new_dir = None

    def create_dir(self):
        """создать папку для логгов"""
        try:
            # папка будет называться вроде "Test 20171231"
            os.mkdir(self.current_dir + "\\Test {}".format(self.date_time))  # создать папку с именем текущей даты
        except OSError:
            print("Папка с таким именем уже существует")
        self.path_to_new_dir = (self.current_dir + "\\Test {}".format(self.date_time))  # узнать путь к созданной папке

    def create_files(self):
        """создает файлы для логов"""
        os.chdir(self.path_to_new_dir)  # сменить дирректорию
        file_loggs = open("logs.txt", "w")  # создать файл для логгов
        file_loggs.close()

    def report_logs(self, text):
        """эта функция записывает текст в файл с указанием текущего времени"""
        file_loggs = open(str(self.path_to_new_dir) + "\\logs.txt", "a")  # открыть файл на дозапись
        file_loggs.write(str(time.strftime("%H:%M:%S ")) + text + "\n")  # записать в файл текущее время + текст
        file_loggs.close()

    def archivation_dir(self):
        """добавляет файл в арзив"""
        # !ТОЛЬКО ДЛЯ ЛИНУКС СИСТЕМ!
        os.system("tar -cvf archive " + str(self.path_to_new_dir))

    def send_archive(self):
        """отправить архив """
        pass
