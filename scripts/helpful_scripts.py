# create this file under  AAVE_BROWNIE_PY/scripts refer video 1:29:27


def get_account(index=None,id=None):
    #accounts[0]
    #accounts.add("env")
    #accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if(
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
      ):  
        return accounts[0]
    
