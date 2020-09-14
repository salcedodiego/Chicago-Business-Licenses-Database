"""
Contains functions that writes MySQL queries in a .txt file to be copied and paste in a MySQL script for inserting data.
"""


def write_buss_query(df):
    """
    Generates query for "business" table.
    """
    with open('bus_table_query.txt', 'w') as file:
        boolean = True
        while boolean:
            row = 0
            t = 1
            size = df.shape[0]
            limit = 1000  # limit for MySLQ multiple inserting data
            while t != 0:
                file.write('INSERT INTO business VALUES\n')
                for i in range(limit):  # iterate 1000 times
                    lic_id = df['license_id'].iloc[row]
                    acct_no = df['account_number'].iloc[row]
                    legal_name = df['legal_name'].iloc[row]
                    dba = df['doing_business_as_name'].iloc[row]
                    bus_act = df['business_activity'].iloc[row]
                    if row == size-1:  # exit "for loop" at last data entry
                        file.write(f'({lic_id},{acct_no},"{legal_name}","{dba}","{bus_act}");')
                        row += 1
                        break
                    elif i == limit-1:  # end of query after 1000 entries reached
                        file.write(f'({lic_id},{acct_no},"{legal_name}","{dba}","{bus_act}");\n')
                    else:
                        file.write(f'({lic_id},{acct_no},"{legal_name}","{dba}","{bus_act}"),\n')
                    row += 1
                if row == size:  # exit "while t != 0 loop" at last data entry
                    t = 0
            boolean = False  # Exit "while True loop" and end function


def write_loc_query(df):
    """
        Generates query for "business_loc" table
    """
    with open('loc_table_query.txt', 'w') as file:
        boolean = True
        while boolean:
            row = 0
            t = 1
            limit = 1000  # limit for MySLQ multiple inserting data
            size = df.shape[0]
            while t != 0:
                file.write('INSERT INTO license_loc VALUES\n')
                for i in range(limit):  # iterate 1000 times
                    lic_id = df['license_id'].iloc[row]
                    address = df['address'].iloc[row]
                    city = df['city'].iloc[row]
                    state = df['state'].iloc[row]
                    zip_code = df['zip_code'].iloc[row]
                    if row == size-1:  # exit "for loop" at last data entry
                        file.write(f'({lic_id},"{address}","{city}","{state}",{zip_code});')
                        row += 1
                        break
                    elif i == limit-1:  # end of query after 1000 entries reached
                        file.write(f'({lic_id},"{address}","{city}","{state}",{zip_code});\n')
                    else:
                        file.write(f'({lic_id},"{address}","{city}","{state}",{zip_code}),\n')
                    row += 1
                if row == size:  # exit "while t != 0 loop" at last data entry otherwise keep iterating
                    t = 0
            boolean = False


def write_lic_query(df):
    """
        Generates query for "business_lic" table
    """
    with open('lic_table_query.txt', 'w') as file:
        boolean = True
        while boolean:
            row = 0
            t = 1
            limit = 1000  # limit for MySLQ multiple inserting data
            size = df.shape[0]
            while t != 0:
                file.write('INSERT INTO license_info VALUES\n')
                for i in range(limit):  # iterate 1000 times
                    lic_id = df['license_id'].iloc[row]
                    descr = df['license_description'].iloc[row]
                    start = df['license_start_date'].iloc[row]
                    end = df['expiration_date'].iloc[row]
                    if row == size-1:  # exit "for loop" at last data entry
                        file.write(f'({lic_id},"{descr}","{start}","{end}");')
                        row += 1
                        break
                    elif i == limit-1:  # end of query after 1000 entries reached
                        file.write(f'({lic_id},"{descr}","{start}","{end}");\n')
                    else:
                        file.write(f'({lic_id},"{descr}","{start}","{end}"),\n')
                    row += 1
                if row == size:  # exit "while t != 0 loop" at last data entry otherwise keep iterating
                    t = 0
            boolean = False


def write_owners_query(df):
    """
        Generates query for "owners" table
    """
    with open('owners_table_query.txt', 'w') as file:
        boolean = True
        while boolean:
            row = 0
            t = 1
            limit = 1000  # limit for MySLQ multiple inserting data
            size = df.shape[0]
            while t != 0:
                file.write('INSERT INTO owners VALUES\n')
                for i in range(limit):
                    acct_no = df['account_number'].iloc[row]
                    first_name = df['owner_first_name'].iloc[row]
                    last_name = df['owner_last_name'].iloc[row]
                    title = df['owner_title'].iloc[row]
                    if row == size-1:  # exit "for loop" at last data entry
                        file.write(f'({acct_no},"{first_name}","{last_name}","{title}");')  # changing for testing
                        row += 1
                        break
                    elif i == limit-1:  # end of query after 1000 entries reached
                        file.write(f'({acct_no},"{first_name}","{last_name}","{title}");\n')
                    else:
                        file.write(f'({acct_no},"{first_name}","{last_name}","{title}"),\n')
                    row += 1
                if row == size:  # exit "while t != 0 loop" at last data entry otherwise keep iterating
                    t = 0
            boolean = False
