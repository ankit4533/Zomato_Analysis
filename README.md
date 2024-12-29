# Restaurant Data Analysis Project 🍽️

## Overview
This project analyzes restaurant data to provide insights into ratings, pricing, and overall performance metrics. Using Python and its data science libraries, we perform exploratory data analysis and create visualizations to understand restaurant performance patterns.

## Features
- Analysis of restaurant ratings distribution
- Identification of top-rated restaurants
- Cost vs. Rating correlation analysis
- Interactive visualizations

## Dependencies
```python
pandas==1.5.3
matplotlib==3.7.1
seaborn==0.12.2
```

## Project Structure
```
restaurant-analysis/
├── data/
│   └── reviews.csv
├── src/
│   └── analysis.py
├── README.md
└── requirements.txt
```

## Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/restaurant-analysis.git
cd restaurant-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Code Examples

### Data Preprocessing
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
data = pd.read_csv("reviews.csv")
df = pd.DataFrame(data)

# Clean 'Rate for two' column
df['Rate for two'] = df['Rate for two'].replace({',': ''}, regex=True).astype(float)
```

### Basic Analysis
```python
# Check data information
print(df.info())
print(df.head())

# Create rating distribution plot
plt.hist(df['Overall_Rating'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Overall Ratings')
plt.xlabel('Ratings')
plt.ylabel('Number of Restaurants')
plt.show()
```

### Advanced Analysis
```python
# Get top 5 restaurants
top_rated = df.sort_values(by='Overall_Rating', ascending=False).head(5)
print("Top 5 Restaurants with Highest Ratings:\n", 
      top_rated[['Name', 'Overall_Rating']])

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Rate for two', y='Overall_Rating', data=df)
```

## Visualizations Generated
1. Distribution of restaurant ratings
2. Scatter plot showing relationship between cost and ratings
3. Annotated plots with restaurant names

## Key Findings
- Distribution of restaurant ratings across different price ranges
- Correlation between restaurant prices and customer ratings
- Identification of top-performing restaurants

## Future Enhancements
- Add sentiment analysis of customer reviews
- Include geographical visualization of restaurant locations
- Implement time series analysis of rating trends

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
Your Name - https://github.com/ankit4533

Project Link: [https://github.com/ankit4533/restaurant-analysis](https://github.com/yourusername/restaurant-analysis)

 
