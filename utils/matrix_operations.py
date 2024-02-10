from scipy.sparse import csr_matrix
import pandas as pd


#function to convert the json data to a csr matrix
def convert_to_csr(data):
    df = pd.DataFrame(data).T
    csr = csr_matrix(df.values)
    return csr

#function to check serviceability of a pincode
def check_pincode_serviceability_helper(pincode,csr,vendor_map,pincode_map):
    if pincode not in pincode_map:
        return []
    arr = csr.getcol(pincode_map[pincode]).toarray()
    vendors = []
    for i in range(len(arr)):
        if arr[i] != 0:
            vendors.append(list(vendor_map.keys())[i])
    return vendors
