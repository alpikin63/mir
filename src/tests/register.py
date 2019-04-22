from selene.api import *
from src.components.header import Header
import allure
from src.pages.LkMainPage import LkMainPage
from src.model.user import User
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage
import time

config.browser_name = 'chrome'


@allure.title('Првека регистрации существующего пользователя')
def test_step1_registred_number():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step("Проверка повления уведомления о использовании текущего номера"):
        RegisterPage().register_step1(
            User(phone='9771874093', approve1=1, approve2=1), browser.driver()).master_error.should(have.exact_text(
            'Такой телефон уже используется'))
    with allure.step('Проверка отсутствия перехода на второй шаг'):
        RegisterPage().code_input.should_not(be.visible)


@allure.title('Проверка регистрации при вводе некорректного номера')
def test_step1_uncorrect_number():
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Ввод номера несоответствующего маске'):
        RegisterPage().register_step1(
            User(phone='97718740', approve1=1, approve2=1), browser.driver()).phone_error.should(
            have.exact_text('Введите корректный номер телефона'))
    with allure.step('Проверка отсутствия перехода на второй шаг'):
        RegisterPage().code_input.should_not(be.visible)


@allure.title('Проверка регистрации при вводе пустого телефона')
def test_step1_empty_number():
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Ввод пустого номера'):
        RegisterPage().register_step1(
            User(phone='', approve1=1, approve2=1), browser.driver()).phone_error.should(
            have.exact_text('Введите корректный номер телефона'))
    with allure.step('Проверка отсутствия перехода на второй шаг'):
        RegisterPage().code_input.should_not(be.visible)


@allure.title('Проверка перехода на второй шаг при неотмеченных чекбоксах политики конфиденциальности')
def test_step1_empty_checkbox():
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Ввод корректного незарегистрированного номера 1й чекбокс не отмечен'):
        RegisterPage().register_step1(
            User(phone='9201239746', approve1=0, approve2=1), browser.driver())
    with allure.step('Проверка отсутствия перехода на второй шаг'):
        RegisterPage().code_input.should_not(be.visible)
    with allure.step("Ввод корректного незарегистрированного номера 2й чекбокс не отмечен"):
        RegisterPage().register_step1(
            User(phone='9201239746', approve1=0, approve2=1), browser.driver())
    with allure.step('Проверка отсутствия перехода на второй шаг'):
        RegisterPage().code_input.should_not(be.visible)

# def test_step1_deactivated_number();
# def test_step2_uncorrect_code():
# def test_step2_empty_code():
# def test_step3_empty_fieldes():
# def test_step3_uncorrect_email():
# def test_step3_differents_passwords():
# def test_step3_correct_registration():