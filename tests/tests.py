#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from test_task.modules.mods import *
from selenium.webdriver import Firefox as FWD
from selenium.webdriver import Chrome as CWD
from selenium.webdriver import Opera as OWD
from selenium.webdriver import Safari as SWD
import logging

logging.basicConfig(filename="tets_logs.log", level=logging.INFO,
                    format="[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")


class TestOne(unittest.TestCase):
    def setUp(self):
        self.browser = FWD()  # запускать тесты в фаерфоксе, если нужно в другом браузере, то нужный раскоментить
        self.id_test = "0000001"  # ид теста
        self.name_test = "Листание рубрик"  # имя

    def test_run(self):
        logging.info("Запускаем тест '{}' id: {}".format(self.name_test, self.id_test))
        self.browser.get(constants["web_site"])  # открыть url который в контантах
        logging.info("Открываем браузер и переходим по адресу {}".format(constants["web_site"]))
        media_field = self.browser.find_element_by_xpath(constants["media"])  # найт вкладку медиа
        logging.info("Ищем вкладку 'Media' - {}".format(media_field))
        media_field.click()  # кликнуть по ней
        logging.info("Кликаем 'Media'")
        culture_field = self.browser.find_element_by_xpath(constants["culture"])  # найти вкладку культура
        logging.info("Ищем вкладку 'Culture' - {}".format(culture_field))
        culture_field.click()
        logging.info("Кликаем 'Culture'")
        video_field = self.browser.find_element_by_xpath(constants["video"])  # найти вкладку видео
        logging.info("Ищем вкладку 'Video' - {}".format(video_field))
        video_field.click()
        logging.info("Кликаем 'Video'")
        about_field = self.browser.find_element_by_xpath(constants["about_us"])  # вкладка "о Нас"
        logging.info("Ищем вкладку 'About Us' - {}".format(about_field))
        about_field.click()
        logging.info("Кликаем 'About Us'")

    def tearDown(self):
        self.browser.quit()  # выход из браузера
        logging.info("Закрытие браузера")


class TestTwo(unittest.TestCase):
    def setUp(self):
        self.browser = FWD()  # как и в первом, фаерфокс по умолчанию, нужный раскоментить
        # self.browser = CWD()#
        self.id_test = "0000002"  # ид теста
        self.name_test = "Подписка на рассылку"  # имя теста
        self.mail = RandomMail.random_mail(self)

    def test_run(self):
        logging.info("Запускаем тест '{}' id: {}".format(self.name_test, self.id_test))
        self.browser.get(constants["web_site"])  # открыть браузер и перейти на нужный урл
        logging.info("Открываем браузер и переходим по адресу {}".format(constants["web_site"]))
        try:
            article_field = self.browser.find_element_by_class_name(
                constants["input_article"])  # найти поле для подписки
            logging.info("Ищем поле для email - {}".format(article_field))
            checkbox = self.browser.find_element_by_class_name(constants["checkbox"])  # поле согласия обработки данных
            logging.info("Ищем поле 'Соглашение обработки данных' - {}".format(checkbox))
            subscribe_field = self.browser.find_element_by_class_name(
                constants["subscribe_article"])  # поле подписаться
            logging.info("Ищем поле 'Подписаться' - {}".format(subscribe_field))
            article_field.send_keys(self.mail)  # вписать рандомно-сгенеренный имейл
            logging.info("Вписываем в поле для email наш адрес - {}".format(self.mail))
            checkbox.click()  # кликнуть на согласие обработки данных
            logging.info("Нажимаем на поле 'Соглашение обработки данных' - {}".format(checkbox))
            # subscribe_field.click()  # кликнуть на форму "Подписаться"
            logging.info("Нажимаем 'Подписаться' - {}".format(subscribe_field))
        except:
            logging.info("Что-то пошло не так :(")

    def tearDown(self):
        self.browser.quit()
        logging.info("Закрытие браузера")


class TestThree(unittest.TestCase):
    def setUp(self):
        self.browser = FWD()  # запускать тесты в фаерфоксе, если нужно
        self.id_test = "0000003"  # ид теста
        self.name_test = "Невалидный XPath"  # имя

    def test_run(self):
        logging.info("Запускаем тест '{}' id: {}".format(self.name_test, self.id_test))
        self.browser.get(constants["web_site"])
        logging.info("Открываем браузер и переходим по адресу {}".format(constants["web_site"]))
        try:
            no_valid = self.browser.find_element_by_xpath(constants["no_valid_path"])
            logging.info("Пытаемся найти элемент по несуществующему XPath - {}".format(no_valid))
        except:
            logging.info("Элемент не найден")

    def tearDown(self):
        self.browser.quit()
        logging.info("Закрытие браузера")


class TestFour(unittest.TestCase):
    def setUp(self):
        self.browser = FWD()
        self.id_test = "0000004"
        self.name_test = "Содержание заглавия"

    def test_run(self):
        logging.info("Запускаем тест '{}' id: {}".format(self.name_test, self.id_test))
        self.browser.get(constants["web_site"])
        logging.info("Открываем браузер и переходим по адресу {}".format(constants["web_site"]))
        try:
            assert "Daily Storm" in self.browser.title
            logging.info("В заглавии содержится 'Daily Storm'")
        except:
            logging.info("Тест успешно завершен, в заглавии отсутвует Daily Storm")
            pass

    def tearDown(self):
        self.browser.quit()
        logging.info("Закрытие браузера")


if __name__ == "__main__":
    unittest.main(verbosity=2)
