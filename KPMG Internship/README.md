# Project Summary (Work in progress)
## Using CRM Data to Identify Important Factors for Ideal Customer Profile

Abstract:

Through a dataset provided by KPMG, an Australian bicycle shop owner was looking to maximize their marketing ROI by analyzing data on their customers and transactions for the past 3 years. This was accomplished by developing customer profiles based on data, along with predicting new sales that referenced data on previous transactions and customer demographics. Results provided a data-driven ideal customer profile, along with a predictive model to start off as a base.

Introduction:

  As online sales continue to grow for most companies, so is the importance of using online marketing to help drive in-store traffic/sales as well. And while most companies are doing a great job of acquring and storing their customers' information (via rewards programs and email lists) into a customer relationship management (CRM) database, most companies are having a tough time using that data to help drive new sales from there.
  
  In this study, an Australian bike shop owner overcame this dilemma (and will hopefully be maximizing their marketing ROI) when they used their CRM data on transactions and customers for the past 3 years. By analyzing the data and trends, this allowed for the creation of a data-driven customer profile, along with a potential predictive models to help predict new sales for individual customers in real-time. Our goals were to identify yearly and monthly sales trends, identify profitable customer segments and bike lines, identify top-selling bike lines and top-purchasing customers, and identify the customer traits associated with higher profits / more frequent purchases.

Methods:

The study's dataset came from a KPMG virtual internship for a bicycle shop based in Australia, with the dataset being modeled after similiar datasets from customers that have similar business profiles. The dataset came in the form of an excel sheet and included the followed four datasets: Customer Demographic, Customer Address, Transactions, New Customers (Address and Demographics). The dataset for 'New Customers' was disregarded since 'Transactions' only had customer ID numbers for the 'Customer' dataset. For the initial data quality check, we checked for duplicates in Customer ID We also checked the completeness of our data to see that Customer Demographic had 96.61% of complete data, Customer Address had 100% of complete data and Transactions also had 100% of complete data. For our initial data clean, we merged the datasets Customer Demographic and Customer Address together, and then we removed the columns without relevant data and also removed the rows without date of births. We also removed customers who were also marked as deceased and/or born before 1900.

Results:

Our initial results showed us a seasonal spikes in monthly sales due to both summer weather and holiday shopping, with sales ramping up in June and then slowing down in September, before ramping back up again in October and slowing back down in December.

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
