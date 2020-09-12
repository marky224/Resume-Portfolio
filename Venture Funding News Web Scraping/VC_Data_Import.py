# Function for grabbing raw html data from 'VC Daily News website'
import pandas as pd

# todo create virtual timer and initiative every weekday


def import_website_html(website_url):
    import requests  # Packages for requests
    from bs4 import BeautifulSoup  # Packaging for downloading website data via HTML
    website_html = BeautifulSoup(requests.get(website_url).text, "html.parser")
    return website_html


def vc_sql_engine():
    import sqlalchemy
    # Set SQL connection destination
    engine = sqlalchemy.create_engine(
        'mssql+pyodbc://@DESKTOP-OVRCKME/VCNewsDailyDB?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
    return engine


def vc_csv_raw():
    VC_csv_raw = pd.read_csv('VC_Data_Raw.csv')
    return VC_csv_raw


def vc_csv_clean():
    VC_csv_clean = pd.read_csv('VC_Data_Clean.csv')
    return VC_csv_clean


# todo - fix storing order in to_sql to use below
def vc_sql_raw():
    vc_raw_sql = pd.read_sql('SELECT * FROM VC_Data_Raw ORDER BY [Funding Date] DESC', vc_sql_engine())\
        .reset_index(drop=True)
    return vc_raw_sql


def vc_sql_clean():
    vc_clean_sql = pd.read_sql('SELECT * FROM VC_Data_Clean ORDER BY [Funding Date] DESC', vc_sql_engine())\
        .reset_index(drop=True)
    return vc_clean_sql


def reset_mode():
    hard_reset = 'False'
    return hard_reset
