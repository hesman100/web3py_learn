# automatic detection

from ens.auto import ns

# or, with a provider
from web3        import Web3
from ens         import ENS
# Note: This inherits the w3 middlewares from the w3 instance and adds a stalecheck middleware to the middleware onion.
# It also inherits the provider and codec from the w3 instance, as well as the ``strict_bytes_type_checking`` flag value.
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # tree.dot.vn #mainet
ns = ENS.from_web3(w3)

# get the domain data
import sys

# Get the arguments from the command line
arguments = sys.argv

# The first argument is always the name of the script
script_name = arguments[0]

# The rest of the arguments are the arguments passed to the script
args_list = arguments[1:]

# Process the arguments as required
print("Script Name: ", script_name)
print("Arguments: ", args_list)

from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["ENS_name", "ADDR_owner", "Expired_day"]
x.align["ENS_name"]   = "l"
x.align["ADDR_owner"] = "l"
x.align["Expired_day"] = "l"

## ==============
if len(args_list) == 0:
     print(f' Pls give me and ENS name')
     exit
else:
    for m_ens_name in args_list:
        last_four_chars = m_ens_name[-4:]
        # Check if the last four characters are '.eth'
        if last_four_chars != '.eth':
#              print("Last four characters of the argument are not '.eth', so I added it automatically")     
            m_ens_name += '.eth'
        owner_address = ns.owner(m_ens_name)
        if owner_address == '0x0000000000000000000000000000000000000000':
            x.add_row([m_ens_name, "0x0", "00-00-00"])                #              print(f' The ENS domain [ {m_ens_name} ] doesnt have owner')
        else:
            # get the resolver contract
            resolver_address = ns.resolver(m_ens_name)
            resolver = w3.eth.contract(address=resolver_address, abi=ns.ABIResolver)
            expiration_timestamp = resolver.functions.ttl(ns.namehash(m_ens_name)).call()
#                        
            # convert the timestamp to a human-readable date
            expiration_date = datetime.fromtimestamp(expiration_timestamp).strftime('%Y-%m-%d %H:%M:%S')
            x.add_row([m_ens_name, owner_address, expiration_date])        #              print(f' The ENS domain [ {m_ens_name} ] is owned by:   { owner_address }')


#  x.border = False

print(x)    


