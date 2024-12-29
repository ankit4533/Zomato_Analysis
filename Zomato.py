import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("reviews.csv")

# Create DataFrame
df = pd.DataFrame(data)

# Step 1: Data Preprocessing - Handle 'Rate for two' column
df['Rate for two'] = df['Rate for two'].replace({',': ''}, regex=True).astype(float)

# Step 2: Basic Data Inspection
print(df.info())  # Check for missing values and data types
print(df.head())  # Display the first few rows of the dataframe

# Step 3: Visualize Restaurant Ratings Distribution
plt.hist(df['Overall_Rating'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Overall Ratings')
plt.xlabel('Ratings')
plt.ylabel('Number of Restaurants')
plt.show()

# Step 4: Top 5 Restaurants with Highest Rating
top_rated = df.sort_values(by='Overall_Rating', ascending=False).head(5)
print("Top 5 Restaurants with Highest Ratings:\n", top_rated[['Name', 'Overall_Rating']])

# Step 5: Rating vs. Cost for Two (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rate for two', y='Overall_Rating', data=df)

# Annotate points with restaurant names
for i in range(df.shape[0]):
    plt.text(df['Rate for two'][i], df['Overall_Rating'][i], df['Name'][i], fontsize=9)

plt.title('Rating vs Cost for Two')
plt.xlabel('Cost for Two')
plt.ylabel('Overall Rating')
plt.show()