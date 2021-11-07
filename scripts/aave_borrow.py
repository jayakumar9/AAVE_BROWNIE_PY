# create this file under AAVE_BROWNIE_PY/scripts

from brownie import network, config, interface
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth

def main():
    account=get_account()
    erc20_address=config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
    # ABI
    # Address
    lending_pool=get_lending_pool()
    print(lending_pool)
    # Approve sending out ERC20 tokens
    # Approve_erc20()

def Approve_erc20():
    # ABI
    # Address
    
     
def get_lending_pool():
    # ABI
    # Address
    lending_pool_addresses_provider=interface.ILendingPoolAddressesProvider(config["networks"]["network.show_active()]["lending_pool_addresses_provider"])
    lending_pool_address= lending_pool_addresses_provider.getLendingPool()   
    # ABI
    # Address-check! 
    lending_pool= interface.ILendingPool(lending_pool_address)                                                                                               
    return lending_pool                                                                                               
    
    
