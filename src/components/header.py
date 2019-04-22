from selene.api import s
from selene.api import browser
from src.pages.LoginPage import LoginPage
from src.pages.RegisterPage import RegisterPage
from src.pages.LkMainPage import LkMainPage


class Header(object):
    def __init__(self):
        self.login_button = s('a[data-autotest="login"]')
        self.register_button = s('a[data-autotest="registration"]')
        self.parters_link = s('.header__top-link')
        self.logo_link = s('.header__logo')
        self.user_name_button = s('.user-head__username')
        self.locator_poapregion = '.region-popup.js-region-popup.is-active'  # css
        self.locator_empty_popup = '.region-popup.js-region-popup.is-active .simplebar-content'  # css

    def open_login_page(self):
        self.login_button.click()
        return LoginPage()

    def open_register_page(self):
        self.register_button.click()
        return RegisterPage()

    def open_lk(self):
        self.user_name_button.click()
        return LkMainPage()