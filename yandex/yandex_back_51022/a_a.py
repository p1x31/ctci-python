def calculate_days_and_seconds(start_date, end_date):
    year1, month1, day1, hour1, min1, sec1 = start_date
    year2, month2, day2, hour2, min2, sec2 = end_date

    # Calculate the number of days
    days = (year2 - year1) * 365
    days += (month2 - month1) * 31
    days += day2 - day1

    # Calculate the number of seconds in the incomplete day
    seconds = (hour2 - hour1) * 3600
    seconds += (min2 - min1) * 60
    seconds += sec2 - sec1

    return days, seconds


# Read the input
start_date = list(map(int, input().split()))
end_date = list(map(int, input().split()))

# Calculate the result
result = calculate_days_and_seconds(start_date, end_date)

# Print the result
print(*result)