class Appointment:
    def __init__(self,day_name,start_time):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
        self.__day_of_week = day_name
        self.__start_time_hour = start_time
    def get_name(self):
        return self.__client_name
    def get_phone(self):
        return self.__client_phone
    def get_appt_type(self):
        return self.__appt_type
    def get_day_of_week(self):
        return self.__day_of_week
    def get_start_time_hour(self):
        return self.__start_time_hour
    def get_appt_type_desc(self):
        desc = {0:'Available',1:'Mens Cut',2:'Ladies Cut',3:'Mens Colouring',4:'Ladies Colouring'}
        return desc[self.__appt_type]
    def get_end_time_hour(self):
        return self.__start_time_hour + 1
    def set_client_name(self,name):
        self.__client_name = name
    def set_client_phone(self,phone):
        self.__client_phone = phone
    def set_appt_type(self,type):
        self.__appt_type = type
    def schedule(self,name,phone,type):
        self.set_client_name(name)
        self.set_client_phone(phone)
        self.set_appt_type(type)
    def cancel(self):
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0
    def format_record(self):
        return f'{self.get_name()},{self.get_phone()},{self.get_appt_type()},{self.get_day_of_week()},{self.get_start_time_hour()}'
    
    def __str__(self):
        return f'{self.get_name():<15}  {self.get_phone():<12}  {self.get_day_of_week():^12}  {self.get_start_time_hour():>2}:00  -  {self.get_end_time_hour():<2}:00  {self.get_appt_type_desc():^15}'


