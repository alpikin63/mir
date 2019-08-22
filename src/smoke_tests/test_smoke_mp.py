from src.model.mobileapi import Mp
import pytest
import random

user = '79999999991'
region = 14
company = 22043
offer = 22064
offer_set = 1
change_phone = str(random.randrange(1111111111, 9999999999))
change_phone_user =  str(random.randrange(1111111111, 9999999999))


def test_verify_code_send():
    assert Mp(user).verify_code_send().status_code == 200


def test_verify():
    assert Mp(user).verify().status_code == 200


def test_auth_policy():
    assert Mp(user).auth_policy().status_code == 200


def test_profile():
    assert Mp(user).profile().status_code == 200


def test_featured_companies_by_region():
    assert Mp(user).featured_companies_by_region(region).status_code == 200


def test_companies_by_region():
    params = {}
    assert Mp(user).companies_by_region(params=params, regionId=region).status_code == 200


def test_company_details():
    assert Mp(user).company_details(companyId=company).status_code == 200


def test_regions():
    assert Mp(user).regions().status_code == 200


def test_top_offers_by_region():
    params = {}
    assert Mp(user).top_offers_by_region(regionId=region, params=params).status_code == 200


def test_offers_by_region():
    params = {}
    assert Mp(user).offers_by_region(regionId=region, params=params).status_code == 200


def test_offer_details():
    assert Mp(user).offer_details(offerId=offer).status_code == 200


def test_offer_sets_by_region():
    assert Mp(user).offer_sets_by_region(regionId=region).status_code == 200


def test_offer_set_offerSetId_in_region():
    assert Mp(user).offer_set_offerSetId_in_region(offerSetId=offer_set, regionId=region).status_code == 200


def test_offer_categories_by_region():
    assert Mp(user).offer_categories_by_region(regionId=region).status_code == 200


def test_top_offer_categories_by_region():
    assert Mp(user).top_offer_categories_by_region(regionId=region).status_code == 200


def test_offers_map_by_region():
    assert Mp(user).offers_map_by_region(regionId=region).status_code == 200


def test_profile_confirm_policy():
    assert Mp('79993814599').profile_confirm_policy().status_code == 200


def test_auth_refresh_token():
    assert Mp(user).auth_refresh_token().status_code == 200


def test_auth_logout():
    assert Mp(user).auth_logout().status_code == 200


def test_profile_update_region():
    assert Mp(user).profile_update_region(regionId=region).status_code == 200


def test_profile_cards():
    assert Mp(user).profile_cards().status_code == 200


def test_profile_card_binding_info():
    assert Mp(user).profile_card_binding_info().status_code == 200


def test_profile_user_chat_profile():
    assert Mp(user).profile_user_chat_profile().status_code == 200


def test_profile_cashback():
    assert Mp(user).profile_cashback().status_code == 200


def test_profile_cashback_operations():
    params = {}
    assert Mp(user).profile_cashback_operations(params=params).status_code == 200


def test_profile_change_phone_send_code():
    assert Mp(user).profile_change_phone_send_code(phone=change_phone).status_code == 200


# def test_profile_change_phone_confirm_code():
#     body = {
#         "name": "Test",
#         "sex": 1,
#         "email": "test@test.test",
#         "birthDate": "2000-02-02"
#     }
#     Mp(change_phone_user).profile_update(body=body).json()
#     print(Mp(change_phone_user).profile_change_phone_send_code(phone=change_phone).json())
#     assert Mp(change_phone_user).profile_change_phone_confirm_code().status_code == 200


def test_profile_update():
    body = {
        "name": "Test",
        "sex": 1,
        "email": "test@test.test",
        "birthDate": "2000-02-02"
    }
    assert Mp(user).profile_update(body=body).status_code == 200


def test_region_find_by_coordinates():
    lt = '14.234'
    ln = '15,342'
    assert Mp(user).region_find_by_coordinates(ln=ln, lt=lt).status_code == 200


def test_profile_bind_card():
    pass


def test_profile_bind_card_certs_chain():
    pass
