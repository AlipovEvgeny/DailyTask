#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from test_task.modules.mods import *
from test_task.modules.mods import constants
from selenium.webdriver import Firefox as FWD
from selenium.webdriver import Chrome as CWD
from selenium.webdriver import Opera as OWD
from selenium.webdriver import Safari as SWD
import time


class TestOne(unittest.TestCase):
    def setUp(self):
        self.browser = FWD()  # запускать тесты в фаерфоксе, если нужно в другом браузере, то нужный раскоментить
        # self.browser = CWD()
        # self.browser = OWD()
        # self.browser = SWD()
        self.id_test = "0000001"  # ид теста
        self.name_test = "Листание рубрик"  # имя

    def test_run(self):
        self.browser.get(constants["web_site"])  # открыть url который в контантах
        media_field = self.browser.find_element_by_xpath(constants["media"])  # найт вкладку медиа
        media_field.click()  # кликнуть по ней
        time.sleep(1)  # слип чтобы не так быстро все кликалось
        culture_field = self.browser.find_element_by_xpath(constants["culture"])  # найти вкладку культура
        culture_field.click()
        time.sleep(1)
        video_field = self.browser.find_element_by_xpath(constants["video"])  # найти вкладку видео
        video_field.click()
        time.sleep(1)
        about_field = self.browser.find_element_by_xpath(constants["about_us"])  # вкладка "о Нас"
        about_field.click()
        time.sleep(1)

    def tearDown(self):
        self.browser.quit()  # выход из браузера

class TestTwo(unittest.TestCase):
    def setUp(self):
        self.browser = FWD()  # как и в первом, фаерфокс по умолчанию, нужный раскоментить
        # self.browser = CWD()#
        self.id_test = "0000002"  # ид теста
        self.name_test = "Подписка на рассылку"  # имя теста

    def test_run(self):
        self.browser.get(constants["web_site"])  # открыть браузер и перейти на нужный урл
        article_field = self.browser.find_element_by_class_name(constants["input_article"])  # найти поле для подписки
        checkbox = self.browser.find_element_by_class_name(constants["checkbox"])  # поле согласия обработки данных
        subscribe_field = self.browser.find_element_by_class_name(constants["subscribe_article"])  # поле подписаться
        article_field.send_keys(RandomMail.random_mail(self))  # вписать рандомно-сгенеренный имейл
        checkbox.click()  # кликнуть на согласие обработки данных
        subscribe_field.click()  # кликнуть на форму "Подписаться"
        time.sleep(5)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
