import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# 1. Fetch Data
URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

# 2. Direct Extraction (List Comprehension)
# We are grabbing Name, Price, and Description
items = soup.find_all("div", class_="thumbnail")

laptop_data = [
    {
        "Model": item.find("a", class_="title").text.strip(),
        "Current_Price": float(item.find("h4", class_="price").text.replace("$", "")),
        # We simulate an 'Original Price' by adding 15% to show a 'Discount'
        "Original_Price": round(float(item.find("h4", class_="price").text.replace("$", "")) * 1.15, 2),
        "Reviews": int(item.find("p", class_="review-count").text.split()[0]) if item.find("p", class_="review-count") else 0
    }
    for item in items
]

# 3. Data Analysis with Pandas
df = pd.DataFrame(laptop_data)

# Calculate the 'Savings'
df['Savings'] = df['Original_Price'] - df['Current_Price']

# Filter: Only show Laptops with more than 10 reviews (High Reliability)
reliable_deals = df[df['Reviews'] > 10].sort_values(by='Savings', ascending=False).head(8)

# 4. Professional Visualization
plt.figure(figsize=(12, 7))
plt.barh(reliable_deals['Model'], reliable_deals['Savings'], color='forestgreen')

# Add Labels
plt.title('Best Value Deals (Potential Savings in USD)', fontsize=15)
plt.xlabel('Total Savings ($)', fontsize=12)
plt.ylabel('Laptop Model', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig('value_analysis.png')
plt.show()

print("Analysis Complete. Dataframe of Best Deals:")
print(reliable_deals[['Model', 'Current_Price', 'Savings']])