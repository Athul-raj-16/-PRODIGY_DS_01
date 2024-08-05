import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
df = pd.read_csv('population.csv')

# Check the first few rows of the dataframe to understand its structure
print(df.head())

# Select the year of interest, for example 1973
year = '2000'

# Filter out the relevant columns: Country Name and the specific year
df_year = df[['Country Name', year]].dropna()

# Rename columns for convenience
df_year.columns = ['Country Name', 'Population']

# Convert Population to numeric values
df_year['Population'] = pd.to_numeric(df_year['Population'], errors='coerce')

# Drop rows with any missing values after conversion
df_year = df_year.dropna()

# Plotting the histogram of population distribution for the year 1973
plt.figure(figsize=(12, 8))
sns.histplot(df_year['Population'], bins=30, kde=True)

# Adding titles and labels
plt.title('Population Distribution in 2000')
plt.xlabel('Population')
plt.ylabel('Frequency')

# Show the plot
plt.show()
