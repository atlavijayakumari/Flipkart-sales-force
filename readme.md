# Multi-Source Sales Data Pipeline & Business Insights Dashboard

## Documentation

### Dataset & Preparation
- Data sources: CSV, JSON, and Excel files.
- Load all files if present; otherwise, skip.
- Clean data by:
  - Converting `Date` to datetime format.
  - Standardizing `Product` names (trim + title case).
  - Removing missing values and duplicates.

### Key Insights
- Total revenue and units sold.
- Revenue by product.
- Monthly revenue trends.

### Visualizations
- Revenue over time (line chart).
- Product-wise revenue summary.

### How to Run
1. Place `sample_sales_data.csv`, `.json`, and `.xlsx` in the same folder as the script/notebook.
2. Run the Python script or Jupyter Notebook.
3. View output and visualizations.
4. (Optional) Export reports as CSV or PDF.

### Next Steps
- Create a secure login dashboard for controlled access to reports.
