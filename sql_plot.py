'''Reads and plot data from a database using sqlite'''

import sqlite3
import matplotlib.pyplot as plt

# Create a connection:
con = sqlite3.connect("LifeExpectancy.db")
# Interaction is possible thanks to:
cur = con.cursor()

# Then we execute a query:
life_raw = cur.execute('SELECT Life FROM LifeExpectancy').fetchall()
# and remove the parentheses and commas (needed to create a histogram)
life = [i[0] for i in life_raw]

''' # Alternatively, we can use a for loop:
life_raw = []
for row in cur.execute('SELECT Life FROM LifeExpectancy'):
    life_raw.append(row)
dat = [i[0] for i in life_raw]'''

# Another query:
life_gnp = cur.execute('SELECT GNP, Life FROM LifeExpectancy').fetchall()
x, y = [i[0] for i in life_gnp], [i[1] for i in life_gnp]

# Finally create a histogram
count, bins, ignored = plt.hist(life, 100, color = 'blue')
plt.xlabel('Life expectancy')
plt.ylabel('Count')
plt.title('Life expectancy histogram')

# and a scatter plot:
plt.scatter(x, y)
plt.xlabel('GNP')
plt.ylabel('Life expectancy')
plt.title('GNP vs Life expectancy')
plt.xscale('log')
plt.xlim(1,100000000)
plt.ylim(30,90)

plt.show()

# Close the connection
con.close()
