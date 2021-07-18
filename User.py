import random

#from intfaaace import *
'''model_time = 1000  # 10080
ecm_count = 10  # 10 кол-во ЭВМ
printer_count = 5  # 5 кол-во принтеров
user_interval = 10  # 10 интервал между людьми
user_task_interval = 15  # 15 между выполняемыми заданиями
printer_use_time = 5  # 5 использование принтера
use_printer_chance = 30  # 30 вероятность исполльзования принтера'''


ecm_users = []
printer_users = []
ecm_pending_users = []
printer_pending_users = []
ecm_list = []
printer_list = []

queue_sum_ecm = 0
queue_sum_printer = 0
printer_in_use_sum = 0
ecm_in_use_sum = 0


'''def read_start_values(self):
    global ecm_count
    ecm_count = int(self.ecm_count_cnt.text())
    global printer_count
    printer_count = int(self.printer_count_cnt.text())
    global user_interval
    user_interval = int(self.user_interval_cnt.text())
    global user_task_interval
    user_task_interval = int(self.user_task_interval_cnt.text())
    global printer_use_time
    printer_use_time = int(self.printer_use_time_cnt.text())
    global use_printer_chance
    use_printer_chance = int(self.use_printer_chance_cnt.text())
    # self.time_be4_cmplt_evm1 = int(self.time_evm1_task_cnt.text())
    global model_time
    model_time = int(self.model_time_cnt.text())'''



class User(MainWindow):
    def __init__(self):
        self.will_use_printer = True if (random.randint(0, 100) <= use_printer_chance) else False
        self.task_remaining_time = user_task_interval
        self.printer_remaining_time = printer_use_time
        self.wants_to_use_printer = False
        self.done_ecm = False
        self.done_printer = False
        self.name_ecm_work = ""
        self.name_printer_work = ""
        self.ecm_end = False
        '''self.will_use_printer = False
        self.task_remaining_time = 0
        self.printer_remaining_time = 0
        self.wants_to_use_printer = False
        self.done_ecm = False
        self.done_printer = False
        self.name_ecm_work = ""
        self.name_printer_work = ""
        self.ecm_end = False'''

    def ecm_tick(self):
        if self.ecm_end == False:
            if self.will_use_printer:  # если будет работать с принтером
                if self.task_remaining_time != 0:  # если еще работает с эвм
                    self.task_remaining_time -= 1  # тогда уменьшаем время до окончания
                else:
                    self.done_ecm = True  # то закончил с ЭВМ
                    self.wants_to_use_printer = True  # и ждет принтер
            else:  # если не будет работать с принтером
                if self.task_remaining_time != 0:  # если еще работает с эвм
                    self.task_remaining_time -= 1  # тогда уменьшаем время до оканчания
                else:
                    self.done_ecm = True  # иначе задание выполнено


    def printer_tick(self):
        if self.printer_remaining_time != 0:  # если работа принтера не 0
            self.printer_remaining_time -= 1  # тогда уменьшаем время до окончания принтера
        else:
            self.done_printer = True  # иначе выполнено