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
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
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
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
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
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
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


@allure.title("Проверка ввода некоррекного кода из смс ")
def test_step2_uncorrect_code():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Ввод корректного номера'):
        RegisterPage().register_step2(
            User(phone='9201239746', approve1=1, approve2=1, sms='q123'), browser.driver()).code_error.should(
            have.exact_text('Введите не менее 4 символов'))
    with allure.step('Проверка отсутствия перехода на третий шаг'):
        RegisterPage().name_input.should_not(be.visible)


@allure.title("Проверка ввода пустого кода из смс ")
def test_step2_empty_code():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Ввод корректного номера'):
        RegisterPage().register_step2(
            User(phone='9201239746', approve1=1, approve2=1, sms=''), browser.driver()).code_error.should(
            have.exact_text('Обязательное поле'))
    with allure.step('Проверка отсутствия перехода на третий шаг'):
        RegisterPage().name_input.should_not(be.visible)


@allure.title("Регистрация при незаполненных полях на 3шаге")
def test_step3_empty_fieldes():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Ввод корректного номера'):
        RegisterPage().register_step3(
            User(phone='9201239747', approve1=1, approve2=1, sms='1111'), browser.driver())
    with allure.step("Проверка валидации поля ИМЯ"):
        RegisterPage().name_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля E-mail"):
        RegisterPage().email_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля Придумайте пароль"):
        RegisterPage().password_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля Повторите пароль"):
        RegisterPage().confirm_password_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля День"):
        RegisterPage().data_day_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля Месяц"):
        RegisterPage().data_month_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля Год"):
        RegisterPage().data_year_error.should(have.exact_text('Обязательное поле'))
    with allure.step("Проверка валидации поля Пол"):
        RegisterPage().sex_error.should(have.exact_text('Обязательное поле'))


@allure.title('Проверка ввода некорректного адреса почты')
def test_step3_uncorrect_email():
    browser.open_url('http://loginarea:passarea@nspk.aeroidea.ru')
    with allure.step('Переход на страницу регистрации'):
        Header().open_register_page().title_text.should(have.exact_text('Регистрация'))
    with allure.step('Корректно заполненные поля и невалидная почты'):
        RegisterPage().register_step3(
            User(phone='9201239742',
                 approve1=1, approve2=1, sms='1111', email="alpikin",
                 fio="test", data_day="4", data_month="10", data_year="1993", sex="male", password="123456Qa!",
                 confirm_password="123456Qa!"), browser.driver())
    with allure.step('Проверка валидации поля e-mail'):
        RegisterPage().email_error.should(have.exact_text('Введите корректный email'))

    with allure.step("Проверка отсутствие перехода на сраницу зарегистрированного пользователя"):
        RegisterPage().title_text.should_not(have.exact_text('Добро пожаловать!'))
    RegisterPage().check_email('alpikin@')
    RegisterPage().check_email('@alpikin')
    RegisterPage().check_email('asd@alpikin')
    RegisterPage().check_email('lpikin.ru')
    RegisterPage().check_email('@lpikin.ru')


# def test_step3_differents_passwords():
# def test_step3_correct_registration():
# def test_step1_deactivated_number();