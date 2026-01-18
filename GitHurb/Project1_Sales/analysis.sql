-- Project 1: Sales Analysis SQL Scripts
-- This script contains queries for common business metrics

-- 1. Total Sales and Profit by Category
SELECT 
    Category, 
    SUM(TotalSales) AS TotalRevenue, 
    SUM(Profit) AS TotalProfit,
    (SUM(Profit) / SUM(TotalSales)) * 100 AS ProfitMargin
FROM sales_data
GROUP BY Category
ORDER BY TotalRevenue DESC;

-- 2. Monthly Sales Trend
SELECT 
    STRFTIME('%Y-%m', Date) AS Month, 
    SUM(TotalSales) AS MonthlyRevenue
FROM sales_data
GROUP BY Month
ORDER BY Month;

-- 3. Top 5 Products by Sales
SELECT 
    Product, 
    SUM(TotalSales) AS TotalRevenue
FROM sales_data
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 5;

-- 4. Regional Performance
SELECT 
    Region, 
    SUM(TotalSales) AS TotalRevenue,
    COUNT(OrderID) AS OrderCount
FROM sales_data
GROUP BY Region
ORDER BY TotalRevenue DESC;
