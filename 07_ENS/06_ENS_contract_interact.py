

import sys
import os
import re


from hexbytes    import HexBytes
from prettytable import PrettyTable
from web3        import Web3
from ens         import ENS



# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # tree.dot.vn #mainet
#  w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # Gorli
ns = ENS.from_web3(w3)


## ens contract info:
contract_address = "0x283Af0B28c62C092C9727F1Ee09c02CA627EB7F5"  # Contract Name: ETHRegistrarController  // https://etherscan.io/address/0x283af0b28c62c092c9727f1ee09c02ca627eb7f5#code

import json
#  with open("contract/ens/ens_registrar_abi.json") as f:
# conver single line json to multiple_lines: $jq . myjsonfile.json > pretty.json
with open("contract/ens/ens_registrar_abi_multiline.json") as f:
    json_lines = json.load(f)
abi_of_contract = json_lines["result"]    


m_name_hash_bin = ns.namehash("vozer.eth")   ## binformat
print (m_name_hash_bin.hex())
m_name_hash = m_name_hash_bin.hex() ## using Hex format
#  ens_name_hash = "0xf4a38d09ff3bcf47c8de7c860e97995856ec6b71663b54854ed6fa35f3689429"  ## hash of vozer.eth
#  print(f' ens_name_hash by webtool: {ens_name_hash} ')  # https://swolfeyes.github.io/ethereum-namehash-calculator/
#  contract_address = "0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85"

contract_instance = w3.eth.contract(address=contract_address, abi=abi_of_contract)


#  try_read = contract_instance.functions.nameExpires(ens_name_hash).call()  // not list in ABI
try_read = contract_instance.functions.available(m_name_hash).call() 
print (try_read)
print(f' is available? : {try_read} ')  

#  owner_addr = contract_instance.functions.owner(m_name_hash_bin).call() 
#  print(f' owner_addr : {owner_addr} ')  







#  tx_hash_wr = contract_instance.functions.setVar(19).transact()
#  tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash_wr)
#  print("Transaction receipt mined:")
#  pprint.pprint(dict(tx_receipt))



