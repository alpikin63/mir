from selene.api import *
import allure


class LkSettingsPage(object):
    def __init__(self):
        self.deactivate_button = s(".lk-settings__deact-btn")
        self.deactivate_password_input = s('[name="password-deact"]')
        self.deactivate_button_confirm = s('.lk-deact-popup__btns button[type="submit"]')
        self.byby_popup = s('.popup__inner.js-popup-inner')
        self.user_name_input = s('#username.lk-settings__input')
        self.user_birthday_text = s('.lk-settings__birth')
        self.user_phone_text = s('.lk-settings__tel')
        self.user_sex_text = s('.lk-settings__sex')
        self.user_email_input = s('#email.lk-settings__input')
        self.save_button = s('.lk-settings__row-value .btn.btn--small.btn--trsp-bg.mr-md-4.mr-2 + button')
        self.sucsess_msg = s('.master-message.is-success.is-active')
        self.change_phone_button = s('.lk-settings__tel + a')
        self.confirm_email_button = s('.lk-settings__email-approve-btn')
        self.confirm_email_popup_title = s('.popup__title')
        self.avatar_input = s('[type="file"]')
        self.avatar_popub_buttons = ss('.lk-popup-ava__footer button')
        self.master_errors_popup = s('.master-message')

    def deactivate_user(self, user):
        with allure.step('Нажатие на кнопку деактивации'):
            self.deactivate_button.click()
        with allure.step('Ввод пароля: %s'%user.password):
            self.deactivate_password_input.set(user.password)
        with allure.step('Нажатие кнопки подтверждения'):
            self.deactivate_button_confirm.click()
        with allure.step('Проверка появления прощального попапа'):
            self.byby_popup.should(be.visible)


