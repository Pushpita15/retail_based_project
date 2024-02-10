import pandas as pd
import json

#function to load data
def load_data(path):
    with open(path,'r') as file:
        data = json.load(file)
    return data
    

#function to map each vendor to a unique integer
def map_vendors(data):
    vendors = list(data.keys())
    vendors_map = {vendors[i]:i for i in range(len(vendors))}
    return vendors_map

#function to map each pincode to a unique integer
def map_pincodes(data):
    firstKey = list(data.keys())
    firstKey = firstKey[0]
    pincodes = list(data[firstKey].keys())
    pincodes_map = {pincodes[i]:i for i in range(len(pincodes))}
    return pincodes_map