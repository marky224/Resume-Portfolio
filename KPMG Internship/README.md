# Project Summary (Work in progress)
## Using CRM Data to Identify Important Factors for Ideal Customer Profile

Abstract:

Through a dataset provided by KPMG, an Australian bicycle shop owner was looking to maximize their marketing ROI by analyzing data on their customers and transactions for the past 3 years. This was accomplished by developing customer profiles based on data, along with predicting new sales that referenced data on previous transactions and customer demographics. Results provided a data-driven ideal customer profile, along with a baseline predictive model for customers that have been in the CRM for longer then 3 years.

Introduction:

  As online sales continue to grow for most companies, so is the importance of using online marketing to help drive in-store traffic/sales as well. And while most companies are doing a great job of acquring and storing their customers' information into a customer relationship management (CRM) database via rewards programs and email lists, most companies are having a tough time using that data to help drive new sales from there.
  
  In this study, an Australian bike shop owner overcame this dilemma (to maximize their marketing ROI) by using their CRM data on transactions and customers for the past 3 years. Our goals were to identify yearly and monthly trends in sales, identify profitable customer segments and bike lines, identify top-selling bike lines and top-purchasing customers, and identify customer traits associated with higher profits / more frequent purchases. By analyzing the data and looking for trends, this allowed for the creation of a data-driven customer profile, along with a potential model to help predict new sales for individual customers in real-time.

Methods:

The study's dataset came from a KPMG virtual internship for a bicycle shop based in Australia, with the dataset being modeled after similiar customer datasets that have similar business profiles. The data came in an excel sheet and included four sets of data: Customer Demographic, Customer Address, Transactions, New Customers (Address and Demographics). The 'New Customers' dataset was disregarded since 'Transactions' only had 'customer ID' numbers that were associated with the 'Customer' dataset. For the initial data quality check, duplicates in 'Customer ID' were checked for and none were found. The data completeness check then showed that Customer Demographic had 96.61% complete data, Customer Address had 100% complete data, and Transactions had 100% complete data. For the initial data clean, the datasets were merged together for 'Customer Demographic' and 'Customer Address'. Then the columns without relevant data were removed, along with removing the rows that did not have a date of birth. Customer rows were also removed for those who were marked as deceased and/or born before 1900.

Results:

The initial results showed two seasonal spikes in monthly sales due to both summer weather and holiday shopping, with sales ramping up in June and then slowing down in September, before ramping back up again in October and slowing back down in December.

![](images/Transactions%20by%20Month.png)

Our results after that showed us while most bikes sales came from bike types that were either 'standard' or 'road', the bike types 'mountain' and 'road' proved to be a lot more profitable.

![](images/Transactions%20by%20Bike.PNG)

We further look into any potential trends in sales by bike types by looking to see if there are any trends that appear in monthly sales -- to see if it would make sense to focus advertisement for these bike lines on certain times of the year. Unfortunately, we found no such monthly trends in bike sales by bike type, with bike sales by bike types following similar trends overall.

![](images/Transactions%20by%20Bike%20-%20Monthly.PNG)

Then we start our initial exploration into the customer based to find any trends and see that most of the customer base seems to be concentrated between 1971 to 1981 -- which makes our most popular age group people between 40 and 50 years of age.

![](images/Customers%20by%20DOB.png)

We further explore our customers by seeing how many bikes they have purchased from the store in the last 3 years. We see that 3 to 8 bike purchases covers the majority of customers - so 1 to 3 annual bike purchases per customer seems to be the average.

![](images/Average%20Customer%20Transactions.PNG)

What was uncovered in the transaction dataset is the clear difference in profitability by wealth segment, with the customer group 'mass customer' being twice as profitable as the other two groups 'affluent' and 'high net worth'.

![](images/Average%20Profit%20per%20Transaction%20by%20Wealth.png)

After uncovering the significant differences in profit by customer segment, we map out our customers by wealth segment (color) and total profits by bubble density. We didn't uncover any specific geographic trends as they related to differences in customers by customer group - other then sales concentrated among major cities along the coast.

![](images/Map%20Bike%20Sales%20by%20Profit%20-%20North.PNG)

![](images/Map%20Bike%20Sales%20by%20Profit%20-%20South.PNG)

We also explore customers by date of birth and wealth, but see customers in each group had a similiar distribution to the overall customer age trend (40 - 50 years old).

![](images/Customers%20by%20Wealth%20by%20Birth%20Year.png)

Given the differences in customers by wealth group, one last thing that stood out from a geographic standpoint, is that most customers reside in areas that have similar property values -- with 7 to 11 being the most popular range.

![](images/Property%20Values.png)

Discussion:

So from our exploration of the data, we can see how their is an ideal customer profile for this bike shop in the form of some who is between 40 to 50 years of range, within their 'mass customer' group, with property values ranging between 7 to 11. And while our original goal of the study was to also develop a predictive model to help determine new purchases, we weren't able to create a successful model without reference the total number of bikes purchases that had been made in the past 3 years. While this was something that was taken out to help the adaptability of the model onto real data, in retrospect, this is something that can be further explore by cutting the number of transactions to the last one or two years, in order to help with newer customers as well -- with no model being applied to customers under one or two years of age within the CRM. Age of customer record wasn't included in the dataset, so this is something that could help with similiar data in the future.
