# Day 23: Excel Power Query - ETL Basics
# Author: Bhanu Pratap Singh
# Date: April 27, 2026

"""
POWER QUERY ETL WORKFLOW
Extract → Transform → Load

Today's Learning:
- Power Query basics in Excel
- ETL concepts (Extract, Transform, Load)
- Data cleaning steps:
  1. Capitalize column names
  2. Standardize region names
  3. Handle missing values
  4. Filter cancelled orders
"""

# Manual steps completed in Excel Power Query Editor:
# 1. Loaded raw_sales data
# 2. Transformed "Sales Rep" column - Capitalize Each Word
# 3. Transformed "Region" column - Capitalize Each Word
# 4. Standardized "Status" column - lowercase
# 5. Replaced null values in "Amount" with 0
# 6. Replaced null values in "Sales Rep" with "Unknown"
# 7. Filtered out "cancelled" status records
# 8. Loaded clean data to new worksheet
# 9. Tested refresh functionality with new data

# Key Learnings:
# - Power Query remembers transformation steps
# - Can refresh data and all transformations apply automatically
# - Better than manual Excel cleanup
# - Real-world use case: Automated data pipelines in finance

print("Day 23: Power Query ETL workflow completed!")
print("Next: Master pandas (Day 29-35) for Python equivalent")