temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]
positive_readings, negative_readings = 0, 0

for num in temperature_readings:
    if num >= 0:
        positive_readings += num
    else:
        negative_readings += num

print('Average of positive readings:', positive_readings)

print('Average of negative readings', negative_readings)

