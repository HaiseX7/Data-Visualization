import csv 
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/bay_area_2020.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	sf_data = []
	for row in reader:
		if row[1] == 'SAN FRANCISCO INTERNATIONAL AIRPORT, CA US':
			sf_data.append(row)

	dates_sf, highs_sf, lows_sf = [], [], []
	for row in sf_data:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[9])
		low = int(row[10])

		dates_sf.append(date)
		highs_sf.append(high)
		lows_sf.append(low)

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	dates_dv, highs_dv, lows_dv = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[2], '%Y-%m-%d')
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates_dv.append(current_date)
			highs_dv.append(high)
			lows_dv.append(low)

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)
	print(header)
	
	highs_sitka, lows_sitka, dates_sitka = [], [], []
	for row in reader:
		date =  datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		low = int(row[6])
		dates_sitka.append(date)
		highs_sitka.append(high)
		lows_sitka.append(low)


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(dates_sitka, highs_sitka, c='blue', alpha=0.7)
ax1.plot(dates_sitka, lows_sitka, c='blue', alpha=0.7)
ax1.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

ax1.plot(dates_dv, highs_dv, c='red', alpha=0.7)
ax1.plot(dates_dv, lows_dv, c='red', alpha=0.7)
ax1.fill_between(dates_dv, highs_dv, lows_dv, facecolor='red', alpha=0.1)

ax1.plot(dates_sf, highs_sf, c='green', alpha=0.7)
ax1.plot(dates_sf, lows_sf, c='green', alpha=0.7)
ax1.fill_between(dates_sf, highs_sf, lows_sf, facecolor='green', alpha=0.1)

ax1.set_title("High and Low Temperature of Sitka and Death Valley (2018) and San Francisco (2020)", fontsize=16)
ax1.set_ylabel("Temperature (F)", fontsize=12)
ax1.tick_params(axis='both', labelsize=12)

ax2.plot(range(363), highs_sitka, c='blue', alpha=0.7)
ax2.plot(range(363), lows_sitka, c='blue', alpha=0.7)
ax2.fill_between(range(363), highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

ax2.plot(range(363), highs_dv, c='red', alpha=0.7)
ax2.plot(range(363), lows_dv, c='red', alpha=0.7)
ax2.fill_between(range(363), highs_dv, lows_dv, facecolor='red', alpha=0.1)

ax2.plot(range(367), highs_sf, c='green', alpha=0.7)
ax2.plot(range(367), lows_sf, c='green', alpha=0.7)
ax2.fill_between(range(367), highs_sf, lows_sf, facecolor='green', alpha=0.1)

ax2.set_title("Comparison of High and Low Temperature of Sitka and Death Valley (2018) and San Francisco (2020)", fontsize=16)
ax2.set_ylabel("Temperature (F)", fontsize=12)
ax2.set_xlabel("Day # of the year", fontsize=12)
ax2.tick_params(axis='both', labelsize=12)

plt.show()

