from selene.api import *


class LkCardsAddPage(object):
    def __init__(self):
        self.number_input = s('.lk-add-card__input')
        self.submit_button = s('.lk-add-card__form button.btn')
        self.sucsess_message = s('.lk-add-card__success-title')
        self.title_text = s('.lk-add-card__title')
        self.error_message = s('.lk-add-card__error')
        self.allcards_btn = s('.lk-add-card__success .btn')

    def add_card(self, number):
        self.number_input.set_value(number)
        self.submit_button.click()
