from selene.api import *
import time


class LkMenu(object):
    def __init__(self):
        self.main_link = s(by.link_text('Главная'))
        self.cashback_link = s(by.link_text('Мой кэшбэк'))
        self.cards_link = s(by.link_text('Мои карты'))
        self.settings_link = s(by.link_text('Настройки'))
        self.favorit_link = s(by.link_text('Избранное'))
        self.exit_link = s('.lk-user__btn')
        self.name_text = s('.lk-user__name')
        self.avatar_image = s('.lk-user__ava')

    def exit(self):
        self.exit_link.click()
        return self

    def open_settings(self):
        time.sleep(3)
        self.settings_link.click()
        return self

    def open_main(self):
        self.main_link.click()
        return self

    def open_cards(self):
        self.cards_link.click()
        return self

    def open_favorite(self):
        self.favorit_link.click()

    def open_cashback(self):
        self.cashback_link.click()
        return self