class User(object):

    def __init__(self, phone='', sms='', fio='', email='', password='', confirm_password='',
                 sex='', data_day='', data_month='', data_year='',  approve1=0, approve2=0):
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
