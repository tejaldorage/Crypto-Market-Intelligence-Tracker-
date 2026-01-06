# 📊 Crypto Market Intelligence Tracker
(Web Scraping & Data Analysis Project)

## 📌 Project Overview
The Crypto Market Intelligence Tracker is a Python-based data scraping and analytics project that demonstrates how to collect, process, analyze, and visualize market data using real-world web scraping techniques.
Although named for crypto intelligence, this implementation uses a sample e-commerce website to safely simulate real market data extraction. The project focuses on identifying high-value deals based on pricing trends, review counts, and potential savings.
This project showcases practical skills in web scraping, data analysis, and data visualization, making it suitable for data science and analytics portfolios.

## 📌 Features
- 📊 Web scraping with BeautifulSoup  
- 🧠 Data analysis using Pandas  
- 📉 Visualization with Matplotlib

## 🎯 Objectives
- Scrape structured data from a live website using BeautifulSoup
- Clean and transform raw data into meaningful insights
- Analyze pricing patterns and calculate potential savings
- Identify high-reliability products based on review counts
- Visualize insights using Matplotlib

## 🛠️ Technologies Used
- Python
- Requests – for HTTP requests
- BeautifulSoup (bs4) – for HTML parsing
- Pandas – for data manipulation and analysis
- Matplotlib – for data visualization

## 🖼️ Screenshot

### excal page

<img width="1070" height="560" alt="Screenshot 2026-01-06 144859" src="https://github.com/user-attachments/assets/d8274c44-b7ed-4f81-954c-2142ed7cb238" />

### value analysis.png 

<img width="1917" height="974" alt="Screenshot 2026-01-06 145000" src="https://github.com/user-attachments/assets/f53239f8-cf9d-443d-802e-170ffc89e1d7" />

## 📂 Project Structure
```
WEB SCRAPING/
│
├── Crypto-Market-Intelligence-Tracker.py  # Web scraping and analysis script
├── value_analysis.png     # Generated visualization
├── README.md              # Project documentation

```
## 📈 Data Analysis
- Calculate Savings = Original Price − Current Price
- Filter products with more than 10 reviews (higher reliability)
-  Rank products by maximum potential savings
- Select Top 8 best-value deals
  
## 📊 Visualization

- Horizontal bar chart displaying potential savings

- Clean, professional layout with labels and grid lines

- Output saved as value_analysis.png


# 🚀 How to Run the Project
  1️⃣ Install Required Libraries
  pip install requests beautifulsoup4 pandas matplotlib
  2️⃣ Run the Script
  Crypto-Market-Intelligence-Tracker.py
- 3️⃣ Output
- Printed table of best deals in the terminal
- Saved visualization image: value_analysis.png

# 📌 Sample Output
Analysis Complete. Dataframe of Best Deals:
             Model     Current_Price   Savings
------------------------------------------------
Laptop XYZ         799.99             120.00
Laptop ABC         699.99             105.00


  





