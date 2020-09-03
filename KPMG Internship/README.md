# Project Summary (Work in progress)
## Identifying Ideal Customers and Predicting New Sales with CRM Data

Abstract:

Through a dataset provided by KPMG, we're going to be helping a bicycle shop owner maximize their marketing ROI by using their historical data on customers and transactions. Developing customer profiles based on data and helping to estimate news sales based off of previous transactions and customer demographic information.


Introduction:

  As online sales continue to grow as a sales channel for most companies, so is the importance of using online marketing to help drive in-store traffic and sales as well. And while most companies are doing a great job of acquring and storing their customers' information (via rewards programs and email lists) into a customer relationship management (CRM) database, most companies are having a tough time using that data to help drive new sales.
  
  In this study, we're going to be helping a bike shop owner maximize their historical data on their customers and transactions, to keep marketing focused on the customer segments that are most profitable and drive the most sales. With the goal of identifying the most profitable bike lines and customer segments, along with identifying which customer traits are associated with higher profits and more frequent purchases.

Methods:

Our study's dataset came from a KPMG virtual internship for a bicycle shop based in Australia, with the dataset being modeled after customer datasets that have similar business profiles. The dataset came in the form of an excel sheet and included the followed four datasets: Customer Demographic, Customer Address, Transactions, New Customers (Address and Demographics). The dataset for 'New Customers' was disregarded since 'Transactions' only had customer ID numbers for the 'Customer' dataset. For the initial data quality check, we checked for duplicates in Customer ID We also checked the completeness of our data to see that Customer Demographic had 96.61% of complete data, Customer Address had 100% of complete data and Transactions also had 100% of complete data. For our initial data clean, we merged the datasets Customer Demographic and Customer Address together, and then we removed the columns without relevant data and also removed the rows without date of births. We also removed customers who were also marked as deceased and/or born before 1900.

Results:

Our initial results showed us a seasonal spikes in monthly sales due to both summer weather and holiday shopping, with sales ramping up in June and then slowing down in September, before ramping back up again in October and slowing back down in December.

![](images/Transactions%20by%20Month.png)

Our results after that showed us while most bikes sales came from bike types that were either 'standard' or 'road', the bike types 'mountain' and 'road' proved to be a lot more profitable.

![](images/Transactions%20by%20Bike.PNG)
We further look into any potential trends in sales by bike types by looking to see if there are any trends that appear in monthly sales -- to see if it would make sense to focus advertisement for these bike lines on certain times of the year. Unfortunately, we found no such monthly trends in bike sales by bike type.

![](images/Transactions%20by%20Bike%20-%20Monthly.PNG)

Discussion:

Title:

- Predicting Profits from New Customers based on Sociodemographic Data

Abstract:
