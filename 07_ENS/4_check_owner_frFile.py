# automatic detection

from ens.auto import ns

# or, with a provider
from web3        import Web3
from ens         import ENS
# Note: This inherits the w3 middlewares from the w3 instance and adds a stalecheck middleware to the middleware onion.
# It also inherits the provider and codec from the w3 instance, as well as the ``strict_bytes_type_checking`` flag value.
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # tree.dot.vn #mainet
ns = ENS.from_web3(w3)

import sys

# Get the file name from the command line
file_name = sys.argv[1]
args_list = []

# Open the file for reading
with open(file_name, 'r') as file:
    # Read the file line by line
    for line in file:
        # Strip any whitespace from the line and store it as an argument
        argument = line.strip()
        args_list.append(argument)

        # Do something with the argument, e.g. print it
        print(argument)


# The first argument is always the name of the script
script_name = sys.argv[0]

# Process the arguments as required
print("Script Name: ", script_name)
print("Arguments: ", args_list)

from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["ENS_name", "ADDR_owner"]
x.align["ENS_name"]   = "l"
x.align["ADDR_owner"] = "l"

## ==============
if len(args_list) == 0:
     print(f' Pls give me and ENS name')
     exit
else:
    for m_ens_name in args_list:
        last_four_chars = m_ens_name[-4:]
        # Check if the last four characters are '.eth'
        if last_four_chars != '.eth':
            print("Last four characters of the argument are not '.eth', so I added it automatically")     
            m_ens_name += '.eth'
        owner_address = ns.owner(m_ens_name)
        if owner_address == '0x0000000000000000000000000000000000000000':
            x.add_row([m_ens_name, "0x0"])                #              print(f' The ENS domain [ {m_ens_name} ] doesnt have owner')
        else:
            x.add_row([m_ens_name, owner_address])        #              print(f' The ENS domain [ {m_ens_name} ] is owned by:   { owner_address }')


#  x.border = False

print(x)    


