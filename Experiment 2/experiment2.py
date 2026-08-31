
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Superstore.csv")

print("\n========================================")
print("DATASET LOADED SUCCESSFULLY")
print("========================================")

print(df.head())

print("\n========================================")
print("DATASET INFORMATION")
print("========================================")

print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\n========================================")
print("CATEGORY DISTRIBUTION")
print("========================================")

if "Category" in df.columns:
    print(df["Category"].value_counts())

if "Region" in df.columns:
    print("\nRegion Distribution:")
    print(df["Region"].value_counts())

if "Segment" in df.columns:
    print("\nSegment Distribution:")
    print(df["Segment"].value_counts())
if "Sales" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Sales"],
        bins=30,
        kde=True
    )

    plt.title("Distribution of Sales")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.show()

if "Profit" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Profit"],
        bins=30,
        kde=True
    )

    plt.title("Distribution of Profit")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.show()

if "Category" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.countplot(
        data=df,
        x="Category"
    )

    plt.title("Number of Orders by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=20)
    plt.show()

if "Category" in df.columns and "Sales" in df.columns:

    category_sales = df.groupby(
        "Category"
    )["Sales"].sum().sort_values(ascending=False)

    print("\nSales by Category:")
    print(category_sales)

    plt.figure(figsize=(8, 5))

    category_sales.plot(
        kind="bar"
    )

    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=20)
    plt.show()

if "Category" in df.columns and "Profit" in df.columns:

    category_profit = df.groupby(
        "Category"
    )["Profit"].sum().sort_values(ascending=False)

    print("\nProfit by Category:")
    print(category_profit)

    plt.figure(figsize=(8, 5))

    category_profit.plot(
        kind="bar"
    )

    plt.title("Total Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Profit")
    plt.xticks(rotation=20)
    plt.show()

if "Region" in df.columns and "Sales" in df.columns:

    region_sales = df.groupby(
        "Region"
    )["Sales"].sum().sort_values(ascending=False)

    print("\nSales by Region:")
    print(region_sales)

    plt.figure(figsize=(8, 5))

    region_sales.plot(
        kind="bar"
    )

    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=20)
    plt.show()

if "Region" in df.columns and "Profit" in df.columns:

    region_profit = df.groupby(
        "Region"
    )["Profit"].sum().sort_values(ascending=False)

    print("\nProfit by Region:")
    print(region_profit)

    plt.figure(figsize=(8, 5))

    region_profit.plot(
        kind="bar"
    )

    plt.title("Total Profit by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Profit")
    plt.xticks(rotation=20)
    plt.show()

numeric_df = df.select_dtypes(
    include=np.number
)

correlation = numeric_df.corr()

print("\n========================================")
print("CORRELATION MATRIX")
print("========================================")

print(correlation)


plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()

if "Sales" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        x=df["Sales"]
    )

    plt.title("Box Plot of Sales")
    plt.xlabel("Sales")
    plt.show()

if "Profit" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        x=df["Profit"]
    )

    plt.title("Box Plot of Profit")
    plt.xlabel("Profit")
    plt.show()
if "Sales" in df.columns and "Profit" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Sales",
        y="Profit"
    )

    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.show()

if "Sales" in df.columns and "Quantity" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=df,
        x="Quantity",
        y="Sales"
    )

    plt.title("Quantity vs Sales")
    plt.xlabel("Quantity")
    plt.ylabel("Sales")
    plt.show()
if "Segment" in df.columns and "Sales" in df.columns:

    segment_sales = df.groupby(
        "Segment"
    )["Sales"].sum().sort_values(ascending=False)

    print("\nSales by Customer Segment:")
    print(segment_sales)

    plt.figure(figsize=(8, 5))

    segment_sales.plot(
        kind="bar"
    )

    plt.title("Sales by Customer Segment")
    plt.xlabel("Customer Segment")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=20)
    plt.show()
print("\n========================================")
print("BUSINESS INSIGHTS")
print("========================================")


if "Category" in df.columns and "Sales" in df.columns:

    best_category = df.groupby(
        "Category"
    )["Sales"].sum().idxmax()

    print(
        "1. Highest sales category:",
        best_category
    )


if "Region" in df.columns and "Sales" in df.columns:

    best_region = df.groupby(
        "Region"
    )["Sales"].sum().idxmax()

    print(
        "2. Highest sales region:",
        best_region
    )


if "Category" in df.columns and "Profit" in df.columns:

    best_profit_category = df.groupby(
        "Category"
    )["Profit"].sum().idxmax()

    print(
        "3. Most profitable category:",
        best_profit_category
    )


if "Segment" in df.columns and "Sales" in df.columns:

    best_segment = df.groupby(
        "Segment"
    )["Sales"].sum().idxmax()

    print(
        "4. Highest sales customer segment:",
        best_segment
    )


if "Sales" in df.columns and "Profit" in df.columns:

    correlation_value = df["Sales"].corr(
        df["Profit"]
    )

    print(
        "5. Correlation between Sales and Profit:",
        round(correlation_value, 3)
    )

print("\n========================================")
print("EDA COMPLETED SUCCESSFULLY")
print("========================================")

print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

print("\nAll major EDA analyses and visualizations completed.")