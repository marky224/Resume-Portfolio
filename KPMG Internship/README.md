# Project Summary
Retail sales have been shown to be significantly effected by a variety of factors - from customer satisfaction, age, weather, lighting, e-commerce shopping trends. Understanding this, we're going to be helping a bike shop owner understand what customer features they should be focusing on in order to maximize the ROI of their marketing efforts and predict sales of new customers (for current and new markets) by analyzing their customer demographics, transaction history data, and leveraging other variables from outside data as needed (i.e., weather, google trends). The end goal is to help them develop data-driven client profiles based on their transaction data, along with predicting future sales of new customers based on their demographic information.

## Project Overview
Stage 1: Research Question:
- Allowing a bike shop owner to understand what customer features they should focus on in order maximize the ROI of their marketing efforts for current and new markets - by analyzing transaction history, customer data, and adding other relevant datasets (i.e., weather, crime rates, gas prices, etc) to predict new sales. (Why)
- By uncover underlying trends in seasonal sales, product features and customer demograhics that are significantly correlated with positive purchasing behaviors (i.e., sales volumne, profit). (How)
- Allowing teams to: understand which customer features drive higher customer lifetime value (and to what degree), develop ideal numbers of customer profiles based on data, and predict customer lifetime value for new customers based on their demograhics. (What)


Stage 2: Acquire Data
- Below

Stage 3: Data Exploration
- Below

Stage 4: Data Model
- Below

Stage 5: Data Communication
- Pending

## Project Outline
Analyzing customer and transaction data to allow a bike shop owner to maximize their marketing ROI for going into new markets by:
- Identify which customer features drive purchases (i.e., age, wealth, city) and understand to what degree they influence purchases
- Determine how many customer profiles should be developed, along with identifying feature averages for each customer profile
- Calculate customer lifetime value (CLV) for current customers and predicting CLV of new customers based on their feature profile

- Intial Analysis
  - Import
    - Download KPMG Dataset
    - Download Google Trend Info
      - Bike searches per region
    - Import add'l sociodemographic info (i.e., purchasing average, purchasing rate average, voting rates, political affliation, average income, eduation rates, average age, etc - per zip code)
    - Scrap and Format Weather Dataset (Temp, rainfall, etc)
    - Scrap real estate data (average sale price per zip code, average house valuation per community, etc)
    - Combine Datasets
  - Calculate 3 Year Customer Lifetime Value and Age
    - Download and Combine Add'l City Data
      - Leverage Relevant Social-Demographic Data
  - EDA
    - Display Dataset Features and Sizes for Customers, New Customers, Transactions and Demographic Data
    - Display Feature Averages for Customers, New Customers, Transactions and Demographic Data
    - Plot Annual Sales Trends for Customers
    - Plot Categorical vs Numerical Data for Customers and Transactions
    - Plot Correlation Heatmap for Customers
    - Display Highest Correlations for Customers
    - Display Feature Averages for Customers by Wealth Segment
    - Plot Annual Sales Trends by Wealth Segment
  - Feature Preprocessing
    - Label Encode Data
  - Feature Normalization
    - Identify and Log Transform Skewed Data
    - Normalize Data
  - Feature Engineering
    - Identify Percentages and Values to Create (i.e., Age Group)
    - Bin Values Accordingly
    - Drop/Combine Columns with Similar/Irrelevant Values (i.e., deceased. address)
  - Class Imbalance
    - Plot AOC and ROC Curves
  - Data Leakage
    - Perform K-Fold Cross-Validation
  - Unsupervised Machine Learning
    - PCA to Identify # Number of Clusters
    - Cluster Data with PCA
  - Supervised Machine Learning
    - Build Decision Tree Regression Model
  - Evaluation
    - Identify Predictive Score
    - Identify Feature Importance
- Refine Analysis and Results
  - Feature Preprocessing
    - Collect, Combine and Drop Additional Data, based on Important Features Identified
  - Feature Normalization
  - Feature Engineering
  - Class Imbalance
  - Data Leakage
  - Supervised Machine Learning
  - Evaluation
[Repeat 'Refine Analysis and Results' until prediction results are accurate]
- Cluster Analysis
  - Unsupervised Machine Learning
  - Supervised Machine Learning
- Display Results
  - Results
    - Display Model Predictive Power
    - Display Feature Averages and Customer Lifetime Value
    - Display Feature Importances
    - Graph Annual Sales Trends
    - Display Ideal Number of Customer Profiles / Clusters
    - Display Feature Averages and Customer Lifetime Value by Ideal Customer Profile
    - Display Model Predictive Power by Customer Profile
    - Display Feature Averages by Customer Profile
    - Display Customer Lifetime Value by Customer Profile
    - Display Feature Importances by Customer Profile
    - Graph Annual Sales Trends by Customer Profile

References
 - [Customer satisfaction and retail sales performance: an empirical investigation(https://www.sciencedirect.com/science/article/abs/pii/S0022435904000594)
 - [The effects of weather on retail sales](https://ideas.repec.org/p/fip/fedgfe/2000-08.html)
 - [The Effects of Technology on Retail Sales, Commercial Property Values and Percentage Rents](https://aresjournals.org/doi/abs/10.5555/repm.6.2.y2002k2632757j07)
 - [The Importance of Weather for E-Commerce Orders Forecasting](https://dl.acm.org/doi/abs/10.1145/3385061.3385064)
 - [Whether Weather Matters: Impact of Exogenous Factors on Customers Channel Choice](https://link.springer.com/chapter/10.1007/978-3-030-20119-7_10)
 - [Statistical Machine Learning Model for Stochastic Optimal Planning of Distribution Networks Considering a Dynamic Correlation and Dimension Reduction](https://ieeexplore.ieee.org/abstract/document/8999581)
 - [Exploring the implementation blind spots Selective Decoupling of Freedom of Information](https://www.semanticscholar.org/paper/Exploring-the-implementation-blind-spots-Selective-Kuk/ec1f111b1e53122dc0abec491ce91eff5611f987)
