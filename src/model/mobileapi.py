import requests
import json


class Mp(object):
    def __init__(self, phone):

        self.url = 'http://nspk.aeroidea.ru:82/api/v4/'
        self.finger_print = 'c062a8addacadbdb0bda00399dabdb8a4f5702e9a024733c659a9d96c4810c74'
        self.sms_code = '1111'
        self.signature = 'Zj08rhmizoETd0oVOLbuED1Op5FaNL2pq7rOhUIcQvoqjfH/2hOXHq3HGApi6jxexI7uBwvcoAanp9Msqhjtwn8uzRMnG1LL32yXFgxOo++9XP6plLqM8aw0k7kFlW3p2efMi1HtheQG6HGpQ183Qwfqh9b4Fbz8OVY2hOO6DZ1E7k6AatE6pBrMWsezK2/280vJG+gK3VnVGyn9sSbrnelIMZaCbZK2fKF5RgexKDTLzrwVhc4bma5ZAsOF92zQlALD7YMVmNY1/qwyMS+vh6laQptbmK63Hq+hVgj9pzjS2TZ9zJvb0y6ZWpWWswdg29vlvW+zllwhwdkUH76Izg=='
        self.aplication_version = '0.1'
        self.acsses_token = ''
        self.refresh_token = ''
        self.phone = phone

    def verify_code_send(self):
        headers = {"X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json"}
        body = json.dumps({
            "phone": self.phone,
            "deviceInfo": {
                "model": "Xiaomi Redmi 5 Plus",
                "uuid": "b3f9e56c5ce771d0",
                "systemName": "Android",
                "systemVersion": "8.1.0",
                "name": "Xiaomi Redmi 5 Plus",
                "publicKey": "{{publicKey}}"
            }
        })
        response = requests.post(url=self.url + 'auth/new-verification-code', data=body, headers=headers)
        return response

    def verify(self):
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json", "signature": self.signature}
        body = json.dumps({"phone": self.phone, "verificationCode": self.sms_code})
        response = requests.post(url=self.url + 'auth/verify', data=body, headers=headers)
        return response

    def auth_policy(self):
        headers = {
                "X-Device-Fingerprint": self.finger_print, "Accept": "text/plain, application/json, text/json",
                "X-Application-Version": self.aplication_version}
        response = requests.get(url=self.url + 'auth/policy', headers=headers)
        return response

    def auth(self):
        self.verify_code_send()
        first_resp = self.verify()
        if(first_resp.status_code == 401):
            self.verify_code_send()
            second_resp = self.verify()
            self.acsses_token = json.loads(second_resp.text)['accessToken']
            self.refresh_token = json.loads(second_resp.text)['refreshToken']
        else:
            self.acsses_token = json.loads(first_resp.text)['accessToken']
            self.refresh_token = json.loads(first_resp.text)['refreshToken']

    def profile(self):
        self.auth()
        headers = {
                "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
                "X-Access-Token": self.acsses_token, "X-Application-Version": self.aplication_version}
        response = requests.get(url=self.url + 'profile', headers=headers)
        return response

    def featured_companies_by_region(self, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token":  self.acsses_token, "X-Application-Version": self.aplication_version}
        response = requests.get(url=self.url + 'featured-companies/by-region/' + str(regionId), headers=headers)
        return response
    
    def companies_by_region(self, regionId, params):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'companies/by-region/' + str(regionId), headers=headers, params=params)
        return response
    
    def company_details(self, companyId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'company-details/' + str(companyId), headers=headers)
        return response

    def regions(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'regions', headers=headers)
        return response

    def top_offers_by_region(self, regionId, params):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'top-offers/by-region/'+str(regionId), headers=headers, params=params)
        return response

    def offers_by_region(self, regionId, params):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'offers/by-region/' + str(regionId), headers=headers, params=params)
        return response

    def offer_details(self, offerId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'offer-details/' + str(offerId), headers=headers)
        return response

    def offer_sets_by_region(self, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'offer-sets/by-region/' + str(regionId), headers=headers)
        return response

    def offer_set_offerSetId_in_region(self, offerSetId, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(
            url=self.url + 'offer-set/' + str(offerSetId) + '/in-region/' + str(regionId), headers=headers)
        return response

    def offer_categories_by_region(self, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Accept": "text/plain, application/json, text/json",
            "X-Access-Token": self.acsses_token, }
        response = requests.get(url=self.url + 'offer-categories/by-region/' + str(regionId), headers=headers)
        return response

    def top_offer_categories_by_region(self, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token, "X-Application-Version": self.aplication_version}
        response = requests.get(url=self.url + 'top-offer-categories/by-region/' + str(regionId), headers=headers)
        return response

    def offers_map_by_region(self, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'offers-map/by-region/' + str(regionId), headers=headers)
        return response

    def profile_confirm_policy(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print,
            "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        body = json.dumps({"pdnPolicyConfirmed": True, "offerConfirmed": True, "licenceConfirmed": True})
        response = requests.post(url=self.url + 'profile/confirm-policy', headers=headers, data=body)
        return response

    def auth_refresh_token(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Refresh-Token": self.refresh_token}
        body = json.dumps({"signature": self.signature})
        response = requests.post(url=self.url + 'auth/refresh-token', headers=headers, data=body)
        return response
    
    def auth_logout(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.post(url=self.url + 'auth/logout', headers=headers)
        return response
    
    def profile_update_region(self, regionId):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        body = json.dumps({"regionId": regionId})
        response = requests.post(url=self.url + 'profile/update-region', headers=headers, data=body)
        return response

    def profile_cards(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'profile/cards', headers=headers)
        return response

    def profile_card_binding_info(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'profile/card-binding-info', headers=headers)
        return response

    def profile_user_chat_profile(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'profile/user-chat-profile', headers=headers)
        return response

    def profile_cashback(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'profile/cashback', headers=headers)
        return response

    def profile_cashback_operations(self, params):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'profile/cashback-operations', headers=headers, params=params)
        return response

    def profile_change_phone_send_code(self, phone):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        body = json.dumps({"phone": phone})
        response = requests.post(url=self.url + 'profile/change-phone/send-code', data=body, headers=headers)
        return response

    def profile_change_phone_confirm_code(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Access-Token": self.acsses_token}
        body = json.dumps({"phone": self.phone, "verificationCode": self.sms_code})
        response = requests.post(url=self.url + 'profile/change-phone/confirm-code', data=body, headers=headers)
        print(response.json())
        return response

    def profile_update(self, body):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        body = json.dumps(body)
        response = requests.post(url=self.url + 'profile/update', data=body, headers=headers)
        return response

    def region_find_by_coordinates(self, lt, ln):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        params = {"latitude": lt, "longitude": ln}
        response = requests.get(url=self.url + 'region/find-by-coordinates', headers=headers, params=params)
        return response

    def profile_bind_card(self):
        pass

    def profile_bind_card_certs_chain(self):
        self.auth()
        headers = {
            "X-Device-Fingerprint": self.finger_print, "Content-Type": "application/json",
            "X-Application-Version": self.aplication_version, "X-Access-Token": self.acsses_token}
        response = requests.get(url=self.url + 'profile/bind-card/certs-chain', headers=headers)
        return response

