import requests


class Vkc(object):
    def __init__(self):
        self.headers = {
            "Authorization": "Basic bG9naW5hcmVhOnBhc3NhcmVh", "Accept": "text/plain, application/json, text/json"}
        self.url = 'http://nspk.aeroidea.ru:83/api/v2/'

    def clients_by_id(self, user_id):
        response = requests.get(self.url+'clients/'+str(user_id), headers=self.headers)
        return response

    def clients_by_phone(self, user_phone):
        response = requests.get(self.url + 'clients/by-phone/' + str(user_phone), headers=self.headers)
        return response

    def clients_operation_by_id(self, user_id, **params):
        if params:
            url = self.url + "clients/"+str(user_id)+'/all-cards-operations?'
            for i in params:
                if i == 'fr':
                    url = url +i+'om'+'='+ str(params[i])+'&'
                else:
                    url = url = url + i+'='+str(params[i])+'&'
            url = url[:-1]
        else:
            url = self.url + "clients/" + str(user_id) + '/all-cards-operations'

        response = requests.get(url, headers=self.headers)
        return response

    def all_partners(self):
        response = requests.get(self.url+'partners', headers=self.headers)
        return response

    def partners_by_id(self, partner_id):
        response = requests.get(self.url+'partners/'+str(partner_id), headers=self.headers)
        return response

    def partner_actions(self, partner_id):
        response = requests.get(self.url+'partners/'+str(partner_id)+'/offers', headers=self.headers)
        return response

    def offer_by_id(self, offer_id):
        response = requests.get(self.url+'offers/'+str(offer_id), headers=self.headers)
        return response

    def offer_points(self, offer_id):
        response = requests.get(self.url+'offers/'+str(offer_id)+'/sales-points', headers=self.headers)
        return response

    def registration_status_by_pan(self, pan):
        response = requests.get(self.url+'card-registation-statuses/by-pan/'+str(pan), headers=self.headers)
        return response

    def registration_status_by_phone(self, phone):
        response = requests.get(self.url+'card-registation-statuses/by-phone/'+str(phone), headers=self.headers)
        return response
