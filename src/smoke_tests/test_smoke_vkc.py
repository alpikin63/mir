from src.model.vkc import Vkc
import json
import jsonschema
from jsonschema import validate
client_id = '2'
client_phone = '79771874093'
partner_id = '22043'
offer_id = '22058'
card_pan = '220211XXXXXX0007'


def test_clients_by_id():
    response = Vkc().clients_by_id(user_id=client_id)
    assert response.status_code == 200


def test_clients_by_phone():
    response = Vkc().clients_by_phone(user_phone=client_phone)
    assert response.status_code == 200


def test_clients_operation_by_id():
    response = Vkc().clients_operation_by_id(
        user_id=client_id, fr='2018-01-01T00:00:00Z', to='2020-01-01T00:00:00Z', page='1', pageSise="20")
    assert response.status_code == 200


def test_all_partners():
    response = Vkc().all_partners()
    assert response.status_code == 200


def test_partners_by_id():
    response = Vkc().partners_by_id(partner_id=partner_id)
    assert response.status_code == 200


def test_partner_actions():
    response = Vkc().partner_actions(partner_id=partner_id)
    assert response.status_code == 200


def test_offer_by_id():
    response = Vkc().offer_by_id(offer_id=offer_id)
    assert response.status_code == 200


def test_offer_points():
    response = Vkc().offer_points(offer_id=offer_id)
    assert response.status_code == 200


def test_registration_status_by_pan():
    response = Vkc().registration_status_by_pan(pan=card_pan)
    assert response.status_code == 200


def test_registration_status_by_phone():
    response = Vkc().registration_status_by_phone(phone=client_phone)
    assert response.status_code == 200

