from selene.api import *
import allure

class LkSettingsPage(object):
    def __init__(self):
        self.deactivate_button = s(".lk-settings__deact-btn")
        self.deactivate_password_input=s('[name="password-deact"]')
        self.deactivate_button_confirm =s('.lk-deact-popup__btns button[type="submit"]')
        self.byby_popup = s('.popup__inner.js-popup-inner')
        self.user_name_input = s('#username.lk-settings__input')
        self.user_birthday_text = s('.lk-settings__birth')
        self.user_phone_text = s('.lk-settings__tel')
        self.user_sex_text = s('.lk-settings__sex')
        self.user_email_input = s('#email.lk-settings__input')

    def deactivate_user(self, user):
        with allure.step('Нажатие на кнопку деактивации'):
            self.deactivate_button.click()
        with allure.step('Ввод пароля: %s'%user.password):
            self.deactivate_password_input.set(user.password)
        with allure.step('Нажатие кнопки подтверждения'):
            self.deactivate_button_confirm.click()
        with allure.step('Проверка появления прощального попапа'):
            self.byby_popup.should(be.visible)


