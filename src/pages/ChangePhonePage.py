from selene.api import *
from src.components.lk_menu import LkMenu
from src.pages.LkSettingsPage import LkSettingsPage


class ChangePhonePage(object):
    def __init__(self):
        self.number_input = s('[name="new_tel"]')
        self.password_input = s('[name="pass"]')
        self.next_button = s('.main button[type="submit"]')
        self.sms_input = s('[name="code"]')

    def change_phone(self, user, phone):
        self.number_input.set_value(phone)
        self.password_input.set_value(user.password)
        self.next_button.click()
        self.sms_input.set_value('1111')
        self.next_button.click()
        LkMenu().open_settings()
        return LkSettingsPage()

