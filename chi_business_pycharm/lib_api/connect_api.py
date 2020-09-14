from sodapy import Socrata

"""
Functions for conecting to API and retrieving datasets. 
"""


def get_bus_lic_data():
    client = Socrata('data.cityofchicago.org', 'your-password-here')
    data_set = 'uupf-x98q'
    data = client.get(data_set,
                      query="""
                            SELECT
                            license_id, account_number, legal_name, doing_business_as_name,
                            business_activity, address, city, state, zip_code, license_description,
                            license_start_date, expiration_date  
                            LIMIT 100000
                            """)
    client.close()

    return data


def get_owners_data():
    client = Socrata('data.cityofchicago.org', 'your-password-here')
    data_set = 'ezma-pppn'
    data = client.get(data_set, query="""
                                            SELECT  
                                            account_number, owner_first_name, owner_last_name, owner_title                       
                                            LIMIT 300000                                          
                                            """)
    client.close()

    return data
