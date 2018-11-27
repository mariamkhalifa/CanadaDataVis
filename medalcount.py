import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count +=1
		else:
			if row[7] == "Gold":
				golds.append(row[7])
			elif row[7] == "Silver":
				silvers.append(row[7])
			else:
				bronzes.append(row[7])
			line_count += 1

print('processed', line_count, 'rows of data')
print('gold medals won: ', len(golds))
print('silver medals won: ', len(silvers))
print('bronze medals won: ', len(bronzes))

pct_golds = len(golds) / line_count * 100
pct_silvers = len(silvers) / line_count * 100
pct_bronzes = len(bronzes) / line_count * 100
# do some math here and draw a pie chart based on last week's example
labels = "Gold", "Silver", "Bronze"
sizes = [pct_golds, pct_silvers, pct_bronzes]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=True)

plt.legend(labels, loc=1)
plt.title("Medals by Color")
plt.show()


