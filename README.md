# 🛒 Local Kirana Store Analytics System

A Python-based Exploratory Data Analysis (EDA) project designed to uncover key sales insights and demand patterns for a local Kirana (retail) store.
This project demonstrates end-to-end data analysis - including data cleaning, transformation, trend detection, and visualization - using Pandas, Matplotlib, and modular Python scripting.
It follows a structured, professional workflow: raw data cleaned and standardized through custom utility functions in utils.py, analysis performed in Jupyter Notebook, and final visualizations exported to the /outputs directory.

## 📁 Project Structure 

```
kirana-store-analytics/
├── data/
│   ├── sales_data.csv              
│   └── sales_data_cleaned.csv      
│
├── notebook/
│   └── analysis.ipynb              
│
├── scripts/
│   └── utils.py                    
│
├── outputs/
│   ├── top_items.png               
│   ├── category_revenue.png        
│   ├── daily_trend.png             
│   └── weekly_trend.png            
│
└── README.md                      
```

## 📝 Description
This project helps small retailers or Kirana shop owners to:
- Understand sales performance
- Track product demand patterns
- Gain insights for better business decisions
> Ideal for Python learners who want to apply real-world data analytics skills using Pandas and NumPy.

## 🎯 Core Objectives
- Analyze daily and weekly sales performance
- Identify top-performing items and categories by revenue
- Visualize revenue trends and category distribution
- Detect short-term (weekly) demand patterns within available data

## 📁 Dataset
- Format: .csv
- Fields include:
   - Date
   - Item
   - Category
   - Quantity 
   - Price
   - Total Revenue

## 🧰 Tools & Libraries Used
- Python 3.x
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib (basic plots)
- Seaborn (optional for advanced visuals)

## 📊 Sample Output
Plots generated using Matplotlib/Seaborn to show:
- Top products by quantity  
- Daily and weekly revenue trends  
- Category-wise sales performance  

See visuals in `/outputs/`:  
- `top_items.png` — Top 5 items by total revenue  
- `category_revenue.png` — Revenue share by category  
- `daily_trend.png` — Daily revenue trend  
- `weekly_trend.png` — Weekly aggregated revenue trend

## 📊 Sales Performance Visuals

### 🛒 Top-Selling Items
![Top Items](outputs/top_items.png)

### 🧺 Category-wise Revenue
![Category Revenue](outputs/category_revenue.png)

### 📅 Daily Sales Trend
![Daily Trend](outputs/daily_trend.png)

### 📈 Weekly Revenue Trend
![Weekly Trend](outputs/weekly_trend.png)

## ⚙️ How to Run
**Step 1** Clone the repository
  
    https://github.com/jimmy-prakash/kirana-store-analytics.git

**Step 2** Navigate to the project folder

    cd kirana-store-analytics

**Step 3** Open the Jupyter Notebook
  
    jupyter notebook notebook/analysis.ipynb

Run all notebook cells step by step to view the analysis output.

## 🧠 Skills Demonstrated
- Data Cleaning & Handling Missing Values  
- Filtering, Sorting, Aggregation  
- GroupBy, Pivot Tables  
- Data Visualization (Bar, Line, Pie Charts)  
- Python File Structure & Modularity  
- Designed and executed a modular, reproducible data pipeline combining custom Python scripts (`utils.py`) with Jupyter-based analysis.

## 🚀 Future Enhancements
- Add more advanced visualizations
- Include inventory-level summary tables
- Create downloadable daily/weekly sales reports
- Extend the dataset to a multi-month or yearly range to analyze seasonal sales patterns.

## 🧾 Author

👤 Jimmi Prakash

Aspiring Data Analyst focused on deriving actionable business insights through Python-based data analytics.

🔗 github.com/jimmy-prakash




