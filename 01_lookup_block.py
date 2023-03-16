

import sys
import os
import re


from hexbytes import HexBytes
from prettytable import PrettyTable
from web3        import Web3
#_ from eth_utils import keccak


# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # tree.dot.vn

block_info = w3.eth.get_block(12345)  # this is dictionary type

x = PrettyTable()
x.field_names = ["Key", "Value", "Value_type"]
x.align["Key"]   = "l"
x.align["Value"] = "l"
x.align["Value_type"] = "l"

m_int_pattern = r'b\'(.*)'  # b'Geth/v1.0.0/linux/go1.4.2'   | b'1\xd9\xec~8U\xae\xba7\xfd\x9
m_hex_pat  = r'<class \'hexbytes.main.HexBytes\'>'  # <class 'hexbytes.main.HexBytes'>

#  data = b'1\xd9\xec~8U\xae\xba7\xfd\x92\xaa\x169\x84^p\xb3`\xa6\x0fw\xf1.\xffS\x04)\xef\x8c\xfc\xba'

#  hex_data = HexBytes(data)

#  print(hex_data)


for key, value in block_info.items():
    st_value = str(value)
    type_of_val = str(type(value))
#      print (type_of_val)
    m_hex_match = re.search(m_hex_pat, type_of_val)
    if m_hex_match:

        hex_val = value.hex()
        st_value = str(hex_val)
#          print (hex_val)
    
    

    if len(st_value) > 30:
        st_value = st_value[:30] + "..."

    x.add_row([key, st_value, type_of_val])

print (" row count: %d " % len(x._rows) )

        
x.border = False

print(x)    
   

#_ json_parse = json.loads(block_info)
#_ print(json.dump(json_parse, indent=4))

