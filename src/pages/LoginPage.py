from selene.api import s
from selene.api import ss
from src.pages.LkMainPage import LkMainPage
import allure


class LoginPage(object):
    def __init__(self):
        self.password_input = s('[name="pass"]')
        self.login_button = s('.auth__submit')
        self.telephon_input = s('#tel')
        self.password_eye_button = s('#pass+button')
        self.fogott_password_link = s('.auth__pass-link')
        self.register_link = s('.auth__footer a')
        self.title_name = s('h1')
        self.input_error_blocks_login = ss('.input-block.has-error')[0].s('#tel')
        self.input_error_blocks_password = ss('.input-block.has-error')[0].s('#pass')
        self.input_error_blocks = ss('.input-block.has-error')
        self.error_text = 'span'
        self.back_error_text = s('.auth__master-error')
        self.captcha_block = s('auth__captcha')

    def login(self, user):
        with allure.step("Ввод телефона %s"%user.phone):
            self.telephon_input.set(user.phone)
        with allure.step('Ввод пароля %s'%user.password):
            self.password_input.set(user.password)
        with allure.step('Нажатие кнопки "Войти" %s'%self.login_button.__str__()):
            self.login_button.click()
        return LkMainPage()