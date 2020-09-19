# Real Estate Price Predictor - Kaggle Rebuild

## Project Goals

Analyzing data on historical real estate sales to help a potential buyer find undervalued properties by:
- Analyzing and exploring how the general real estate market is broken down (i.e., price, square feet, stories)
- Analyze how different house features effect sale prices for houses
- Predict the price of sale of a house based on features and location

## Abstract

Through a dataset provided by Kaggle for a data science competition, this project analyzes real estate data in the Boston market to help a potential home buyer maximize the ROI of their new home purchase. By determining the house's value of different features (i.e., bathrooms vs floors) and predicting sale prices based on house features to find undervalued houses currently available to buy.


## Introduction

This project's task comes from a Kaggle competition.
![](images/Real%20Estate%20-%20Kaggle%20Competition.PNG)

Our project's task was to rebuild an end-to-end project that had made it to the top 0.3%.
![](images/Real%20Estate%20Project%20Model.PNG)

The project's task is to identify house features that help predict the price of a house when it is sold, and build a predictive model accordingly.

![](images/Real%20Estate%20Sale%20Price.PNG)

The initial data analysis involved using a heatmap to help identify features that have [higher and lower] correlations with our target feature 'Sale Price'.

![](images/Real%20Estate%20Heatmap.PNG)

The features that had higher and lower correlations with 'Sale Price' were plotted against each other for an initial visual analysis.

![](images/Real%20Estate%20Pairplot.PNG)

## Methods

Missing features in the data were then investigated, but none of the correlated features investigated [above] had any significant problems with missing data. Our missing data was imputted by averaging missing house features (i.e., lot square feet) by zip code.

![](images/Real%20Estate%20Missing%20Features.PNG)

To help prevent overfitting when working with real-world data, a logarithm transformation was applied to the target feature 'Sale Price'.

![](images/Real%20Estate%20Sale%20Price%20Log.PNG)

## Results

- Data Model

- Data Results

## Discussion

- Implications and Further Research
