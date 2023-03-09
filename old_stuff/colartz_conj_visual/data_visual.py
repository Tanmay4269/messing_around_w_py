import matplotlib.pyplot as plt
import pandas as pd

# Read the csv file
df = pd.read_csv("messing_around_w_py/colartz_conj_visual/coords.csv")

# Get the x and y coordinates from the dataframe
x = df['x']
y = df['y']

# Plot the points
plt.plot(x, y, 'ro')
plt.xlabel('Test number')
plt.ylabel('Number of iterations to converge')

# Show the plot
plt.show()
