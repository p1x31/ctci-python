
def days_in_year(year, month, day):
    # Список с количеством дней в каждом месяце
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Суммируем элементы списка до нужного месяца
    days = sum(days_in_month[:month-1])
    # Прибавляем день
    days += day
    # Возвращаем результат
    return days

# Функция для подсчета секунд в дне до заданного времени
def seconds_in_day(hour, minute, second):
    # Умножаем час на 3600
    seconds = hour * 3600
    # Умножаем минуту на 60 и прибавляем к секундам
    seconds += minute * 60
    # Прибавляем секунду
    seconds += second
    # Возвращаем результат
    return seconds

# Функция для решения задачи
def solve(year1, month1, day1, hour1, min1, sec1,
          year2, month2, day2, hour2, min2, sec2):
    # Вычисляем разницу между годами в днях
    days = (year2 - year1) * 365
    # Добавляем разницу между днями в году
    days += days_in_year(year2, month2, day2) - days_in_year(year1, month1, day1)
    # Если первая дата больше второй по времени (но не по дате), то вычитаем один день
    # if (hour1 > hour2 or (hour1 == hour2 and min1 > min2) or 
    #     (hour1 == hour2 and min1 == min2 and sec1 > sec2)):
    #     days = days
    # # Если вторая дата больше первой по времени (но не по дате), то прибавляем один день
    # elif (hour2 > hour1 or (hour2 == hour1 and min2 > min1) or 
    #       (hour2 == hour1 and min2 == min1 and sec2 > sec1)):
    #     days = days
    # Вычисляем разницу между временами в секундах
    seconds = seconds_in_day(hour2, min2, sec2) - seconds_in_day(hour1, min1, sec1)
    # Если секунды отрицательные, то прибавляем 86400 (количество секунд в сутках) и вычитаем один день
    if seconds < 0:
        seconds += 86400
        days -= 1
    # Возвращаем пару из дней и секунд
    return (days, seconds)

# Читаем входные данные
year1, month1, day1, hour1, min1, sec1 = map(int, input().split())
year2, month2, day2, hour2, min2, sec2 = map(int, input().split())
# Выводим ответ
print(*solve(year1, month1, day1, hour1, min1, sec1,
             year2, month2, day2, hour2, min2, sec2))