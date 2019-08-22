from selene.api import *
from src.components.header import Header
import allure
from src.components.lk_menu import LkMenu
from src.pages.LkSettingsPage import LkSettingsPage
from src.pages.ChangePhonePage import ChangePhonePage
from src.model.user import User
from src.pages.LoginPage import LoginPage
from src.model.card import Card
import random
import string
import pytest
import os
import time

tru_user = User(phone='3777777777', password='Qwerty!23', fio='test')


class TestSettingsLk:

    def setup(self):
        tru_user.create_user_api()
        browser.open_url('/')
        Header().open_login_page()
        LoginPage().login(tru_user)

    def teardown(self):
        browser.close()

    def test_change_name(self):
        LkMenu().open_settings()
        test_name = "autotestname" + ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
        LkSettingsPage().user_name_input.set_value(test_name)
        LkSettingsPage().save_button.click()
        LkSettingsPage().sucsess_msg.should(be.visible)
        browser.driver().refresh()
        assert LkSettingsPage().user_name_input.get_attribute('value') == test_name

    @pytest.mark.skip(reason="Bag")
    def test_change_number(self):
        LkMenu().open_settings()
        LkSettingsPage().change_phone_button.click()
        phone = User().phone_generate()
        phone_text = '+7 (' + str(phone)[0:3] + ') ' + str(phone)[3:6] + '-' + str(phone)[6:8]+'-' + str(phone)[8:10]
        ChangePhonePage().change_phone(user=tru_user, phone=phone).user_phone_text.should(have.text(phone_text))
        LkSettingsPage().change_phone_button.click()
        ChangePhonePage().change_phone(user=tru_user, phone=tru_user.phone)

    def test_change_email(self):
        LkMenu().open_settings()
        random_email = "autotestemail" + ''.join(random.choice(string.ascii_uppercase) for _ in range(10)) + "@mail.ru"
        LkSettingsPage().user_email_input.set_value(random_email)
        LkSettingsPage().save_button.click()
        LkSettingsPage().sucsess_msg.should(be.visible)
        browser.driver().refresh()
        assert LkSettingsPage().user_email_input.get_attribute('value') == random_email

    def test_confirm_email(self):
        LkMenu().open_settings()
        LkSettingsPage().confirm_email_button.click()
        LkSettingsPage().confirm_email_popup_title.should(be.visible)
        LkSettingsPage().confirm_email_popup_title.should(have.text('Проверьте ваш e-mail'))

    def test_change_avatar(self):
        LkMenu().open_settings()
        locator = '[type="file"]'
        LkSettingsPage().avatar_input.should(be.enabled)
        browser.execute_script(script="document.querySelector('"+locator+"').style.width = '1px';")
        browser.execute_script(script="document.querySelector('"+locator+"').style.height = '1px';")
        browser.execute_script(script="document.querySelector('"+locator+"').style.display = 'block';")
        LkSettingsPage().avatar_input.send_keys(os.getcwd() + '\MilfordSound.jpg')
        LkSettingsPage().avatar_popub_buttons[1].click()
        LkSettingsPage().master_errors_popup.should(have.exact_text('Данные успешно обновлены'))
        LkSettingsPage().save_button.click()






