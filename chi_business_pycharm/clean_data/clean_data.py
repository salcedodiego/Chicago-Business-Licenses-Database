import pandas as pd


class DataPrep:
    """
    Contains functions that perform data cleaning operations.
    """

    def __init__(self, lic_bus, owners):
        self.lic_bus = pd.DataFrame(lic_bus)
        self.owner = pd.DataFrame(owners)

    def zip_code_fix(self):
        """
        Replaces non-numeric Zip Code entries.
        """
        for i in range(self.lic_bus.shape[0]):
            try:
                self.lic_bus.zip_code.loc[i] = int(self.lic_bus.zip_code.loc[i])
            except ValueError:
                self.lic_bus.zip_code.loc[i] = '00000'

    @property
    def bus_lic(self):
        # Filling null values
        self.lic_bus.city.fillna('Chicago', inplace=True)
        self.lic_bus.doing_business_as_name.fillna('Not Provided', inplace=True)
        self.lic_bus.business_activity.fillna('Not Provided', inplace=True)
        self.lic_bus.license_start_date.fillna('0000-00-00', inplace=True)
        self.lic_bus.zip_code.fillna('00000', inplace=True)

        # Treatment for string entries.
        DataPrep.zip_code_fix(self)
        self.lic_bus.city = self.lic_bus.city.apply(lambda x: x.title())
        self.lic_bus.address = self.lic_bus.address.apply(
            lambda x: x.title().replace('Th', 'th').replace('1St', '1st').replace('Th', 'th').replace('Nd',
                                                                                                      'nd').replace('"',
                                                                                                                    "'").replace(
                'Rd', 'rd'))
        self.lic_bus.doing_business_as_name = self.lic_bus.doing_business_as_name.apply(
            lambda x: x.title().replace('Llc', 'LLC').replace('"', "'").replace('Lp', 'LP'))
        self.lic_bus.legal_name = self.lic_bus.legal_name.apply(
            lambda x: x.title().replace('Llc', 'LLC').replace('"', "'").replace('Lp', 'LP'))
        self.lic_bus.license_start_date = self.lic_bus.license_start_date.apply(lambda x: x[:10])
        self.lic_bus.expiration_date = self.lic_bus.expiration_date.apply(lambda x: x[:10])

        return self.lic_bus.sort_values('license_id')

    @property
    def owners(self):
        # Merge with lic_buss to exclude non-existent account_numbers
        acct_no = self.lic_bus.account_number.drop_duplicates()
        df = pd.DataFrame(acct_no, columns=['account_number'])
        df = df.merge(self.owner, on='account_number', how='inner')

        # Filling null values
        df.owner_first_name.fillna('Not Provided', inplace=True)
        df.owner_last_name.fillna('Not Provided', inplace=True)
        df.owner_title.fillna('Not Provided', inplace=True)

        # Treatment for string entries.
        df.owner_first_name = df.owner_first_name.apply(lambda x: x.title().replace('"', "'"))
        df.owner_last_name = df.owner_last_name.apply(lambda x: x.title().replace('"', "'"))
        df.owner_title = df.owner_title.apply(lambda x: x.title())

        return df.sort_values('account_number')
