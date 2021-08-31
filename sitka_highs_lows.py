import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)
	print(header)
	
	highs, lows, dates = [], [], []
	for row in reader:
		date =  datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		dates.append(date)
		highs.append(high)
		lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, lows, c='blue', alpha=0.7)
ax.plot(dates, highs, c='red', alpha=0.7)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high and low temperatures - 2018 (Sitka)", fontsize=24)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', labelsize=12)

plt.show()


