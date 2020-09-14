import lib_api.connect_api as lib
import clean_data.clean_data as cld
import get_query as query

# Get data from API
data = cld.DataPrep(lib.get_bus_lic_data(), lib.get_owners_data())

# Clean data
bus_lic_df = data.bus_lic
owners_df = data.owners

# Write queries
query.write_buss_query(bus_lic_df)
query.write_lic_query(bus_lic_df)
query.write_loc_query(bus_lic_df)
query.write_owners_query(owners_df)
