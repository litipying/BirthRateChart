import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import numpy as np

data = []

with open('BirthRate.csv', newline='', encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    
    for row in reader:
        year = int(row[0])  
        birth_rate = float(row[1])  
        male_births = int(row[2])  
        female_births = int(row[3])  
        
        data.append((year, male_births, female_births, birth_rate))
        print(f'{year} -- Male: {male_births}, Female: {female_births}, Birth Rate: {birth_rate}')

years = [record[0] for record in data]
male_births = [record[1] for record in data]
female_births = [record[2] for record in data]
birth_rate = [record[3] for record in data]


sns.set(style="whitegrid")


fig, ax1 = plt.subplots(figsize=(10,5))

distance = 0.6

years = np.array(years)

# Plot bar charts using seaborn
ax1.bar(years - distance/2, male_births, width=0.4, color='blue', label='Male Births', alpha=0.7)
ax1.bar(years + distance/2, female_births, width=0.4, color='pink', label='Female Births', alpha=0.7)

ax1.set_ylabel('Number of Births')
ax1.set_xlabel('Year')


ax2 = ax1.twinx()

ax2.plot(years, birth_rate, color='green', label='Birth Rate', marker='o', linestyle='-', linewidth=2)

ax2.set_ylabel('Birth Rate (per 1,000 population)', color='green')


ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.title('Number of Births (Male & Female) and Birth Rate Over Time')


plt.show()
