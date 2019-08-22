from selene.api import *


class LkCards(object):
    def __init__(self):
        self.add_button = s('.lk-cards__add-btn')
        self.add_button_empty = s('.lk-cards__empty-btn')
        self.delete_button = s('.lk-card__delete-btn')
        self.pan = s('.lk-card__num')
        self.delete_popup_button = s('.lk-cards__popup-delete .btn.btn--small.btn--trsp-bg.mr-md-4.mr-2 + button')
        self.card_description_text = s('.lk-card__desc')

    def open_add_form(self):
        self.add_button.click()

    def delete_card(self):
        self.delete_button.click()
        self.delete_popup_button.click()




