import random
import datetime
import locale
import requests
import json


class User(object):

    def __init__(self, phone='', sms='1111', fio='test', email='test@email.ru', password='Qwerty!23',
                 confirm_password='', sex='', data_day='', data_month='', data_year='',  approve1=0,
                 approve2=0, rand=False):

        self.phone = phone
        self.sms_code = sms
        self.fio = fio
        self.email = email
        self.password = password
        self.sex = sex
        self.data_day = data_day
        self.data_month = data_month
        self.data_year = data_year
        self.chekbox1 = approve1
        self.chekbox2 = approve2
        self.confirm_password = confirm_password
        if rand:
            self.phone = self.phone_generate()
        self.api_url = 'http://nspk.aeroidea.ru/api/'

    def phone_generate(self):
        return random.randrange(1111111111, 9999999999)

    def get_settings_data(self):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return str(datetime.date(
            int(self.data_year), int(self.data_month), int(self.data_day)).strftime(
            'X%d X%B X%Y').replace('X0', 'X').replace('X', ''))

    def get_settings_sex(self):
        if self.sex == 'male':
            return "мужской"
        else:
            return 'женский'

    def get_settings_phone(self):
        phone = '+7 (' + str(self.phone)[0:3] + ') ' + str(self.phone)[3:6] + '-' + str(
            self.phone)[6:8]+'-' + str(self.phone)[8:10]
        return phone

    def create_user_api(self):
        headers = {
            "Content-Type": "application/json", "Authorization": "Basic bG9naW5hcmVhOnBhc3NhcmVh"
        }
        body_send = json.dumps({"phoneNumber": self.phone, "scopes": ["register-user", "reset-password"]})
        resp = requests.post(url=self.api_url+'v2/send-code', data=body_send, headers=headers).text
        print(resp)
        session_code = json.loads(resp)['sessionId']
        body_veryfy = json.dumps({"code": self.sms_code, "sessionId": session_code})
        token = json.loads(
            requests.post(url=self.api_url+'v1/verify-code', data=body_veryfy, headers=headers).text)['token']
        body = json.dumps({
            'phoneNumber': self.phone,
            'password': self.password,
            'name': self.fio,
            'email': 'test@mail.ru'
        })
        headers_reg = {
            "Content-Type": "application/json", "Authorization": "Bearer "+token
        }
        requests.post(url=self.api_url+'v1/users', data=body, headers=headers_reg)

        return self
