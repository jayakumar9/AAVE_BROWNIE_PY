# create this file under AAVE_BROWNIE_PY/scripts refer at video 3.solidity time 1:23:52

frrom scripts.helpful_scripts import get_account
from brownie import interface,config,network



def main():
    get_weth()
    
    
def get_weth():
    """
    Mints WETH by depositing ETh.
    
    """
    # ABI
    # Address
    account=get_account()
    weth=interface.IWeth(config["networks"][network.show_active()]["weth_token"]
                         
    
    
