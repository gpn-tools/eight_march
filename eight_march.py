import random
import datetime
import pdb

from settings import *

days_of_week = {1:'ПН', 2:'ВТ', 3:'СР', 4:'ЧТ', 5:'ПТ', 6:'СБ', 7:'ВС'}

# вычисление количества сотрудников мужского и женского пола
qty_staff_m = len(staff_m)  
qty_staff_w = len(staff_w)

# вычисление дня недели праздника и даты поздравления
date_of_8_march = datetime.datetime(datetime.datetime.now().year,3,8)
day_of_week_8_march = date_of_8_march.isoweekday()
if (day_of_week_8_march == 1) or (day_of_week_8_march == 6) or (day_of_week_8_march == 7):
    day_of_compliment = 5
else:
    day_of_compliment = day_of_week_8_march - 1
date_of_compliment = date_of_8_march - datetime.timedelta(abs(day_of_week_8_march - day_of_compliment))

# вычисление размера взноса с каждого содрудника-мужчины
payment = int(qty_staff_w*budget_per_w_person/qty_staff_m)
     
# печать в консоль ранее рассчитанных значений     
print('\nВ этом году 8 марта это ', days_of_week[day_of_week_8_march], 
      '. Поздравлять надо в(во) ', days_of_week[day_of_compliment], 
      ' (',date_of_compliment.strftime('%d.%m.%Y'), ')\n', sep='')
print('Всего женщин в этом году - ', qty_staff_w, sep='')
print('Всего мужчин в этом году - ', qty_staff_m, '\n', sep='')
print('Бюджет на одну женщину установлен равным ', budget_per_w_person, 
      ' руб. Каждый участник поздравления должен будет сдать ', payment , ' руб.\n', sep='')

# функция для вывода результатов назначения на экран
def print_results(results):
    for each in results:
        print("\t", each[0], " - ", each[1], sep="")

# назначение участников на задачи
assignment_result = []
if len(fixed_assignment) > 0:
    for each in fixed_assignment:
        assignment_result.append( (tasks[each[0]], staff_m[each[1]]) ) 
    for each in assignment_result:    
        tasks.remove(each[0])
        staff_m.remove(each[1])

print('Распределение добровольцев по подготовительным задачам следующее:')
print_results(assignment_result)

random.seed()
assignment_result = []
for task in tasks:
    random_number = random.randint(0, len(staff_m)-1)
    assignment_result.append( (task, staff_m[random_number]) ) 
    staff_m.remove(staff_m[random_number])

print('\nРаспределение людей по остальным подготовительным задачам следующее:')
print_results(assignment_result)

# pdb.set_trace()
