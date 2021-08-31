import csv
from datetime import datetime
import matplotlib.pyplot as plt


def find_tmin_tmax_index(header_row):
	for i in range(len(header_row)):
		if header_row[i] == 'TMIN':
			tmin = i 
		elif header_row[i] == 'TMAX':
			tmax = i
	return (tmin, tmax)


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	tmin, tmax = find_tmin_tmax_index(header_row)

	dates_dv, highs_dv, lows_dv = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[2], '%Y-%m-%d')
			high = int(row[tmax])
			low = int(row[tmin])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates_dv.append(current_date)
			highs_dv.append(high)
			lows_dv.append(low)

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	tmin, tmax = find_tmin_tmax_index(header_row)
	
	highs_sitka, lows_sitka, dates_sitka = [], [], []
	for row in reader:
		date =  datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[tmax])
		low = int(row[tmin])
		dates_sitka.append(date)
		highs_sitka.append(high)
		lows_sitka.append(low)

fig, ax = plt.subplots()
ax.plot(dates_sitka, highs_sitka, c='blue', alpha=0.7)
ax.plot(dates_sitka, lows_sitka, c='blue', alpha=0.7)
ax.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

ax.plot(dates_dv, highs_dv, c='red', alpha=0.7)
ax.plot(dates_dv, lows_dv, c='red', alpha=0.7)
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='red', alpha=0.1)

ax.set_title("High and Low Temperature of Sitka and Death Valley (2018)", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(axis='both', labelsize=12)

plt.show()

"""
I tried to make a plot that colored the overlapped area between the two graphs 
purple to show explicitly when Sitka was hotter than Death Valley's low. However,
It didnt work because there wasn't enough frequency in the temperature
recordings so it was inherently off.

overlap_highs, overlap_lows, overlap_dates = [], [], []
for x in range(len(dates_sitka)):
	if highs_sitka[x] >= lows_dv[x]:
		if lows_sitka[x] >= lows_dv[x]:
			overlap_highs.append(highs_sitka[x])
			overlap_lows.append(lows_sitka[x])
			overlap_dates.append(dates_sitka[x])
		else:
			overlap_highs.append(highs_sitka[x])
			overlap_lows.append(lows_dv[x])
			overlap_dates.append(dates_sitka[x])
print(overlap_dates)
ax.plot(overlap_dates, overlap_highs, s=5, c='purple', alpha=0.7)
ax.plot(overlap_dates, overlap_lows, s=5, c='purple', alpha=0.7)
ax.fill_between(overlap_dates, overlap_highs, overlap_lows, facecolor='purple', alpha=0.7)
"""
