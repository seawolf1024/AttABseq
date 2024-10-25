import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
dataset_name = 'AB645order'; #AB645order, AB1101order, S1131order
file_path = dataset_name + '.csv'
df = pd.read_csv(file_path)

print(df['ddG'])

# Plot a histogram for the ddG column
plt.hist(df['ddG'], bins=20, edgecolor='black')

# Add labels and title
plt.xlabel('ddG(kcal/mol)')
plt.ylabel('Count')
plt.title(file_path)

plt.savefig(dataset_name + '-distribution.png')
# Show the plot
plt.show()
