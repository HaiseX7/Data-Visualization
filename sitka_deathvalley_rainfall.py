import matplotlib.pyplot as plt
from datetime import datetime
import csv


filename = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'
with open(filename) as f, open(filename2) as f2:
	reader_sitka = csv.reader(f)
	reader_dv = csv.reader(f2)
	header_sitka = next(reader_sitka)
	header_dv = next(reader_dv)
	print(header_sitka)
	print(header_dv)

	dates_sitka, dates_dv, prcps_sitka, prcps_dv = [], [], [], []
	for row in reader_sitka:
		date_sitka = datetime.strptime(row[2], '%Y-%m-%d')
		prcp_sitka = float(row[3])
		prcps_sitka.append(prcp_sitka)
		dates_sitka.append(date_sitka)

	for row in reader_dv:
		date_dv = datetime.strptime(row[2], '%Y-%m-%d')
		prcp_dv = float(row[3])
		prcps_dv.append(prcp_dv)
		dates_dv.append(date_dv)


fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(dates_sitka, prcps_sitka)
ax1.set_title("Daily Precipitation in Sitka", fontsize=16)
ax1.set_ylabel("Rain (in)", fontsize=12)

ax2.plot(dates_dv, prcps_dv)
ax2.set_title("Daily Precipitation in Death Valley", fontsize=16)
ax2.set_ylabel("Rain (in)", fontsize=12)
plt.show()

