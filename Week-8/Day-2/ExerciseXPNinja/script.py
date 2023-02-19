
class Phone:

    def __init__(self, number):
        self.phone_number = number
        self.call_history = []

    def call(self, another_phone):
        call_str = f'{another_phone.phone_number} calls to {self.phone_number}'
        print(call_str)
        self.call_history.append(call_str)

    def show_call_history(self):
        for x in self.call_history:
            print(x)


phone1 = Phone('123456')
phone2 = Phone('654321')

phone1.call(phone2)
phone1.show_call_history()




