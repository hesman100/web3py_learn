

import sys
import os
import re


from hexbytes import HexBytes
from prettytable import PrettyTable
from web3        import Web3



# Connect to an Ethereum node
#  w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # tree.dot.vn  mainet
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # Gorli

print ( "current block num: %d" % w3.eth.block_number)
block_info = w3.eth.get_block('latest')  # this is dictionary type

m_addr        = '0x978Ef1d5132df748AaECF72b273103010739dB75'
m_balance_wei = w3.eth.get_balance(m_addr) ; # andes.eth
print ( "current balance of addr: %s =  %d (wei)" %  (m_addr, m_balance_wei) )


m_balance_eth = w3.from_wei(m_balance_wei, 'ether')
# Format the value to display only 4 decimal places
formatted_value = '{:.4f}'.format(m_balance_eth)

print ( "current balance of addr: %s =  %s (eth)" %  (m_addr, formatted_value) )



   

#_ json_parse = json.loads(block_info)
#_ print(json.dump(json_parse, indent=4))

