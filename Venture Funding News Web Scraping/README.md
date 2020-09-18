# VC Funding Scrap and Store (In Progress)

## Overall Project Goals
Analyzing data on new funding rounds and venture-funded companies, helping teams maximize the ROI of their new innovations / markets by:
- Collecting data on venture funding rounds and the venture-funded companies.
- Cleaning/formatting the collected data and sorting it by funding date and time.
- Storing information into various datatypes such as excel, csv and SQL.

## Abstract
  With data that is sourced from the website 'VCNewsDaily', this project collects information on new venture funding rounds, along with the details on the funding round and the venture-funded companies. This is done to develop a clean list of leads [for education purposes], that can be used for various purposes such as: product development, market research and/or business development.

## Intro
  Venture capital as a funding type offers huge potential rewards, but with huge risks as well. In fact, it is well-known that most venture-funded startups never make it to the initial public offering (IPO) stage (althought this might not always end up being the most ideal end-goal (i.e., acquisition vs IPO)). But for those that do go through multiple venture funds and make it to the IPO, this type of funding has been responsible for most (if not all) of the younger tech giants that are synonomous with Silicon Valley (i.e., Facebook, Google, Twitter, SalesForce, Uber, Doordash, Tesla). Given how venture capital works in stages, there is so much insight that venture funding reveals about developing trends in sales, culture and/or technology.
  
  A team that does a great job of tracking venture capital activity is 'VCNewsDaily'. Their website offers free venture capital details (funding round and company) on the 30 most recent funding rounds on their website at one time. They also have a basic search tool to search companies by letters, along with a full catalog of venture capital details available for purchase. The goal of the study is to interpret the HTML data from the VCNewsDaily website into clean data that is stored into excel sheets and an SQL database.
  
  While no further analysis was done on the venture capital funding activity in this study [after the data was scraped, cleaned and stored], this study does provide the baseline tool for web scraping the data that will be needed for such an educational study on venture capital funding in the future.

## Methods
The 'VCNewsDaily' website is great for finding details into recent fundings, although with limited search capabilities for non-paid tools outside of the last 30 fundings.

![](images/VCNewsDaily%20-%20Website%20Sample.PNG)

Instead, the raw HTML Data will be used by being collected, cleaned and stored.

![](images/VCNewsDaily%20-%20Website%20HTML%20Sample.PNG)

Data Exploration - Identifying and Merging Data

![](images/VCNewsDaily%20Data%20-%20Overview.PNG)
![](images/VCNewsDaily%20Data%20-%20Funding.PNG)
![](images/VCNewsDaily%20Data%20-%20Company.PNG)

## Results
- Data Cleaning
  - Raw Data
![](images/VCNewsDaily%20Data%20-%20Raw.PNG)
  - Prepping Data for Calculations
![](images/VCNewsDaily%20Data%20-%20Clean.PNG)
- Data Engineering
  - Managing SQL Server
![](images/VCNewsDaily%20Data%20-%20SQL%20Table.PNG)
  - Storing Data
![](images/VCNewsDaily%20Data%20-%20SQL.PNG)

## Discussion
  This study provided the baseline web scraping tool for building a list of venture-funded companies and their funding details/goals.
  
  Once collected and stored, this data can then be easily enriched and analyzed to help teams with market research, product development and/or business development. Market research from venture capital activity can be utilized by teams in the private equity and venture capital industries to help identify potential acquisitions / upcoming competitors. Product development teams in the various sciences industries (i.e., biotech, aerospace, electronics) can use VC activity to help identify upcoming technologies / methods that could offer parallel benefits to their own businesses. And business development teams can use VC activity to develop potential leads to go after (if good fit) or use it to systemically go through the targets in their CRM based on funding activity (i.e., similar industry / region).
