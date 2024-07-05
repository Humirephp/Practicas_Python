### Dates ###

from datetime import datetime

new = datetime.now()
# Muestra el dia la hora los segundos el año los minutos y el mes en tiempo real
def print_date(date):
    print("DIA")
    print(date.day)
    print("Hora")
    print(date.hour)
    print("Segundos")
    print(date.second)
    print("Año")
    print(date.year)
    print("Minuto")
    print(date.minute)
    print("Mes")
    print(date.month)
    print(date.timestamp())

print_date(new)
 
timestamp = new.timestamp()
print(timestamp)

year_2024 = datetime(2025, 10, 10, 18, 30, 45,)

print_date(year_2024)

from datetime import time

import_time = time(8, 30, 20,)

print(import_time.hour)
print(import_time.minute)
print(import_time.second)

from datetime import date

import_date = date.today()

print(import_date.year)
print(import_date.month)
print(import_date.day)

import_date = date(2026, 10, 1,)

print(import_date.year)
print(import_date.month)
print(import_date.day)

import_date = date(import_date.year + 1, import_date.month + 1, import_date.day + 1,)
print(import_date.year)
print(import_date.month)
print(import_date.day)

diferencia = year_2024 - new
print(diferencia)
diferencia = year_2024.date() - import_date
print(diferencia)


from datetime import timedelta

star_timedelta = timedelta(5, 60, 10, weeks= 11,)
end_timedelta = timedelta(10, 60, 10, weeks= 12,)
print(end_timedelta - star_timedelta)
print(end_timedelta + star_timedelta)

    