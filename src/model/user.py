import random
import datetime
import locale


class User(object):

    def __init__(self, phone='', sms='', fio='', email='', password='', confirm_password='',
                 sex='', data_day='', data_month='', data_year='',  approve1=0, approve2=0, rand=False):
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

    def phone_generate(self):
        return random.randrange(1111111111,9999999999)

    def get_settings_data(self):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return datetime.date(
            int(self.data_year), int(self.data_month), int(self.data_day)).strftime(
            'X%d X%B X%Y').replace('X0','X').replace('X','')

    def get_settings_sex(self):
        if self.sex == 'male':
            return "мужской"
        else:
            return 'женский'

    def get_settings_phone(self):
        print(self.phone)
        phone = '+7 (' + str(self.phone)[0:3] + ') '+ str(self.phone)[3:6] + '-' + str(
            self.phone)[6:8]+'-'+ str(self.phone)[8:10]
        return phone

