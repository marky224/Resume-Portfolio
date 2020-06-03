## Project Overview
Stage 1: Research Question:
- Allowing a bike shop owner to understand what customer features they should focus on in order maximize the ROI of their marketing efforts when entering new markets - by analyzing transaction history, customer data, and adding other relevant datasets (i.e., weather, crime rates. etc) to predict sales. (Why)
- To uncover underlying trends in seasonal sales, product features and customer demograhics that are significantly correlated with positive purchasing behaviors (i.e., sales volumne, profit). (How)
- Allowing teams to understand: which customer features drive higher customer lifetime value (and to what degree), develop ideal numbers of customer profiles based on data, and predict customer lifetime value for new customers based on their demograhics. (What)

Stage 2: Acquire Data
- A

Stage 3: Data Exploration
- A

Stage 4: Data Model
- A

Stage 5: Data Communication
- A

## Project Outline
Analyzing customer and transaction data to allow a bike shop owner to maximize their marketing ROI for going into new markets by:
- Identify which customer features drive purchases (i.e., age, wealth, city) and understand to what degree they influence purchases
- Determine how many customer profiles should be developed, along with identifying feature averages for each customer profile
- Calculate customer lifetime value (CLV) for current customers and predicting CLV of new customers based on their feature profile

- Intial Analysis
  - Import
    - Download and Combine KPMG Dataset
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
