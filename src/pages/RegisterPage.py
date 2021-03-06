from selene.api import s
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selene.api import *
import allure
import time


class RegisterPage(object):
    def __init__(self):
        self.title_text = s('h1.reg__title')
        self.phone_input = s('input[id="tel"]')
        self.next_button = s('.reg__footer button')
        self.cancel_button = s('.reg__footer a')
        self.code_input = s('input[name="code"]')
        self.name_input = s('input[name="name"]')
        self.email_input = s('input[name="email"]')
        self.password_input = s('input[name="pass"]')
        self.confirm_password_input = s('input[name="pass_confirmation"]')
        self.data_day_select = s('.reg__form-select--day')
        self.data_month_select = s('.reg__form-select--month')
        self.data_year_select = s('.reg__form-select--year')
        self.male_radio = s('label[for="male"]')
        self.female_radio = s('label[for="male"]')
        self.checkbox1 = s('label[for="approve1"]')
        self.checkbox2 = s('label[for="approve2"]')
        self.phone_error = s('label[for="tel"]+div+span')
        self.code_error = s('label[for="code"]+div+span')
        self.name_error = s('label[for="name"]+div+span')
        self.email_error = s('label[for="email"]+div+span')
        self.password_error = s('label[for="pass"]+div+span')
        self.confirm_password_error = s('label[for="pass_confirmation"]+div+span')
        self.data_day_error = s('.reg__form-select--day .error-msg')
        self.data_month_error = s('.reg__form-select--month .error-msg')
        self.data_year_error = s('.reg__form-select--year .error-msg')
        self.submit = s('.reg__footer button')
        self.error_phone = s('.master-message .master-message__msg')
        self.master_error = s('.master-message.is-error.is-active')
        self.auth_back_error = s('.auth__master-error')
        self.sex_error = s('div.reg__form-block.reg__form-block--radio.form__group.mb-4 > div > span')
        self.welcome_button = s('.reg__success-btn')
        self.registered_user_step3_v2_text = s('[name="_method"] + div.row')

    def register_step1(self, user, driver):
        with allure.step('Ввод телефона: %s - переход на следующий шаг'%user.phone):
            self.phone_input.click()
            self.phone_input.send_keys(user.phone)
            if user.chekbox1 == 1:
                """Костыль для нажатия на чекбокс"""
                action = ActionChains(driver)
                action.move_to_element_with_offset(
                    driver.find_element_by_css_selector('label[for="approve1"]'), 20, 20).click().perform()
                """"""

            if user.chekbox2 == 1:
                self.checkbox2.click()
            self.next_button.click()
        return self

    def register_step2(self, user, driver):
        self.register_step1(user, driver)
        with allure.step('Ввод кода - переход на следующий шаг'):
            self.code_input.set(user.sms_code)
            self.next_button.click()
        return self

    def register_step3(self, user, driver):
        self.register_step2(user, driver)
        with allure.step('Заполнение данных формы'):

            with allure.step('Поле Фио: %s'%user.fio):
                self.name_input.set(user.fio)

            with allure.step('Поле email: %s'%user.email):
                self.email_input.set(user.email)

            with allure.step('Поле Пароль: %s'%user.password):
                self.password_input.set(user.password)

            with allure.step('Поле Повторение пароля: %s'%user.confirm_password):
                self.confirm_password_input.set(user.confirm_password)

            with allure.step('Поле Дата рождения'):

                with allure.step('Заполнение поля день: %s'%user.data_day):
                    self.data_day_select.click()
                    self.data_day_select.find(' .choices__item[data-value="' + user.data_day + '"]').click()

                with allure.step('Заполнение поля месяц: %s'%user.data_month):
                    self.data_month_select.click()
                    self.data_month_select.find(' .choices__item[data-value="' + user.data_month + '"]').click()

                with allure.step('Заполнение поля год: %s'%user.data_year):
                    self.data_year_select.click()
                    self.data_year_select.find(' .choices__item[data-value="' + user.data_year + '"]').click()

            with allure.step('Поле Пол: %s'%user.sex):
                if user.sex == 'male':
                    self.male_radio.click()
                elif user.sex == 'female':
                    self.female_radio.click()
            with allure.step('Нажатие кнопки Зарегестрироваться'):
                self.submit.click()
        return self

    def register_step3_already_register_v2(self, user, driver, cancel=False):
        self.register_step2(user, driver)
        with allure.step('Заполнение данных формы'):
            with allure.step('Поле Новый Пароль: %s'%user.password):
                self.password_input.set(user.password)

            with allure.step('Поле Повторение пароля: %s'%user.confirm_password):
                self.confirm_password_input.set(user.confirm_password)

            with allure.step('Проверка открытия формы смены пароля'):
                self.title_text.should(have.text('Задать пароль'))
                self.registered_user_step3_v2_text.should(have.text(
                    'Уважаемый клиент!\nРанее Вы регистрировались в Программе лояльности. Для восстановления доступа к личному кабинету задайте новый пароль.'))
            if(cancel):
                with allure.step('Нажатие кнопки Отмены'):
                    self.cancel_button.click()
            else:
                with allure.step('Нажатие кнопки Зарегестрироваться'):
                    self.next_button.click()
        return self

    def check_email(self, email):
        with allure.step("Ввод некорректного e-mail: %s"%email):
            self.email_input.set(email)
        with allure.step('Нажатие кнопки Зарегестрироваться'):
            self.submit.click()
        with allure.step('Проверка перехода на страницу успешной регистрации'):
            self.title_text.should_not(have.exact_text('Добро пожаловать!'))
        return self