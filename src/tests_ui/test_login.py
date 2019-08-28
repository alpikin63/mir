from selene.api import *
from src.components.header import Header
import allure
from src.pages.LkMainPage import LkMainPage
from src.model.user import User
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage
from selenium import webdriver
import time

tru_user = User(phone='9771874093', password='Qwerty!23', fio='Test Cashback')
uncorrect_user = User(phone='9771874093', password='Qwerty!32', fio='Test Cashback!')
user_without_password = User(phone='9771874093', password='')
user_without_login = User(password='Qwerty123', phone='')


class TestLogin:
    def setup(self):
        browser.open_url('/')

    def teardown(self):
        browser.close()

    @allure.title('Проверка авторизации, существующим пользователемм')
    def test_login_correct(self):
        with allure.step('Переход на страницу авторизации'):
            Header().open_login_page().title_name.should(have.exact_text('Вход'))
        with allure.step('Ввод номера и пароля'):
            LoginPage().login(tru_user)
        with allure.step('Проверка авторизации пользователя'):
            Header().user_name_button.should(have.exact_text(tru_user.fio))
            Header().user_name_button.click()
            LkMainPage().banner_link.should_be(be.visible)

    @allure.title('Проверка авторизации существующего пользователя, без ввода пароля')
    def test_password_uncorrect(self):
        with allure.step('Переход на страницу авторизации'):
            Header().open_login_page().title_name.should(have.exact_text('Вход'))
        with allure.step('Ввод номера и пустого пароля'):
            LoginPage().login(user_without_password)
        with allure.step('Проверка валидации поля пароль'):
            LoginPage().input_error_blocks_password.should(be.visible)
            LoginPage().input_error_blocks[0].element(LoginPage().error_text).should(have.exact_text('Обязательное поле'))
        with allure.step('Проверка неавторизованности пользователя'):
            Header().user_name_button.should_not(be.enabled)
            browser.driver().refresh()
            Header().user_name_button.should_not(be.enabled)

    @allure.title('Проверка авторизации существующего пользователя, без ввода логина')
    def test_login_uncorrect(self):
        with allure.step('Переход на страницу авторизации'):
            Header().open_login_page().title_name.should(have.exact_text('Вход'))
        with allure.step('Ввод номера и пароля'):
            LoginPage().login(user_without_login)
        with allure.step('Проверка валидации поля Телефон'):
            LoginPage().input_error_blocks_login.should(be.visible)
            LoginPage().input_error_blocks[0].element(LoginPage().error_text).should(have.exact_text('Обязательное поле'))
        with allure.step('Проверка неавторизованности пользователя'):
            Header().user_name_button.should_not(be.enabled)
            browser.driver().refresh()
            Header().user_name_button.should_not(be.enabled)

    @allure.title('Проверка авторизации не существующего пользователя')
    def test_login_uncorrect_user(self):
        with allure.step('Переход на страницу авторизации'):
            Header().open_login_page().title_name.should(have.exact_text('Вход'))
        with allure.step('Ввод номера и пароля'):
            LoginPage().login(uncorrect_user)
        with allure.step('Проверка появления ошибки о неверном логине пароле'):
            LoginPage().back_error_text.should(be.visible)
            LoginPage().back_error_text.should(have.exact_text('Неверный номер телефона или пароль.'))
        with allure.step('Проверка неавторизованности пользователя'):
            Header().user_name_button.should_not(be.enabled)
            browser.driver().refresh()
            Header().user_name_button.should_not(be.enabled)

    @allure.title('Проверка авторизации при пустых логине и пароле')
    def test_login_password_empty(self):
        with allure.step('Переход на страницу авторизации'):
            Header().open_login_page().title_name.should(have.exact_text('Вход'))
        with allure.step('Ввод несуществующего номера и пароля'):
            LoginPage().login(User())
        with allure.step('Проверка валидации поля Телефон'):
            LoginPage().input_error_blocks[0].element(LoginPage().error_text).should(have.exact_text('Обязательное поле'))
        with allure.step('Проверка валидации поля Пароль'):
            LoginPage().input_error_blocks[1].element(LoginPage().error_text).should(have.exact_text('Обязательное поле'))
        with allure.step('Проверка неавторизованности пользователя'):
            Header().user_name_button.should_not(be.enabled)
            browser.driver().refresh()
            Header().user_name_button.should_not(be.enabled)

    @allure.title('Переход на страницу регистрации')
    def test_register_open(self):
        with allure.step('Переход на страницу авторизации'):
            Header().open_login_page().title_name.should(have.exact_text('Вход'))
        with allure.step('Нажатие на ссылку Регистрация'):
            LoginPage().register_link.click()
        with allure.step('Проверка перехода на страницу регистрации'):
            RegisterPage().title_text.should(have.exact_text("Регистрация"))


    # @allure.title('Проверка каптчи')
    # def test_login_uncorrect_captcha(self):
    #     browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
    #     with allure.step('Переход на страницу авторизации'):
    #         Header().open_login_page().title_name.should(have.exact_text('Вход'))
    #     with allure.step('Ввод несуществующего номера и пароля 1я попытка'):
    #         LoginPage().login(uncorrect_user)
    #     with allure.step('Ввод несуществующего номера и пароля 2я попытка'):
    #         LoginPage().login(uncorrect_user)
    #     with allure.step('Ввод несуществующего номера и пароля 3я попытка'):
    #         LoginPage().login(uncorrect_user)
    #     with allure.step('Проверка появления ошибки о неверном логине пароле'):
    #         LoginPage().back_error_text.should(be.visible)
    #         LoginPage().back_error_text.should(have.exact_text('Неверный номер телефона или пароль.'))
    #     with allure.step('Проверка появления каптчи'):
    #         LoginPage().captcha_block.should(be.visible)
    #     with allure.step('Проверка неавторизованности пользователя'):
    #         Header().user_name_button.should_not(be.enabled)
    #         browser.driver().refresh()
    #         Header().user_name_button.should_not(be.enabled)
