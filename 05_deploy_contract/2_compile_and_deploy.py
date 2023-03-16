

import json
from web3 import Web3, HTTPProvider

from solcx import install_solc, compile_source
install_solc(version='latest')

# Read the Solidity contract code from a file
with open('./1_contract.sol', 'r') as file:
    contract_source_code = file.read()

# Compile the Solidity contract
compiled_sol = compile_source(contract_source_code, output_values=['abi', 'bin'] )


# Print the compiled contract object
print(compiled_sol)


print ("================ Collect some info : ==========================")

contract_id, contract_interface = compiled_sol.popitem()

#  get bytecode / bin
bytecode = contract_interface['bin']
print ("================ contract bytecode : ==========================")
print (bytecode)
#  get abi
abi = contract_interface['abi']
print ("================ contract abi (json): ==========================")

print(json.dumps(abi, indent=4))
#  print (abi)





print ("================ deploying contract : ==========================")
### deploy part ===================
# web3.py instance
# Connect to the Ethereum network using Infura HTTPProvider
#  w3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/your-project-id'))
web3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # Gorli


# set pre-funded account as sender
#  web3.eth.default_account = web3.eth.accounts[0]
# 3. Create address sender   #goerli
account_from = {
    'private_key': 'f61e3e3257460632f8e5ee74dc523b9fd3b6a778504515114dfcf9aa5747276b',
    'address': '0x8958EB26b43Fb7d36C2D085cAB5a1D4075648DeA',
}

# contract instance need_to_deployed ( contract_ntd)
contract_ntd = web3.eth.contract(abi=abi, bytecode=bytecode)

#  Build constructor tx
construct_txn = contract_ntd.constructor(5).build_transaction(
    {
        'from': account_from['address'],
        'nonce': web3.eth.get_transaction_count(account_from['address']),
    }
)
#  Sign tx with private_key
tx_create = web3.eth.account.sign_transaction(construct_txn, account_from['private_key'])

#  Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Contract deployed at address: { tx_receipt.contractAddress }')


# my 1st contract : 0xabfe5186B5B6115393E18eA3d15F24cbaaAa4F58


