temperatures = [25, 30, 27, 22, 28, 33, 29]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

temperature_data = list(zip(days, temperatures))
print(temperature_data)
max_temperature = max(temperatures)
max_index = temperatures.index(max_temperature)
max_day = days[max_index]

print("Maximum temperature:", max_temperature)
print("Day:", max_day)

average_temperature = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temperature)
