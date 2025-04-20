import random
from datetime import date
from array import array
years = [random.randint(date.today().year - 5, date.today().year) for i in range(10)]
months = [random.randint(1, 12) for i in range(10)]
days = []
for i in range(len(months)):
    if months[i] == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        d = 31
    elif months[i] == 4 or 6 or 10 or 11:
        d = 30
    elif months[i] == 2 and years[i] % 4 == 0:
        d = 29
    else: 
        d = 28
    days.append(random.randint(1, d))

array_of_time = array('i', [])
somedates = [date(years[i], months[i], days[i]) for i in range(10)]

for i in somedates:
    array_of_time.append(i.toordinal())

#При данном подходе вычисляются 10 разниц, так как также вычисляется разница между первой и последней датой. 
for i in range(10):
    print(f'Разница между {somedates[i-1]} и {somedates[i]}: {abs(array_of_time[i] - array_of_time[i-1])} дней')

