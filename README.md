# 📊 Excel Store Analysis - End-to-End Data Analytics Project

## 📌 Project Overview
This project involves an end-to-end data analysis of the **Vrinda Store** annual sales data for 2022. The goal is to clean the raw data, perform feature engineering, and generate actionable insights to help the store grow its sales in 2023.

**Input File:** `Excel_Store_Analysis.xlsx`
**Target Audience:** Business Stakeholders (Vrinda Store Management)
**Key Goal:** Identify customer purchasing behaviors, top-performing states, and sales trends.

---

## 📂 Dataset Dictionary
The input Excel file contains the following key columns (based on project requirements):
* **Index:** Unique ID for rows.
* **Order ID:** Unique identifier for transactions.
* **Cust ID:** Unique customer identifier.
* **Gender:** Gender of the customer (Needs cleaning).
* **Age:** Age of the customer.
* **Date:** Transaction date.
* **Status:** Order status (Delivered, Cancelled, Refunded, Returned).
* **Channel:** Sales platform (Amazon, Flipkart, Myntra, etc.).
* **Ship City/State:** Location of delivery.
* **Category:** Product category (Kurta, Set, etc.).
* **Amount:** Sales amount (Revenue).
* **Qty:** Quantity ordered.

---

## 🛠 Implementation Plan (For AI Agent)

### Phase 1: Data Cleaning
*Objective: Sanitize the raw dataset for analysis.*

1.  **Standardize Gender Column:**
    * The raw data contains inconsistent values: `M`, `Man`, `W`, `Women`.
    * **Action:** Normalize all values to standard terms:
        * Replace `M` → `Man`
        * Replace `W` → `Women`
2.  **Quantity (Qty) Correction:**
    * Ensure the `Qty` column is strictly numeric.
    * **Action:** Replace any text values (e.g., "One", "Two") with integers (`1`, `2`).
3.  **Null Check:**
    * Verify that critical columns (`Amount`, `Category`, `Status`) have no missing values. Drop or flag rows with missing critical data.

### Phase 2: Data Processing & Feature Engineering
*Objective: Create new columns to support demographic and trend analysis.*

1.  **Create `Age Group` Column:**
    * Bucket customers into categories based on the `Age` column.
    * **Logic:**
        * If `Age` ≥ 50 → **"Senior"**
        * If `Age` ≥ 30 and `Age` < 50 → **"Adult"**
        * If `Age` < 30 → **"Teenager"**
2.  **Create `Month` Column:**
    * Extract the month from the `Date` column to allow monthly aggregation.
    * **Format:** First 3 letters (e.g., Jan, Feb, Mar).

### Phase 3: Data Analysis & Visualization
*Objective: Generate specific aggregations to answer business questions.*

**1. Orders vs. Sales (Monthly Trend)**
* **Metric:** Compare Total Sales (Sum of Amount) and Total Order Count by Month.
* **Visualization Goal:** Dual-axis chart (Line for Orders, Bar for Sales).

**2. Sales by Gender**
* **Metric:** Total Sales (Sum of Amount) grouped by `Gender`.
* **Visualization Goal:** Pie Chart (to show percentage share).

**3. Order Status Breakdown**
* **Metric:** Count of unique Order IDs grouped by `Status`.
* **Visualization Goal:** Pie Chart (to highlight % of Delivered vs. Returned/Cancelled).

**4. Top 5 Performing States**
* **Metric:** Total Sales (Sum of Amount) grouped by `Ship State`.
* **Filter:** Sort descending and keep top 5.
* **Visualization Goal:** Horizontal Bar Chart.

**5. Age & Gender Analysis**
* **Metric:** Total Orders grouped by `Age Group` and `Gender`.
* **Visualization Goal:** Grouped Bar Chart (Contribution of Men vs. Women across age buckets).

**6. Sales by Channel**
* **Metric:** Share of Total Sales grouped by `Channel` (Amazon, Flipkart, etc.).
* **Visualization Goal:** Pie Chart or Donut Chart.

---

## 🔍 Key Insights to Validate
*The analysis should confirm the following hypotheses based on the data:*
1.  **Target Demographic:** Women are likely responsible for ~65% of purchases.
2.  **Peak Season:** Identify the month with the highest sales (Expected: March).
3.  **Top Channels:** Amazon, Flipkart, and Myntra should account for ~80% of sales.
4.  **Highest Value Customer Profile:** Adult Women (Age 30-49) in Maharashtra, Karnataka, and UP.

---

## 🚀 Execution Instructions for AI Editor
1.  Load the `Excel_Store_Analysis.xlsx` file.
2.  Perform the **Phase 1** cleaning steps using Pandas.
3.  Apply **Phase 2** transformations to create the dataframe for analysis.
4.  Generate summary tables (aggregations) for the 6 points in **Phase 3**.
5.  (Optional) If generating a report, output these visualizations using Matplotlib/Seaborn or write them back to a new Excel sheet named `Store_Report`.