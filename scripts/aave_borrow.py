# create this file under AAVE_BROWNIE_PY/scripts

from brownie import network, config, interface
from scripts.helpful_scripts import get_account
from scripts.get_weth import get_weth
from web3 import web3

#0.1
amount=web3.towei(0.1,"ether")

def main():
    account=get_account()
    erc20_address=config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
    # ABI
    # Address
    lending_pool=get_lending_pool()
    //print(lending_pool)
    #approve sending out ERC20 tokens
    approve_erc20(amount,lending_pool.address,erc20_address,account)
   

def Approve_erc20(amount,spender,erc20_address,account):
    print("Approving ERC20 token...")
    erc20= interface.IERC20(erc20_address)
    tx=erc20.approve(spender,amount,{"from":account})
    tx.wait(1)
    print("Approved!)
    return tx
             
  
    
     
def get_lending_pool():
    # ABI
    # Address
    lending_pool_addresses_provider=interface.ILendingPoolAddressesProvider(config["networks"]["network.show_active()]["lending_pool_addresses_provider"])
    lending_pool_address= lending_pool_addresses_provider.getLendingPool()   
    # ABI
    # Address-check! 
    lending_pool= interface.ILendingPool(lending_pool_address)                                                                                               
    return lending_pool                                                                                               
    
    
