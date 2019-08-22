from selene.api import *
from selene.api import browser
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage
from src.pages.LkMainPage import LkMainPage
from src.model.action import Action
import allure


class Header(object):
    def __init__(self):
        self.login_button = s('a[data-autotest="login"]')
        self.register_button = s('a[data-autotest="registration"]')
        self.parters_link = s('.header__top-link')
        self.logo_link = s('.header__logo')
        self.user_name_button = s('.user-head__username')
        self.poapregion_block = s('.region-popup.js-region-popup.is-active')
        self.empty_popup_block = s('.region-popup.js-region-popup.is-active .simplebar-content')
        self.change_region_button = s('.city-select')

    def open_login_page(self):
        self.login_button.click()
        return LoginPage()

    def open_register_page(self):
        self.register_button.click()
        return RegisterPage()

    def open_lk(self):
        self.user_name_button.click()
        return LkMainPage()

    def change_region(self, region_id):
        region_name = Action().get_region_by_id(str(region_id))
        with allure.step('Нажимаем на ссылку для выбора региона'):
            self.change_region_button.click()
        with allure.step("Ожидаем появления попапа"):
            self.poapregion_block.should(be.visible)
        with allure.step('Кликаем на найденный регион {0}'.format(region_name)):
            s(by.link_text(region_name)).click()
        with allure.step('Проверяем что регион сменился'):
            self.change_region_button.should(have.exact_text(region_name))

