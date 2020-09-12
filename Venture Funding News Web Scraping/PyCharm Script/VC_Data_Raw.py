from VC_Data_Import import import_website_html, vc_csv_clean, reset_mode
import pandas as pd


def vc_market_data():
    import os
    os.chdir('C:\\Users\\marky\\PycharmProjects\\VC Scrap and Store\\')
    website_url = 'https://vcnewsdaily.com/'
    vc_market_urls = import_website_html(website_url).find_all('div', class_='col-md-8')
    vc_market_data_ = pd.DataFrame([[vc_market_urls[i].small.text, vc_market_urls[i].h5.text,
                                     vc_market_urls[i].a.get('href')] for i in range(len(vc_market_urls))],
                                   columns=['Funding Date', 'Funding Title', 'Market Article URL'])
    return vc_market_data_


VC_market_data = vc_market_data()


def vc_new_data():
    if reset_mode() == 'True':
        vc_market_data_new = VC_market_data
    else:
        current_vc_market_urls = vc_csv_clean()['Market Article URL']  # change back to vc_sql_raw when fixed
        new_vc_market_urls = VC_market_data['Market Article URL']
        vc_market_data_new = VC_market_data[~new_vc_market_urls.isin(current_vc_market_urls)]
    return vc_market_data_new


VC_new_data = vc_new_data()


def vc_funding_data():
    vc_market_urls = VC_new_data['Market Article URL']  # Hard reset / Reading in only new URLs
    vc_funding_list = []
    for company in range(len(vc_market_urls)):
        vc_funding_html = import_website_html(vc_market_urls[company])
        funding_headline = vc_funding_html.find_all(id='summary')[0].text.strip('\n').strip('\t')
        if len(funding_headline.split(', ')) > 1:
            company_city = funding_headline.split(', ')[0]
            company_state = funding_headline.split(', ')[1]
        else:
            company_city = None
            company_state = None
        website_company_link = vc_funding_html.find_all(id='fullArticle')[0].a.get('href')
        funding_article = vc_funding_html.find_all(id='fullArticle')[1].text
        vc_funding_list.append([funding_headline, company_city, company_state, website_company_link, funding_article])
    vc_funding_list = pd.DataFrame(vc_funding_list, columns=['Funding Headline', 'City', 'State', 'Company Website URL',
                                                             'Funding Article'])
    return vc_funding_list


VC_funding_data = vc_funding_data()


def vc_company_data():
    vc_funding_urls = VC_funding_data['Company Website URL']
    vc_company_list = []
    for company in range(len(vc_funding_urls)):
        company_html = import_website_html(vc_funding_urls[company])
        company_name = company_html.find(class_='col-md-7 d-flex align-items-center').h5.text
        company_desc = company_html.find(class_='mt-5').p.text
        if len(company_html.find_all('td')) > 1:
            if len(company_html.find_all('td')[-2].text.strip('\n')) > 1:
                funding_type = company_html.find_all('td')[-2].text.strip('\n')
            else:
                funding_type = None
            funding_amount = company_html.find_all('td')[-3].text.strip('\n')
            if funding_amount == 'undisclosed':
                funding_amount = None
        else:
            funding_type = None
            funding_amount = None
        vc_company_list.append([company_name, company_desc, funding_type, funding_amount])
    vc_company_list = pd.DataFrame(vc_company_list, columns=['Company Name', 'Company Description',
                                                             'Funding Round Type', 'Funding Round Amount'])
    return vc_company_list


def vc_data_raw():
    from VC_Data_Import import vc_csv_raw, reset_mode
    vc_raw_data = pd.concat([VC_new_data, VC_funding_data, vc_company_data()], axis=1).reset_index(drop=True)
    if reset_mode() == 'False':
        # todo - replace with SQL after storing order fixed
        vc_raw_data = vc_raw_data.append(vc_csv_raw(), ignore_index=True)
    return vc_raw_data
