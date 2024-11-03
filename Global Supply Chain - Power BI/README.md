# Global Supply Chain Analysis

## Table of Contents

- [Introduction](#introduction)
- [Data Cleaning](#data-cleaning)
- [Analysis and Insights](#analysis-and-insights)
  - [Executive Summary](#executive-summary)
    - [Observations](#observations)
    - [Actionable Insights](#actionable-insights)
  - [Customer Insights](#customer-insights)
    - [Observations](#observations-1)
    - [Actionable Insights](#actionable-insights-1)
  - [Shipping and Delivery](#shipping-and-delivery)
    - [Observations](#observations-2)
    - [Actionable Insights](#actionable-insights-2)

## Introduction
This project deals with Visualization and Analysis of the given Supply chain dataset. This dataset was obtained from [here](https://data.mendeley.com/datasets/8gx2fvg2k6/5/files/29dc7b05-dda6-4834-8354-5b5cc44430df). By the means of this project, we aim to uncover some business insights from this dataset by using various visualizations and metrics. We do this by first performing the initial cleaning of this dataset by removing the redundant columns and rows from this dataset.

## Data Cleaning
The original dataset contained 53 columns, out of which we removed 6 columns, namely `Customer Email`, `Customer Password`, `Product Image`, `Product Status`, `Product Description` and `Order Zipcode`. The reasons for removing these columns are below. We removed the orders with an order status of `Suspected_Fraud`.
- Customer Email – This column contains masked values in the form of `XXXXXXXXX`
- Customer Password – This column contains masked values in the form of `XXXXXXXXX`
- Product Image – This column contains link to the product listing, which cannot be used in anyway to derive insights.
- Product Status – This column contains `0` throughout all the rows.
- Product Description – This column is empty and does not contain any value. 
- Order Zipcode – This column has 97% of empty values, therefore not having sufficient data to keep this column for even any future analysis purposes.

The first column of this dataset “Type” has been changed to “Transaction Type” for clarity purposes. 

## Analysis and Insights
Next we create a Dashboard which is spread across 3 pages and which spans the 3 areas namely :  
1.	Executive Summary 
2.	Customer Insights
3.	Shipping and Delivery

### Executive Summary

![Executive Summary](https://github.com/VipulSharma95/Portfolio_Projects/blob/main/Global%20Supply%20Chain%20Power%20BI/Supply%20Chain%20Power%20BI_Page1.jpg)


This is the first page of our Dashboard, and it depicts the information which would concern the higher management by presenting an overall view of company’s performance. This page contains metrics for Total Orders, Total Sales, On-Time Delivery Percentage and Order Profit Margin along with the visualizations of `Sales by Order Country`, `Total Profit by Market`, `Total Sales over Time`. This page also contains 2 slicers for `Order Date` and `Department` to see visualizations for specific Dates and Departments.

#### Observations 
- Over the entire time period of Dataset, there were a total of ~`64,000` orders with a total sale of `$32.31` Million.
- The On-Time Delivery Percentage for the entire time duration was only `41.82%`.
- The order profit margin of `0.12`, shows that average profit margin percentage for all orders is `12%`.
- Total Sales and Profit by Order Country/Market are in the descending order from Europe, LATAM, Pacific Asia, USCA and Africa. 

#### Actionable Insights
- The On-Time Delivery Percentage of only 41.82% shows that less than half of the orders are delivered on time. This presents glaring problems which would result in the higher churn rates of customers for better alternatives. Higher Management should take urgent steps to refine operations supply chain to improve this key metric, which is crucial for driving the company’s business and is a deciding factor for the company’s future performance.
- An increase in the efficiency of the company’s supply chain would reduce losses and would improve bottom line for the company. It would also help in attracting interests of various investors, which would further help the company in its future expansion and acquisition plans.  
- The drastic fall towards the end of the period in Total Sales graph shows that we do not have complete data for January 2018.

### Customer Insights

![Customer Insights Dashboard](https://github.com/VipulSharma95/Portfolio_Projects/blob/main/Global%20Supply%20Chain%20Power%20BI/Supply%20Chain%20Power%20BI_Page2.jpg)

This is the second page of our Dashboard, it depicts the information about customer base of the company which would be important to Customer Acquisition and Marketing Team by presenting `Total Sales by Customer Segments`, `Customers by Country`, `Top 10 Customers by Sales` and `Customers by Transaction Type`. This page also contains 2 slicers as described for the previous page. 

#### Observations
- Highest sales were recorded for “Consumer” segment with the sales of $16.7M.
- Majority of the customers (12,607) belonged to “EE. UU.” Country (No specific instructions regarding further details about this name were provided by the source of this dataset).
- The most popular medium of transaction has been Debit (33.81%) followed by Transfer (26.46%) followed by other mediums.

#### Actionable Insights
- The total sales from “Corporate” segment are around half of that “Consumer” segment. Corporate Segment is essential to any business, this is because the volume of orders/sales per customer is generally much higher for a customer from “Corporate” segment than a customer from “Consumer” segment. Therefore, targeted advertising should be done for “Corporate” segment to improve the sales from this segment.
- Special offers, discounts and dedicated relationship team should be provided to top 10 customers by sales. 
- Since Customers primarily use debit and transfer as payment medium, further technological advancements should be done for these payment mediums to facilitate customers with faster and hassle-free payments. 

### Shipping and Delivery

![Shipping and Delivery](https://github.com/VipulSharma95/Portfolio_Projects/blob/main/Global%20Supply%20Chain%20Power%20BI/Supply%20Chain%20Power%20BI_Page3.jpg)

This is the last page of our Dashboard, it depicts the information about the performance of supply chain and logistics of the company which would be important to Operations and Supply Chain Team by presenting metrics of `Average Order Processing Time`, `Average Shipping Delay`, `Late Delivery Risk` and visualizations of `Late Delivery Risk by Markets`, `Orders by Delivery Status`, `Shipping Days (Real vs Scheduled)` and `Shipping Delay by Order Country`. This page also contains 2 slicers as described for the first page. 

#### Observations
- LATAM and Europe markets are prone to late deliveries as compared to other regions.
- On average the shipment gets delayed across all the regions with an overall average of delay being `0.57` Days.
- 56.09% of orders are delivered late followed by 23.01% orders being shipped in advance.
- An average order takes 3.5 Days to be processed with an overall late delivery risk of 56.09%.
- Also 59.81% of the orders were shipped with "Standard Class" shipping service, followed by 19.47% of the orders being shipped with "Second Class" shipping service which are followed by other services. 

#### Actionable Insights
- There is a late delivery risk of an alarming rate of ~56%, which is a big concern and should be immediately addressed by Supply Chain and logistics team by resolving the bottlenecks which exists throughout the process chain. Such high levels of Late Delivery Risk would lead to customers opting out of the company’s services
- A further drill down may indicate that majority of the late deliveries occur with the "Standard Shipping" service, which might further indicate high attrition rates in the near future because majority of the customers use "Standard Shipping" service and due to unsatisfactory service, they would move towards the competitors instead.
- An average shipping delay of 0.57 days shows a bottleneck to be present at the dispatching warehouse, which should be resolved first after which the resolution should move towards the later stages of shipping.
- More advanced systems should be employed by the company to further reduce order processing times, which would further result in lesser delivery times.
- A further analysis of Shipping delays by countries can help the Operations and Supply chain team to resolve various supply chain specific to each country.
