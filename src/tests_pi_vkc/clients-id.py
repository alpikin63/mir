import requests


class Vkc(object):
    def __init__(self):
        self.headers = {
            "Authorization": "Basic bG9naW5hcmVhOnBhc3NhcmVh", "Accept": "text/plain, application/json, text/json"}
        self.url = 'http://nspk.aeroidea.ru:83/api/v2/'

    def clients_by_id(self, user_id):
        response = requests.get(self.url+'clients/'+str(user_id), headers=self.headers)
        return response.text

    def clients_by_phone(self, user_phone):
        response = requests.get(self.url + '/clients/by-phone/' + str(user_phone), headers=self.headers)
        return response.text

    def clients_operation_by_id(self, user_id, *args):
        if args:
            url = self.url + "/clients/"+str(user_id)+'/all-cards-operations'
            for i in args:
                url = url + i
        response = requests.get(self.url + '/clients/'+str(user_id)+'/all-cards-operations', headers=self.headers)
        return response.text


 Vkc().clients_operation_by_id(user_id=2, to="df")

