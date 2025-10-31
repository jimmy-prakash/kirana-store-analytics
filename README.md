# 🛒 Local Kirana Store Analytics System

An end-to-end, beginner-friendly Python data analytics project that simulates sales tracking for a local Kirana (grocery) store.
This project demonstrates essential data analysis skills using real-world scenarios like identifying top-selling products, tracking trends, and generating insights — all through pure Python and Jupyter Notebook.

## 📁 Project Structure 

```
kirana-store-analytics/
├── data/
│   ├── sales_data.csv              # Raw data (optional)
│   └── sales_data_cleaned.csv      # Cleaned data (ready for EDA)
│
├── notebook/
│   └── analysis.ipynb              # Final, renamed clean notebook
│
├── scripts/
│   └── utils.py                    # Helper cleaning functions
│
├── outputs/
│   ├── top_items.png               # Visualization 1
│   ├── category_revenue.png        # Visualization 2
│   ├── daily_trend.png             # Visualization 3
│   └── weekly_trend.png            # Visualization 4
│
└── README.md                       # Documentation
```

## 📝 Description
This project helps small retailers or Kirana shop owners to:
- Understand sales performance
- Track product demand patterns
- Gain insights for better business decisions
> Ideal for Python learners who want to apply real-world data analytics skills using Pandas and NumPy.

## 🎯 Core Objectives
- Analyze daily & weekly sales performance
- Identify best-selling items (by quantity and revenue)
- Visualize product trends and category-wise sales
- Detect weekly demand patterns

## 📁 Dataset
- Format: .csv
- Fields include:
   - Date
   - Product Name
   - Category
   - Quantity Sold
   - Unit Price
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
(See: outputs/sample_plot.png)

## ⚙️ How to Run
**Step 1** Clone the repository
  
    https://github.com/jimmy-prakash/kirana-store-analytics.git

**Step 2** Navigate to the project folder

    cd kirana-store-analytics

**Step 3** Open the Jupyter Notebook
  
    jupyter notebook notebook/analysis.ipynb

Run all notebook cells step-by-step to view the analysis output.

## 🧠 Skills Demonstrated
- Data Cleaning & Handling Missing Values
- Filtering, Sorting, Aggregation
- GroupBy, Pivot Tables
- Data Visualization (Bar, Line, Pie Charts)
- Python File Structure & Modularity

## 🚀 Future Enhancements
- Add more advanced visualizations
- Include inventory-level summary tables
- Create downloadable daily/weekly sales reports

## 🙋‍♂️ Author
Jimmy Prakash

Aspiring Data Analyst focused on solving real-world problems using Python.

🔗 github.com/jimmy-prakash

