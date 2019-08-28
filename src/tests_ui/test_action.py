from selene.api import *
from src.model.action import Action
import random
from src.components.header import Header
import allure


@allure.suite('Каталог')
@allure.sub_suite('Каталог')
@allure.parent_suite('ФБ каталог')
class TestAction:

    actions = Action().serach_active_actions()
    action = random.choice(actions)

    def setup(self):
        browser.open_url('/promo')

    def teardown(self):
        browser.close()

    @allure.title('Название теста')
    def test_action_visibilble_in_region(self):
        regions = Action().get_actions_regions(action_id=self.action['id'])
        for region in regions:
            Header().change_region(region_id=region)
            allure.attach.file(source=browser.take_screenshot(),
                               attachment_type=allure.attachment_type.PNG,
                               name='test')
            s('[data-id="'+str(self.action['id'])+'"]').should(be.visible)

    @allure.title('')
    def test_action_notvisibilble_in_region(self):
        regions = Action().get_actions_regions(action_id=self.action['id'])
        for region in regions:
            Header().change_region(region_id=region)
            allure.attach.file(source=browser.take_screenshot(),
                               attachment_type=allure.attachment_type.PNG,
                               name='test')
            s('[data-id="'+str(self.action['id'])+'"]').should(be.visible)

