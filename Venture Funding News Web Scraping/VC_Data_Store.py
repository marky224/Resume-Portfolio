from VC_Data_Import import vc_sql_engine
import os
os.chdir('C:\\Users\\marky\\PycharmProjects\\VC Scrap and Store\\')


def vc_data_store_raw():
    from VC_Data_Raw import vc_data_raw
    VC_data_raw = vc_data_raw()
    VC_data_raw.to_sql('VC_Data_Raw', con=vc_sql_engine(), if_exists='replace', index=False)
    VC_data_raw.to_csv('VC_Data_Raw.csv', index=False)
    # todo - figure out order for SQL
    return


def vc_data_store_clean():  # Store Clean Data
    from VC_Data_Clean import vc_data_clean
    VC_data_clean = vc_data_clean()
    VC_data_clean.to_sql('VC_Data_Clean', con=vc_sql_engine(), if_exists='replace', index=False)
    VC_data_clean.to_csv('VC_Data_Clean.csv', index=False)
    return


vc_data_store_raw()
vc_data_store_clean()


# todo - add function for storing enriched data
