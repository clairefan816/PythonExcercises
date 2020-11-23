
# get temp values from https://www.wunderground.com/weather/us/wa/seattle
future_high_temp_fahren = [37, 39, 42, 41, 45, 49, 49, 47, 47, 47]
future_low_temp_fahren = [30, 37, 33, 37, 41, 43, 41, 42, 41, 41]
future_noon_temp_fahren = [30, 36, 41, 39, 43, 48, 47, 46, 46, 45]
BASE = 32
CONVERSION_FACTOR = 5.0/9.0
PRECISION = 1
FUTURE_DAYS = 10

# What is the difference between the highest and the lowest temperature values predicted for the 10 day forecast?
ten_day_highest_fahren = 49
ten_day_lowest_fahren = 30
diff = ten_day_highest_fahren - ten_day_lowest_fahren
print('The difference between the highest and the lowest temperature values predicted for the 10 day forecast is: ', diff, 'degree Fahrenheit')

# What is the average temperature at noon predicted for the 10 day forecast?

s_noon = 0
for i in range(FUTURE_DAYS):
    s_noon += future_noon_temp_fahren[i]
average_noon = s_noon/FUTURE_DAYS
print('The average temperature at noon predicted for the 10 day forecast is: ', average_noon, 'degree Fahrenheit')


# What is the highest temperature predicted for the 10 day forecast, converted from Fahrenheit to Celsius?
celsius_temp = (float(ten_day_highest_fahren) - BASE) * CONVERSION_FACTOR
print('The highest temperature predicted for the 10 day forecast would be ', round(celsius_temp, PRECISION), 'degree Celsius')

