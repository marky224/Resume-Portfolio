# Project Summary
Through a dataset provided by the US government, cities in LA County will be grouped into clusters based on sociodemographic scores to develop benchmarks for each cluster. This will help city officials identify what are the biggest areas for improvement based on cluster (i.e., mental health to upper-class vs school quality to lower-class). Along with mapping out LA County based on socioeconomic clusters to help identify potential visual patterns.


## Introduction

With the national debt in the US being at an all-time high, having local levels of government being more efficient with their funds could be a great opportunity for most cities -- with LA being a great case study. Seeing how Los Angeles County is very diverse and has the largest population for a county in the United States (larger then 41 states individually), there is a lot that can be learned from studying its goverment policies and how socioecomonic standards can vary widely from city-to-city within LA. Depending on what part of Los Angeles you happen to be in, you can go from the mecca of the entertainment history (Beverly Hills) to areas that resemble 2nd and 3rd world countries (Skid Row, South Central) in a quick 10-20 minute drive. This is sad to see because there is no shortage of sympathy and tax-payer funding [in California] for people who want to get their life back together, but sadly it seems that most resources aren't making significant contributions in lowering homelessness and crime rates. A large part of the problem comes from not being able to efficiently prioritize public resources and zoning opportunities based on sociodemographic scores for each city. 

Given the size and complexity of LA County, one-size-fit-all approaches don't work, so instead we are going to use socioeconomic scores to create clusters of cities based on their data to help get a better understanding of LA. By grouping cities into clusters based on sociodemographic factors, this will allow city officiails to get a better understanding of why some programs work well for one socioeconomic group and not the others (i.e., housing projects benefitting upper-class and lower-class vs hurting middle-class). 

## Methods

This study will leverage data made available by the County of Los Angeles at (www.data.lacounty.gov/), titled the 'A Portrait of Los Angeles County using the Human Development Index: GIS Data' available at (www.data.lacounty.gov/Community/A-Portrait-of-Los-Angeles-County-using-the-Human-D/j7aj-mn8v). The goal of this study is to group cities within LA County into clusters of groups based on socioeconomic scores to help indentify population averages, socioeconomic benchmarks, and potential indicators of success (i.e., income, school enrollment, life expectancy, etc.). This study is going to be using unsupervised machine learning methods to cluster cities into groups, based on socioeconomic factors. The socioeconomic clusters map for LA County will also be mapped out according to help identify potential visual trends (for future studies).

Initial data analysis started with an initial heatmap, to find sociodemographic variables that are similar and should be removed.

![](Images/LA%20County%20Heatmap.PNG)

![](Images/LA%20County%20Heatmap%20Model.PNG)

![](Images/LA%20County%20Histograms.png)

- Data Exploration

Maps of LA County

![](Images/LA%20County%20Map.PNG)
![](Images/LA%20County%20Map%20-%20Bachelors%20Degree.PNG)
![](Images/LA%20County%20Map%20-%20Earnings.PNG)
![](Images/LA%20County%20Map%20-%20Graduate%20Degrees.PNG)
![](Images/LA%20County%20Map%20-%20Human%20Development%20Index.PNG)
![](Images/LA%20County%20Map%20-%20No%20HS%20Diplomas.PNG)
![](Images/LA%20County%20Map%20-%20School%20Enrollment.PNG)

PCA

![](Images/LA%20County%20Pairplot%20Model.PNG)

![](Images/LA%20County%20PCA.PNG)

![](Images/LA%20County%20Pairplot%20PCA.PNG)

![](Images/LA%20County%20Pairplot%20Model%20PCA.PNG)

## Results

![](Images/LA%20County%20Map%20-%20Model%20PCA.PNG)

![](Images/LA%20County%20Benchmarks.PNG)

## Discusssion

- Implications / Future Reseearch
