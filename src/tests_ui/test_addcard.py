from selene.api import *
from src.components.header import Header
import allure
from src.components.lk_menu import LkMenu
from src.pages.LkCards import LkCards
from src.pages.LkCardsAddPage import LkCardsAddPage
from src.model.user import User
from src.pages.LoginPage import LoginPage
from src.model.card import Card


tru_user = User(phone='3777777777', password='Qwerty!23')
card = Card(number='2202112288880805', pan='220211******0805')
card_unregistry = Card(number='2202333311111139', pan='220233******1139')

@allure.suite('Добавление карты')
@allure.sub_suite('Личный кабинет')
@allure.parent_suite('ФБ Личный кабинет')
class TestAddCard:

    def setup(self):
        tru_user.create_user_api()
        browser.open_url('/')
        Header().open_login_page()
        LoginPage().login(tru_user)

    def teardown(self):
        browser.close()

    @allure.title('Привязка корректной карты')
    def test_add_correctCard(self):
        LkMenu().open_cards()
        LkCards().add_button_empty.click()
        LkCardsAddPage().title_text.should(have.text('Привязка карты'))
        LkCardsAddPage().add_card(card.number)
        LkCardsAddPage().sucsess_message.should(have.text('Карта успешно привязана!'))
        LkCardsAddPage().allcards_btn.click()
        LkCards().pan.should(have.text(card.pan))
        LkCards().delete_button.click()
        LkCards().delete_popup_button.click()
        LkCards().add_button_empty.should(be.visible)

    @allure.title('Привязка unregistry карты')
    def test_add_unregistryCard(self):
        LkMenu().open_cards()
        LkCards().add_button_empty.click()
        LkCardsAddPage().title_text.should(have.text('Привязка карты'))
        LkCardsAddPage().add_card(card_unregistry.number)
        LkCardsAddPage().sucsess_message.should(have.text('Карта успешно привязана!'))
        LkCardsAddPage().allcards_btn.click()
        LkCards().pan.should(have.text(card_unregistry.pan))
        LkCards().card_description_text.should(have.text('Карта неактивна. Пожалуйста, обратитесь в поддержку'))
        LkCards().delete_button.click()
        LkCards().delete_popup_button.click()
        LkCards().add_button_empty.should(be.visible)

    @allure.title('Повторная привязка карты')
    def test_add_409(self):
        LkMenu().open_cards()
        LkCards().add_button_empty.click()
        LkCardsAddPage().title_text.should(have.text('Привязка карты'))
        LkCardsAddPage().add_card(card_unregistry.number)
        LkCardsAddPage().sucsess_message.should(have.text('Карта успешно привязана!'))
        LkCardsAddPage().allcards_btn.click()
        LkCards().add_button.click()
        LkCardsAddPage().add_card(card_unregistry.number)
        LkCardsAddPage().error_message.should(have.text('Ваша карта уже зарегистрирована в программе лояльности.'))
        LkMenu().open_cards()
        LkCards().delete_button.click()
        LkCards().delete_popup_button.click()
        LkCards().add_button_empty.should(be.visible)





