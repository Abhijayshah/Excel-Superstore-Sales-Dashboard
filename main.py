import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for charts
sns.set_theme(style="whitegrid")

def clean_data(df):
    """Phase 1: Data Cleaning"""
    print("--- Phase 1: Data Cleaning ---")
    
    # 1. Standardize Gender Column
    # Replace M/Men -> Man, W/Women -> Women (based on project requirement M->Man, W->Women)
    # The README says M -> Man, W -> Women. Assuming 'Men' should also be 'Man' and 'Women' is already standard.
    df['Gender'] = df['Gender'].replace({'M': 'Man', 'Men': 'Man', 'W': 'Women'})
    print("Standardized Gender column.")
    
    # 2. Quantity (Qty) Correction
    # Replace any text values with integers
    qty_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    df['Qty'] = df['Qty'].replace(qty_map)
    df['Qty'] = pd.to_numeric(df['Qty'], errors='coerce').fillna(1).astype(int)
    print("Corrected Qty column.")
    
    # 3. Null Check
    # Verify critical columns have no missing values
    critical_cols = ['Amount', 'Category', 'Status']
    df = df.dropna(subset=critical_cols)
    print(f"Dropped rows with null values in {critical_cols}.")
    
    return df

def feature_engineering(df):
    """Phase 2: Data Processing & Feature Engineering"""
    print("\n--- Phase 2: Feature Engineering ---")
    
    # 1. Create Age Group Column
    # Logic: Age >= 50 -> "Senior", 30 <= Age < 50 -> "Adult", Age < 30 -> "Teenager"
    def get_age_group(age):
        if age >= 50:
            return "Senior"
        elif age >= 30:
            return "Adult"
        else:
            return "Teenager"
    
    df['Age Group'] = df['Age'].apply(get_age_group)
    print("Created 'Age Group' column.")
    
    # 2. Create Month Column
    # Extract first 3 letters of month from Date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.strftime('%b')
    print("Created 'Month' column.")
    
    return df

def perform_analysis(df):
    """Phase 3: Data Analysis & Visualization"""
    print("\n--- Phase 3: Data Analysis & Visualization ---")
    
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        print("Created 'outputs' folder.")

    # 1. Orders vs. Sales (Monthly Trend)
    monthly_data = df.groupby('Month').agg({'Amount': 'sum', 'Order ID': 'count'}).reset_index()
    # Sort months by calendar order
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_data['Month'] = pd.Categorical(monthly_data['Month'], categories=months_order, ordered=True)
    monthly_data = monthly_data.sort_values('Month')
    
    print("\n1. Orders vs. Sales (Monthly Trend):")
    print(monthly_data)
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=monthly_data, x='Month', y='Amount', ax=ax1, color='skyblue', label='Sales')
    ax1.set_ylabel('Total Sales (Amount)')
    
    ax2 = ax1.twinx()
    sns.lineplot(data=monthly_data, x='Month', y='Order ID', ax=ax2, marker='o', color='darkblue', label='Orders')
    ax2.set_ylabel('Total Orders')
    
    plt.title('Monthly Sales and Order Trends')
    fig.tight_layout()
    plt.savefig('outputs/monthly_trend.png')
    plt.close()

    # 2. Sales by Gender
    gender_sales = df.groupby('Gender')['Amount'].sum()
    print("\n2. Sales by Gender:")
    print(gender_sales)
    
    plt.figure(figsize=(8, 8))
    plt.pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
    plt.title('Sales Distribution by Gender')
    plt.savefig('outputs/sales_by_gender.png')
    plt.close()

    # 3. Order Status Breakdown
    status_counts = df['Status'].value_counts()
    print("\n3. Order Status Breakdown:")
    print(status_counts)
    
    plt.figure(figsize=(8, 8))
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Order Status Breakdown')
    plt.savefig('outputs/order_status_breakdown.png')
    plt.close()

    # 4. Top 5 Performing States
    top_states = df.groupby('ship-state')['Amount'].sum().sort_values(ascending=False).head(5)
    print("\n4. Top 5 Performing States:")
    print(top_states)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_states.values, y=top_states.index, hue=top_states.index, palette='viridis', legend=False)
    plt.title('Top 5 Performing States by Sales')
    plt.xlabel('Total Sales (Amount)')
    plt.savefig('outputs/top_5_states.png')
    plt.close()

    # 5. Age & Gender Analysis
    age_gender = df.groupby(['Age Group', 'Gender'])['Order ID'].count().reset_index()
    print("\n5. Age & Gender Analysis (Order Counts):")
    print(age_gender)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=age_gender, x='Age Group', y='Order ID', hue='Gender')
    plt.title('Orders by Age Group and Gender')
    plt.ylabel('Total Orders')
    plt.savefig('outputs/age_gender_analysis.png')
    plt.close()

    # 6. Sales by Channel
    channel_sales = df.groupby('Channel')['Amount'].sum()
    print("\n6. Sales by Channel:")
    print(channel_sales)
    
    plt.figure(figsize=(8, 8))
    plt.pie(channel_sales, labels=channel_sales.index, autopct='%1.1f%%', startangle=140)
    plt.title('Sales Distribution by Channel')
    plt.savefig('outputs/sales_by_channel.png')
    plt.close()

def main():
    file_path = 'Store_data_analysis.xlsx'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        return
    
    print(f"Loading data from {file_path}...")
    df = pd.read_excel(file_path)
    
    df = clean_data(df)
    df = feature_engineering(df)
    perform_analysis(df)
    
    print("\nAnalysis complete! Charts saved in 'outputs/' folder.")

if __name__ == "__main__":
    main()
