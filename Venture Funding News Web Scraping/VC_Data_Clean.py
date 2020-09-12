from VC_Data_Import import vc_csv_raw
import pandas as pd


def vc_data_format(dataframe):
    dataframe['Funding Date'] = pd.to_datetime(dataframe['Funding Date'])
    return dataframe


def vc_data_clean():
    vc_raw_data = vc_csv_raw()  # todo - replace with SQL after storing order fixed
    vc_raw_data['Funding Date'] = vc_data_format(vc_raw_data)
    vc_raw_data['City'] = vc_raw_data['City'].str.title()
    vc_raw_data['State'] = vc_raw_data['State'].str.replace(".", "")
    vc_raw_data['Funding Round Amount'] = vc_raw_data['Funding Round Amount'].str.strip('$')\
        .replace(',', '', regex=True).astype('float')
    vc_clean_data = vc_raw_data
    return vc_clean_data
