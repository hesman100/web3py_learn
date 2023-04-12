# automatic detection
from ens.auto import ns

# or, with a provider
from web3        import Web3
from ens         import ENS
# Note: This inherits the w3 middlewares from the w3 instance and adds a stalecheck middleware to the middleware onion.
# It also inherits the provider and codec from the w3 instance, as well as the ``strict_bytes_type_checking`` flag value.
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/bdf81e81d0a447a1ac196b78cfad01ac'))  # tree.dot.vn #mainet
ns = ENS.from_web3(w3)



## ==============
m_ens_name = "tesla.eth"
eth_address = ns.address(m_ens_name)

print(f' ens_name: {m_ens_name}      is_address:   { eth_address }')


domain_name = ns.name(eth_address)
print(f' address:   { eth_address }  has_name:     {domain_name}' )



# find owner of a ens name :

owner_address = ns.owner(m_ens_name)

print(f' Owner of {m_ens_name}      is_address:   { owner_address }')

